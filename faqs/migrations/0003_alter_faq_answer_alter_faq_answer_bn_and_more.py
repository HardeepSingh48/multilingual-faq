# Generated by Django 5.1.5 on 2025-02-02 10:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0002_rename_question_en_faq_question_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_bn',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_hi',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
