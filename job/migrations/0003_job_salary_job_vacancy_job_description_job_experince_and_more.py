# Generated by Django 4.2.1 on 2023-07-24 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_jobtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='Vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='experince',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='publish_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
