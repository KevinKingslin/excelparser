# Generated by Django 4.1.4 on 2023-04-15 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excelparser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
