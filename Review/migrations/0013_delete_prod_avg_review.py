# Generated by Django 4.2.7 on 2023-11-25 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0012_prod_avg_review_avg_rating_star'),
    ]

    operations = [
        migrations.DeleteModel(
            name='prod_avg_review',
        ),
    ]