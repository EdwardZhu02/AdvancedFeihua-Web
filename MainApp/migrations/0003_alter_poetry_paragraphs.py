# Generated by Django 4.0.1 on 2022-03-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_remove_poetry_rhythmic_rank_baidu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poetry',
            name='paragraphs',
            field=models.TextField(max_length=3000),
        ),
    ]
