# Generated by Django 4.1.7 on 2023-02-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vazifa_card', '0003_remove_sifat_narxi'),
    ]

    operations = [
        migrations.AddField(
            model_name='sifat',
            name='narxi',
            field=models.FloatField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
