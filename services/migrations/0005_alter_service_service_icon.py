# Generated by Django 4.1.7 on 2023-07-05 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_delete_visit_alter_service_service_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_icon',
            field=models.CharField(max_length=250),
        ),
    ]
