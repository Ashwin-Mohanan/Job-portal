# Generated by Django 4.0.2 on 2022-04-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_rename_location_resume_college_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='education',
            field=models.CharField(choices=[('10', '10'), ('12', '12'), ('Bsc', 'Bsc'), ('Bsc(Computer Science)', 'Bsc(Computer Science)'), ('Bsc(I.T)', 'Bsc(I.T)'), ('MSC', 'MSC'), ('MCA', 'MCA'), ('B.com', 'B.com'), ('M.com', 'M.com'), ('BMS', 'BMS'), ('BBA', 'BBA')], default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='resume',
            name='work_details',
            field=models.CharField(default='none', max_length=100),
        ),
    ]