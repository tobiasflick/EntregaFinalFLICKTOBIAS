# Generated by Django 4.0.4 on 2022-05-30 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0010_alter_registropromos_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shopping.usuarios')),
            ],
        ),
    ]