from django.db import models

class CatFact(models.Model):
	fact = models.TextField()
	created_at = models.DateTimeField(auto_now_add =True)

	def __str__(self):
		return self.fact[:50]