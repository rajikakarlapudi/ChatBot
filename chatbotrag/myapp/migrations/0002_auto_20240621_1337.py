# Generated by Django 3.2.25 on 2024-06-21 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='include_in_qa',
        ),
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(choices=[('Education', 'Education'), ('Legal', 'Legal'), ('Finance', 'Finance'), ('Real Estate', 'Real Estate'), ('News & Media', 'News & Media'), ('Others', 'Others')], max_length=50),
        ),
    ]