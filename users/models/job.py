from django.db import models
from ..models import CustomUser


class JobType(models.Model):
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_name
    
class WorkerProfile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='worker')
    profile_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='worker/profile',blank=True,null=True)

    def __str__(self):
        return self.profile_name
    
class JobProfile(models.Model):
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, related_name='job_profile')
    job_category = models.ForeignKey(JobType,on_delete=models.CASCADE)
    description = models.TextField()
    job_profile_pic = models.ImageField(upload_to='job/profile',blank=True,null=True)
    max_amount_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    is_negotiable = models.BooleanField(default=True)

    def __str__(self):
        return f"Job profile of {self.worker.profile_name}"