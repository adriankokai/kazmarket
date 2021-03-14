from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		null=True, blank=True
		)
	first_name = models.CharField(max_length=255, null=True, blank=True)
	last_name = models.CharField(max_length=255, null=True, blank=True)
	is_admin = models.BooleanField(default=False)
	is_manager = models.BooleanField(default=False)
	assigned_manager = models.CharField(max_length=255, default='n/a' )
	team = models.ManyToManyField(Team)	
	photo = models.ImageField(null=True, blank=True)
	banner = models.ImageField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		if self.user:
			return self.user.username
		else:
			return ""

#Now this is where the magic happens: we will now define signals so our 
#Profile model will be automatically created/updated 
#when we create/update User instances.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



