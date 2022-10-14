# Generated by Django 4.0.1 on 2022-03-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_alter_poetry_paragraphs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword1', models.CharField(max_length=64)),
                ('keyword2', models.CharField(max_length=64)),
                ('mode', models.CharField(max_length=64)),
                ('topic_description', models.CharField(max_length=256)),
                ('key_description', models.CharField(max_length=256)),
            ],
        ),
    ]