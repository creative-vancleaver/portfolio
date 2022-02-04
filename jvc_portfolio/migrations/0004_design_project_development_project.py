# Generated by Django 4.0.1 on 2022-02-03 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jvc_portfolio', '0003_rename_developement_development'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='design_projects', to='jvc_portfolio.project'),
        ),
        migrations.AddField(
            model_name='development',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='development_projects', to='jvc_portfolio.project'),
        ),
    ]
