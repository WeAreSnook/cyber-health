# Generated by Django 3.1.7 on 2021-05-07 15:54

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0008_load_pathway_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_intro',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
    ]
