# Generated by Django 4.2.4 on 2023-09-13 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_admins'),
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='admins',
        ),
    ]
