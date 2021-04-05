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


class Orders(models.Model):
    order_id = models.IntegerField()
    date = models.DateField(help_text="format : YYYY-MM-DD")
    p_code = models.CharField(max_length=10)
    p_name = models.CharField(max_length=25)
    p_painting_choice = [('Tanjore', 'Tanjore'), ('Acrylic', 'Acrylic'), ('Oil', 'Oil'),
                       ('Pencil sketch', 'Pencil sketch')]
    p_painting_type = models.CharField(choices=p_painting_choice, max_length=20, default=None)
    p_type_choice = [('Flat work', 'Flat work'), ('2D', '2 Dimension'), ('3D', '3 Dimension')]
    p_type_type = models.CharField(choices=p_type_choice, max_length=20, default=None)
    psize_w = models.IntegerField()
    psize_h = models.IntegerField()
    p_price = models.IntegerField()
    p_quantity = models.IntegerField()
    p_totalprice = models.IntegerField()
    p_dispatchedstatus = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.customer.cus_name + ' '+ str(self.order_id)


class Stock(models.Model):

    purchase_id = models.CharField(max_length=12)
    s_date = models.DateField(help_text="format : YYYY-MM-DD")
    sp_name = models.CharField(max_length=25)
    sd_name = models.CharField(max_length=25)
    sp_type = models.CharField(max_length=25)
    s_size_w = models.CharField(max_length=7)
    s_size_h = models.CharField(max_length=7)
    s_price = models.IntegerField()
    s_quantity = models.CharField(max_length=7)
    s_totalprice = models.IntegerField()

    def __str__(self):
        return self.sd_name + ' '+ str(self.s_totalprice)

class Purchase(models.Model):
    stock_id = models.CharField(primary_key=True,max_length=7)
    s_quantity = models.CharField(max_length=12)

    def __str__(self):
        return self.stock_id + ' '+ self.s_quantity

class Report(models.Model):
    f_date = models.DateField()
    t_date = models.DateField()

    def __str__(self):
        return str(self.f_date) + '        '+ str(self.t_date)
