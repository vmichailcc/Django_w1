# Generated by Django 4.0.4 on 2022-06-20 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('released_year', models.IntegerField(max_length=4, verbose_name='Released year')),
                ('description', models.TextField(max_length=5000, verbose_name='Description')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.authors', verbose_name='Author')),
            ],
        ),
    ]
