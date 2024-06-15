import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("valuation_questions", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="question_group",
        ),
        migrations.AddField(
            model_name="question",
            name="group",
            field=models.ForeignKey(
                default=None,  # Set default to None if you want it to be nullable
                null=True,    # Set null=True if you want it to be nullable
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="valuation_questions.QuestionGroup",  # Fix typo in model name
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="questiongroup",
            name="text",
            field=models.CharField(default="", max_length=200),  # Provide a default text
            preserve_default=False,
        ),
    ]
