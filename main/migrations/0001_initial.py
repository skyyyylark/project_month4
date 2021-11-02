# Generated by Django 3.2.6 on 2021-10-23 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laws',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('full_description', models.TextField()),
                ('date', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('type', models.IntegerField(choices=[(1, 'действующие законодательства'), (2, 'проэкты нормативных актов'), (3, 'международные документы')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('full_description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(null=True, upload_to='news')),
                ('link', models.URLField()),
                ('is_main', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('full_description', models.TextField()),
                ('date', models.DateField()),
                ('file', models.FileField(upload_to='files')),
                ('type', models.IntegerField(choices=[(1, 'Публикации ICNL '), (2, 'Другие публикации')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ImageNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.news')),
            ],
        ),
    ]
