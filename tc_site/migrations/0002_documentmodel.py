# Generated by Django 4.0.6 on 2022-08-01 01:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tc_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('document', models.FileField(upload_to='tc_site/static/documents')),
                ('document_type', models.CharField(max_length=100)),
                ('date_issued', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tc_site.companymodel')),
            ],
        ),
    ]
