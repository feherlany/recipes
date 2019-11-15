# Generated by Django 2.2.7 on 2019-11-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='sync',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='storage',
            name='method',
            field=models.CharField(choices=[('DB', 'Dropbox'), ('DAV', 'WebDAV')], default='DB', max_length=128),
        ),
    ]