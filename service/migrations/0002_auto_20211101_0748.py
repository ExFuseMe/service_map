# Generated by Django 3.2.4 on 2021-11-01 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carservice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='carservice',
            name='position',
            field=models.CharField(max_length=15),
        ),
    ]
