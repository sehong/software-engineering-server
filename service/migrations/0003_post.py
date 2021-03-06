# Generated by Django 2.2.12 on 2020-09-30 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20200929_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateField(auto_now=True, verbose_name='작성일')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': '게시물',
                'verbose_name_plural': '게시물',
            },
        ),
    ]
