# Generated by Django 3.1.3 on 2021-03-10 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('icon', models.FileField(upload_to='static/icons')),
                ('cover', models.FileField(upload_to='static/icons')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
