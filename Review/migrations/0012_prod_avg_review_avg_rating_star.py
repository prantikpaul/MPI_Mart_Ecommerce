# Generated by Django 4.2.7 on 2023-11-25 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0011_prod_review_int_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod_avg_review',
            name='avg_rating_star',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
