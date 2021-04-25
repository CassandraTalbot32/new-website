from django.db import models

# Create your models here.
class Entry(models.Model):
	Title		= models.CharField(max_length=120)
	Description = models.TextField(blank=True, null=True)
	Price		= models.DecimalField(decimal_places=2, max_digits=10)
	Summary		= models.TextField()
	Date		= models.DateField(null=True)
	Contact		= models.EmailField(null=True)



	


