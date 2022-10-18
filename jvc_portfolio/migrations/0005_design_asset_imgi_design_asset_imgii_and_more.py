# Generated by Django 4.0.2 on 2022-09-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jvc_portfolio', '0004_rename_image_design_banner_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='asset_imgI',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
        migrations.AddField(
            model_name='design',
            name='asset_imgII',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
        migrations.AddField(
            model_name='design',
            name='asset_imgIII',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
        migrations.AddField(
            model_name='design',
            name='banner_txt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='design',
            name='conclusion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='design',
            name='fullpage_imgI',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
        migrations.AddField(
            model_name='design',
            name='fullpage_imgII',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
        migrations.AddField(
            model_name='design',
            name='fullpage_imgIII',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
        migrations.AddField(
            model_name='design',
            name='mockup_imgI',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
        migrations.AddField(
            model_name='design',
            name='mockup_imgII',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
        migrations.AddField(
            model_name='design',
            name='mockup_imgIII',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
        migrations.AddField(
            model_name='design',
            name='process',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='design',
            name='process_cont',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='design',
            name='responsive_imgI',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
        migrations.AddField(
            model_name='design',
            name='responsive_imgII',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
        migrations.AddField(
            model_name='design',
            name='responsive_imgIII',
            field=models.ImageField(blank=True, null=True, upload_to='images/des/'),
        ),
    ]