from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Mission, SpyCat, Target
from .serializers import MissionSerializer, SpyCatSerializer, TargetUpdateSerializer

# Create your views here.

class CatAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            cat = get_object_or_404(SpyCat, pk=pk)
            serializer = SpyCatSerializer(cat)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        cats = SpyCat.objects.all()
        serializer = SpyCatSerializer(cats, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = SpyCatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk): # full update of a cat by id
        cat = get_object_or_404(SpyCat, pk=pk)
        serializer = SpyCatSerializer(cat, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        cat = get_object_or_404(SpyCat, pk=pk)
        serializer = SpyCatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        cat = get_object_or_404(SpyCat, pk=pk)
        cat.delete()
        return Response(
            {"message": "Cat has been deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )


class MissionAPIView(APIView):
    def get(self, request, pk=None): # getting all missions in the database
        if pk:
            mission = get_object_or_404(Mission, pk=pk)
            serializer = MissionSerializer(mission)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        missions = Mission.objects.all()
        serializer = MissionSerializer(missions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request): # creating a new mission
        serializer = MissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk): # full update of a mission by id
        mission = get_object_or_404(Mission, pk=pk)
        serializer = MissionSerializer(mission, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk): # partial update of a mission by id
        mission = get_object_or_404(Mission, pk=pk)
        serializer = MissionSerializer(mission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk): # deletion of a mission by id
        mission = get_object_or_404(Mission, pk=pk)

        if mission.cat:
            return Response(
                {"error": "Cannot delete mission since it is already assigned to a cat."},
                status=status.HTTP_400_BAD_REQUEST
            )
        mission.delete()

        return Response(
            {"message": "Mission has been deleted successfully."},
            status=status.HTTP_200_OK
        )
    
class UpdateTargetView(APIView):
    def patch(self, request, mission_id, target_id):
        try:
            mission = Mission.objects.get(id=mission_id)
        except Mission.DoesNotExist:
            return Response({'detail': 'Mission not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            target = Target.objects.get(id=target_id, mission=mission)
        except Target.DoesNotExist:
            return Response({'detail': 'Target not found in this mission.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TargetUpdateSerializer(target, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)