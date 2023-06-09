# Generated by Django 4.2 on 2023-04-24 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_area_created_at_area_updated_at_course_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='videolecture',
            name='lecture_text',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.CreateModel(
            name='TextLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('index', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lecture_text', models.TextField(blank=True, max_length=1000, null=True)),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.module')),
            ],
            options={
                'ordering': ['module', 'index', 'name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('index', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lecture_text', models.TextField(blank=True, max_length=1000, null=True)),
                ('question_text', models.TextField(max_length=500)),
                ('alt_a', models.CharField(max_length=50)),
                ('alt_b', models.CharField(max_length=50)),
                ('alt_c', models.CharField(max_length=50)),
                ('alt_d', models.CharField(max_length=50)),
                ('helper_text_a', models.TextField(blank=True, max_length=200, null=True)),
                ('helper_text_b', models.TextField(blank=True, max_length=200, null=True)),
                ('helper_text_c', models.TextField(blank=True, max_length=200, null=True)),
                ('helper_text_d', models.TextField(blank=True, max_length=200, null=True)),
                ('correct_alternative', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1)),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.module')),
            ],
            options={
                'ordering': ['module', 'index', 'name'],
                'abstract': False,
            },
        ),
    ]
