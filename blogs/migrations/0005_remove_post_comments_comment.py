# Generated by Django 4.0.5 on 2023-02-28 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_post_comments_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.post')),
            ],
        ),
    ]