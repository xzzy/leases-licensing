# Generated by Django 3.2.21 on 2023-09-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaseslicensing', '0265_delete_requireddocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicingdetails',
            name='review_once_every',
            field=models.PositiveSmallIntegerField(blank=True, default=5, null=True),
        ),
    ]