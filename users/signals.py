# from .models import CompanyDocuments,CompanyProfile
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# @receiver(post_save, sender=CompanyProfile)
# def create_documents(sender, instance, created, **kwargs):
#     print("signal")
#     if created:
#         CompanyDocuments.objects.create(company=instance)