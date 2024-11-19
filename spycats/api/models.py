from django.db import models
from django.core.exceptions import ValidationError

from .validators import breed_validation

# Create your models here.
class SpyCat(models.Model):
    name = models.CharField('Name', max_length=30)
    years_of_experience = models.PositiveIntegerField('Years of experience')
    breed = models.CharField('Breed', max_length=50, validators=[breed_validation])
    salary = models.IntegerField('Salary') # it is also possible to use DecimalField, but in this scenario IntegerField will be used

class Mission(models.Model):
    cat = models.ForeignKey(SpyCat, on_delete=models.CASCADE, null=True, blank=True)
    complete = models.BooleanField(default=False)

    def delete(self):
        if self.cat is not None:
            raise ValidationError('Cannot delete mission since it is alredy assigned to a cat.')
        super().delete()
        
class Target(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name='targets')
    name = models.CharField('Name', max_length=50)
    country = models.CharField('Country', max_length=50)
    notes = models.TextField('Notes', max_length=500)
    complete = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Target, self).save(*args, **kwargs)