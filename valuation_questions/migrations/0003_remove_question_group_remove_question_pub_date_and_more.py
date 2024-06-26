# Generated by Django 5.0.6 on 2024-06-13 17:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "valuation_questions",
            "0002_remove_question_question_group_question_group_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="group",
        ),
        migrations.RemoveField(
            model_name="question",
            name="pub_date",
        ),
        migrations.RemoveField(
            model_name="questiongroup",
            name="text",
        ),
        migrations.AddField(
            model_name="question",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="question",
            name="question_group",
            field=models.ForeignKey(
                default=django.utils.timezone.now,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="valuation_questions.questiongroup",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="questiongroup",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="question",
            name="text",
            field=models.CharField(max_length=500),
        ),
    ]
