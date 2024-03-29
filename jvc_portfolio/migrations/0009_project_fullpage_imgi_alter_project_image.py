# Generated by Django 4.0.2 on 2023-11-20 18:22

from django.db import migrations, models
import jvc_portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('jvc_portfolio', '0008_project_name_alter_project_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='fullpage_imgI',
            field=models.ImageField(blank=True, null=True, upload_to=jvc_portfolio.models.project_path),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=jvc_portfolio.models.project_path),
        ),
    ]
