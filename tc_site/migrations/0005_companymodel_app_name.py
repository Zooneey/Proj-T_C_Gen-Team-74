# Generated by Django 4.0.6 on 2022-08-04 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tc_site', '0004_alter_documentmodel_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='companymodel',
            name='app_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
