from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid



# Create your models here.

class Room(models.Model):
	uuid = models.UUIDField(default = uuid.uuid4,editable = False)
	# name = models.CharField(max_length=64, unique=True)
	# description = models.TextField()
	subscribers = models.ManyToManyField(User, blank=True)
	last_message = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.subscribers.all())

	def get_last_message(self):
		return self.message_set.order_by('-created').first()
	
	def messages(self):
		return self.message_set.order_by('created')

class Message(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(default=timezone.now)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	content = models.TextField(null=True, blank=True)
	read = models.BooleanField(default=False)
	time_read = models.DateTimeField(null=True, blank=True)
	archived = models.BooleanField(default=False)