# Generated by Django 3.1.3 on 2021-03-18 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_ad_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='location',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='phone',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image1',
            field=models.FileField(blank=True, null=True, upload_to='static/ads'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image2',
            field=models.FileField(blank=True, null=True, upload_to='static/ads'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.subcategory'),
        ),
    ]
