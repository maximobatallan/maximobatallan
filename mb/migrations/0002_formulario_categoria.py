# Generated by Django 4.2.6 on 2023-11-16 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='categoria',
            field=models.CharField(default='categoria', max_length=55),
            preserve_default=False,
        ),
    ]
