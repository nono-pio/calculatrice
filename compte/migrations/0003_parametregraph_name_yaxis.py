# Generated by Django 4.1.1 on 2022-10-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0002_parametregraph_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametregraph',
            name='name_yaxis',
            field=models.CharField(max_length=50, null=True),
        ),
    ]