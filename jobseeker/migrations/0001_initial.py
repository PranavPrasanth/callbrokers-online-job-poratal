# Generated by Django 4.0.3 on 2022-03-24 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0002_vaccany_delete_work1'),
        ('account', '0007_engineer_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplayJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=10)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.vaccany')),
                ('jobseeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.jobseeker')),
            ],
        ),
    ]