from django.db import models



class Post(models.Model):
	LoanReason  = models.CharField(max_length=25)
	Amount		= models.FloatField()
	Discription = models.TextField()
	date		= models.DateTimeField()
	
	def __str__(self):
		return self.LoanReason
