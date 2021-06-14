# Generated by Django 3.2.3 on 2021-06-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_empleaverequest_leavebalance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleaverequest',
            old_name='Emp_ID',
            new_name='Emp_No',
        ),
        migrations.AlterField(
            model_name='employee',
            name='Birth_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Emp_No',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='First_Name',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Hire_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Last_Name',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Middle_Name',
            field=models.CharField(max_length=14, null=True),
        ),
    ]