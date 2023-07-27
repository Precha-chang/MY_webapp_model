# Generated by Django 4.2.2 on 2023-07-27 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.IntegerField()),
                ('prefix', models.IntegerField(choices=[(1, 'นาย'), (2, 'นางสาว'), (3, 'นาง')], default=1)),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
    ]
