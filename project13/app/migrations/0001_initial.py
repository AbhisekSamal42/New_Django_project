# Generated by Django 5.0.7 on 2024-10-04 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BONUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ENAME', models.CharField(max_length=10)),
                ('JOB', models.CharField(max_length=9)),
                ('SAL', models.IntegerField()),
                ('COMM', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DEPT',
            fields=[
                ('DEPTNO', models.IntegerField(primary_key=True, serialize=False)),
                ('DNAME', models.CharField(max_length=14)),
                ('LOC', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='SALGRADE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GRADE', models.IntegerField()),
                ('LOSAL', models.IntegerField()),
                ('HISAL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EMP',
            fields=[
                ('EMPNO', models.IntegerField(primary_key=True, serialize=False)),
                ('ENAME', models.CharField(max_length=10)),
                ('JOB', models.CharField(max_length=9)),
                ('HIREDATE', models.DateField()),
                ('SAL', models.FloatField(max_length=7)),
                ('COMM', models.FloatField(blank=True, max_length=7, null=True)),
                ('DEPTNO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
                ('MGR', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.emp')),
            ],
        ),
    ]
