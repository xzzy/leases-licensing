# Generated by Django 3.2.18 on 2023-09-01 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaseslicensing', '0256_financialmonth'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposalapplicant',
            name='emailuser_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
