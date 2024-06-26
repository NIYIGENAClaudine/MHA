# Generated by Django 5.0.6 on 2024-06-01 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_therapist_booking"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.CharField(
                choices=[
                    ("Depression", "Depression"),
                    ("Anxiety", "Anxiety"),
                    ("Stress Management", "Stress Management"),
                    ("Mindfulness and Meditation", "Mindfulness and Meditation"),
                    ("Traumatic Disorder", "Traumatic Disorder"),
                ],
                default="Depression",
                max_length=50,
            ),
        ),
    ]
