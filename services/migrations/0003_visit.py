# Generated by Django 4.1.7 on 2023-06-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_service_service_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place_type', models.CharField(choices=[('national', 'national'), ('worldwide', 'worldwide'), ('regional', 'regional')], max_length=50)),
            ],
        ),
    ]
