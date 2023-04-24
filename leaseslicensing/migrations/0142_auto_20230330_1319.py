# Generated by Django 3.2.18 on 2023-03-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaseslicensing', '0141_emailuserlogdocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvaluseraction',
            name='who_full_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='competitiveprocessuseraction',
            name='who_full_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='complianceuseraction',
            name='who_full_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='emailuseraction',
            name='who_full_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='organisationaction',
            name='who_full_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='organisationrequestuseraction',
            name='who_full_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='proposaluseraction',
            name='who_full_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]