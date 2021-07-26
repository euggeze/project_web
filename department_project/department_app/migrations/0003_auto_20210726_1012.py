# Generated by Django 3.2.5 on 2021-07-26 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department_app', '0002_auto_20210726_0706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name'], 'verbose_name': 'Department names'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['name'], 'verbose_name': 'Employee information'},
        ),
        migrations.RenameField(
            model_name='department',
            old_name='id_department',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='name_department',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='id_department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='id_employee',
            new_name='id',
        ),
        migrations.AlterModelTable(
            name='department',
            table='department_app_department',
        ),
        migrations.AlterModelTable(
            name='employee',
            table='department_app_employee',
        ),
    ]
