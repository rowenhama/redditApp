# Generated by Django 3.1.3 on 2021-02-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('emp_cod', models.CharField(max_length=4)),
                ('mobile', models.CharField(max_length=15)),
            ],
        ),
    ]
