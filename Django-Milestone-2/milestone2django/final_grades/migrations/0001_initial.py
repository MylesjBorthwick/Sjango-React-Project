# Generated by Django 3.1.4 on 2021-01-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Final_Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_grades_id', models.IntegerField()),
                ('course_outline_id', models.IntegerField()),
                ('weight', models.TextField()),
                ('finalGrade', models.TextField()),
                ('name', models.TextField()),
            ],
        ),
    ]
