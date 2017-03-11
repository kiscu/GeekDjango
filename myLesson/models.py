from __future__ import unicode_literals

from django.db import models

class Mysite(models.Model):
	title = models.CharField(max_length=100)
	url = models.URLField()
	author = models.CharField(max_length=100)
	num = models.IntegerField()

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['num']
		