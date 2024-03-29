# Generated by Django 2.2.2 on 2019-06-20 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_chunk_upload.models
import django_chunk_upload.settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyChunkUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_id', models.CharField(default=django_chunk_upload.models.generate_upload_id, editable=False, max_length=32, unique=True)),
                ('file', models.FileField(max_length=255, upload_to=django_chunk_upload.settings.default_upload_to)),
                ('filename', models.CharField(max_length=255)),
                ('offset', models.BigIntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Uploading'), (2, 'Complete')], default=1)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chunk_uploads', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
