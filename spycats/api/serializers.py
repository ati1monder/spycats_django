from rest_framework import serializers

from .models import *

class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['id', 'name', 'years_of_experience', 'breed', 'salary']

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'complete']

class TargetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'complete'] 

    def validate(self, data):
        target = self.instance

        if target.complete or target.mission.complete:
            if 'notes' in data and data['notes'] != target.notes:
                raise ValidationError("Cannot update notes since the target or the mission is completed.")
        
        return data

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True) # we assume that there will be an array of objects

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'complete', 'targets']
    
    def create(self, validated_data):
        targets_data = validated_data.pop('targets') # we remove "targets" since it's not a part of "Mission" model for its successfull creation
        mission = Mission.objects.create(**validated_data)
        
        for data in targets_data:
            Target.objects.create(mission=mission, **data)
        
        return mission
    
    def update(self, instance: Mission, validated_data):
        targets_data = validated_data.pop('targets', None) 
        instance.cat = validated_data.get('cat', instance.cat)
        instance.complete = validated_data.get('complete', instance.complete)
        instance.save()

        if targets_data: # checking if we have targets_data
            for data in targets_data:
                t_id = data.get('id') #
                if t_id:
                    target = Target.objects.get(id=t_id, mission=instance)
                    for attr, value in data.items():
                        setattr(target, attr, value)
                    target.save()
                else:
                    Target.objects.create(mission=instance, **data)
        return instance