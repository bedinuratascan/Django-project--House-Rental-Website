# Generated by Django 3.0.3 on 2020-03-08 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('rent', models.IntegerField()),
                ('detail', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('area', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
                ('buildingFloor', models.IntegerField()),
                ('floorLocation', models.IntegerField()),
                ('furnished', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('balconied', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('heating', models.CharField(max_length=255)),
                ('withintheSite', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('fromWho', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.Category')),
            ],
        ),
    ]