# Generated by Django 4.0.1 on 2022-02-04 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jvc_portfolio', '0004_design_project_development_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='name',
            field=models.CharField(choices=[('PS', 'Photoshop'), ('AI', 'Illustrator'), ('Lightroom', 'Lightroom')], max_length=200),
        ),
    ]
