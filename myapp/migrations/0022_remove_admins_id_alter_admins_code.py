# Generated by Django 4.2.4 on 2023-09-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_admins_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admins',
            name='id',
        ),
        migrations.AlterField(
            model_name='admins',
            name='code',
            field=models.AutoField(default=102, primary_key=True, serialize=False),
        ),
    ]
