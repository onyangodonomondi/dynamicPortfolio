# Generated by Django 4.1.2 on 2022-10-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_experience_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('level', models.IntegerField(blank=True, default=50, null=True)),
            ],
        ),
    ]