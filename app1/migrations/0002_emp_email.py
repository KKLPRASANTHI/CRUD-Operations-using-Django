# Generated by Django 3.0.8 on 2020-07-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
