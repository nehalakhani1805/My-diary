from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.
class Entry(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural='Entries'

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk':self.pk})