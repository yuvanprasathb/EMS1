# Generated by Django 4.2.4 on 2023-09-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_employees_employee_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Employee_Code',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
