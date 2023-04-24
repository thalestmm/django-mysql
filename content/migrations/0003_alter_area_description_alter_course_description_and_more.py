# Generated by Django 4.2 on 2023-04-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_area_module_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='videolecture',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
