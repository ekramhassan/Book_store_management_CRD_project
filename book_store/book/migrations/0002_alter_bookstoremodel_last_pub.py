# Generated by Django 5.0.6 on 2024-05-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstoremodel',
            name='last_pub',
            field=models.DateField(auto_now=True),
        ),
    ]
