# Generated by Django 5.0.3 on 2024-03-21 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
