# Generated by Django 4.0.4 on 2022-04-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='books',
            field=models.ManyToManyField(to='book.book'),
        ),
    ]
