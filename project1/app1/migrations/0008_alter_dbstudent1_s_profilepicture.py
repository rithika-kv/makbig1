# Generated by Django 5.1.7 on 2025-05-21 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_dbstudent1_s_guardianphonenumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbstudent1',
            name='s_profilepicture',
            field=models.ImageField(blank=True, null=True, upload_to='profilepics/'),
        ),
    ]
