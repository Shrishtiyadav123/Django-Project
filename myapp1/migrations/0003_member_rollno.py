# Generated by Django 5.0 on 2024-01-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_member_phoneno'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='rollno',
            field=models.IntegerField(null=True),
        ),
    ]
