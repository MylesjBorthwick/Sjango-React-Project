# Generated by Django 3.1.4 on 2021-01-08 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommended_Textbooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textbook_id', models.IntegerField()),
                ('course_outline_id', models.IntegerField()),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('edition', models.TextField()),
                ('publisher', models.TextField()),
            ],
        ),
    ]
