# Generated by Django 4.1.7 on 2023-04-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0005_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthdate",
            field=models.DateField(null=True, verbose_name="Geburtsdatum"),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="E-Mail Adresse"),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=100, verbose_name="Vorname"),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=100, verbose_name="Nachname"),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.EmailField(max_length=254, unique=True, verbose_name="Benutzername"),
        ),
        migrations.AlterField(
            model_name="warn",
            name="reason",
            field=models.CharField(
                choices=[
                    ("Falschinformationen", "Falschinformationen"),
                    ("Missbrauch von Privilegien", "Missbrauch von Privilegien"),
                    ("Belästigung", "Belästigung"),
                    ("Cybermobing", "Cybermobbing"),
                    ("Cybergrooming", "Cybergrooming"),
                    ("Whataboutismus", "Whataboutismus"),
                    ("Relativierung", "Relativierung"),
                    ("Erpressung", "Erpressung"),
                    ("Drohung", "Drohung"),
                    ("Wortwahl", "Wortwahl"),
                    ("Hassrede", "Hassrede"),
                    ("Beleidigung", "Beleidigung"),
                    ("Diskriminierung", "Diskriminierung"),
                    ("Sexismus", "Sexismus"),
                    ("Rassismus", "Rassismus"),
                    ("Faschismus", "Faschismus"),
                    ("Antisemitismus", "Antisemitismus"),
                    ("Betrug", "Betrug"),
                    ("Spam", "Spam"),
                ],
                default="Hassrede",
                max_length=30,
            ),
        ),
    ]
