from django.db import models

# Create your models here.

class Customer(models.Model):
    cus_name = models.CharField(max_length=50)
    mail_id = models.EmailField()
    mobile = models.IntegerField()
    address = models.CharField(max_length=200)
    dob = models.DateField()

    def __str__(self):
        return self.cus_name

class Custpro(models.Model):
    size_w = models.IntegerField()
    size_h = models.IntegerField()
    quantity = models.IntegerField()
    requirements = models.CharField(max_length=500)
    painting_choice = [('Tanjore','Tanjore'),('Acrylic','Acrylic'),('Oil','Oil'),('Pencil sketch','Pencil sketch')]
    painting_type = models.CharField(choices=painting_choice,max_length=20,default=None)
    type_choice = [('Flat work', 'Flat work'), ('2D', '2 Dimension'), ('3D', '3 Dimension')]
    type_type = models.CharField(choices=type_choice, max_length=20, default=None)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.cus_name +' '+ self.painting_type +' '+ self.type_type







