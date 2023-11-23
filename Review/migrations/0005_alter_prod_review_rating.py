# Generated by Django 4.2.7 on 2023-11-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0004_alter_prod_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prod_review',
            name='rating',
            field=models.CharField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, 'five')], max_length=5),
        ),
    ]
