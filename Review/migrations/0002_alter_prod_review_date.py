# Generated by Django 4.2.7 on 2023-11-22 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prod_review',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
