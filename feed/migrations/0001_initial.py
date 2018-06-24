# Generated by Django 2.0.5 on 2018-06-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(help_text='What is the topic of the post?', max_length=50)),
                ('body', models.CharField(help_text='Enter body of post', max_length=150)),
                ('feel', models.CharField(blank=True, choices=[('h', 'happy'), ('s', 'sad'), ('e', 'excited'), ('a', 'angry')], default='h', help_text='what are you feeling?', max_length=1)),
                ('date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
