from django.urls import path
from . import views

urlpatterns = [
    path('worker/signup/',views.worker_signup,name='worker-signup'),
    path('worker/signout/',views.worker_signout,name='worker-signout'),
    path('worker/dashboard/',views.worker_dashboard,name='worker-dashboard'),
    path('update/profile',views.update_worker_profile,name='update-profile'),
    path('jobprofile/',views.job_profile,name='job-profile'),
    path('add/job/',views.add_job_profile,name='add-job')
]
