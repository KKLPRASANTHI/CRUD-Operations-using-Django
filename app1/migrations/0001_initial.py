# Generated by Django 3.0.8 on 2020-07-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(null=True)),
                ('salary', models.FloatField(null=True)),
                ('desig', models.CharField(max_length=50, null=True)),
                ('pno', models.IntegerField(null=True)),
            ],
        ),
    ]
