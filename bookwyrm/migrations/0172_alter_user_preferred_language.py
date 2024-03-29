# Generated by Django 3.2.16 on 2022-12-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0171_alter_user_preferred_timezone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="preferred_language",
            field=models.CharField(
                blank=True,
                choices=[
                    ("en-us", "English"),
                    ("ca-es", "Català (Catalan)"),
                    ("de-de", "Deutsch (German)"),
                    ("es-es", "Español (Spanish)"),
                    ("eu-es", "Euskara (Basque)"),
                    ("gl-es", "Galego (Galician)"),
                    ("it-it", "Italiano (Italian)"),
                    ("fi-fi", "Suomi (Finnish)"),
                    ("fr-fr", "Français (French)"),
                    ("lt-lt", "Lietuvių (Lithuanian)"),
                    ("no-no", "Norsk (Norwegian)"),
                    ("pl-pl", "Polski (Polish)"),
                    ("pt-br", "Português do Brasil (Brazilian Portuguese)"),
                    ("pt-pt", "Português Europeu (European Portuguese)"),
                    ("ro-ro", "Română (Romanian)"),
                    ("sv-se", "Svenska (Swedish)"),
                    ("zh-hans", "简体中文 (Simplified Chinese)"),
                    ("zh-hant", "繁體中文 (Traditional Chinese)"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
