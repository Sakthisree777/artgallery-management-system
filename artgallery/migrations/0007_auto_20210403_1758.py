# Generated by Django 3.1.7 on 2021-04-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artgallery', '0006_orders_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('stock_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('s_quantity', models.CharField(max_length=7)),
            ],
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(help_text='format : YYYY-MM-DD'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='purchase_id',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='stock',
            name='s_date',
            field=models.DateField(help_text='format : YYYY-MM-DD'),
        ),
    ]
