# Generated by Django 4.1.13 on 2024-01-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0002_remove_quote_author_remove_quote_user_note_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tags',
            field=models.ManyToManyField(blank=True, to='noteapp.tag'),
        ),
    ]
