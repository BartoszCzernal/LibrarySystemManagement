# Generated by Django 3.0.5 on 2020-04-21 08:32

from django.db import migrations
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=isbn_field.fields.ISBNField(default='', max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN'),
        ),
    ]
