# Generated by Django 3.2.23 on 2023-11-22 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaseslicensing', '0300_auto_20231103_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumerpriceindex',
            name='quarter',
            field=models.PositiveSmallIntegerField(help_text='1 = MAR, 2 = JUN, 3 = SEP, 4 = DEC', null=True),
        ),
        migrations.AlterField(
            model_name='cpicalculationmethod',
            name='quarter',
            field=models.PositiveSmallIntegerField(help_text='1 = MAR, 2 = JUN, 3 = SEP, 4 = DEC', null=True),
        ),
    ]