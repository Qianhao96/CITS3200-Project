# Generated by Django 2.1.1 on 2018-10-22 11:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverSheetFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_data', picklefield.fields.PickledObjectField(blank=True, editable=False, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 10, 22, 11, 30, 58, 661381, tzinfo=utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 10, 22, 11, 30, 58, 661437, tzinfo=utc))),
                ('name', models.CharField(default='coversheetform_#test', max_length=30)),
                ('approved', models.BooleanField(default=False)),
                ('request_lodged', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_general', models.BooleanField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CriteriaTemplateFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_general', models.BooleanField()),
                ('name', models.CharField(max_length=100)),
                ('data', models.TextField(default=' @ @ @ ')),
                ('creator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='Ignore message')),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 10, 22, 11, 30, 58, 662054, tzinfo=utc))),
                ('author', models.CharField(default='admin', max_length=30)),
                ('coversheet', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='animalwellbeing.CoverSheetFormModel')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_Q', models.CharField(default=None, max_length=100)),
                ('Question', models.CharField(default=None, max_length=150)),
                ('Answer', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Researchers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(default='user', max_length=30)),
                ('firstname', models.CharField(default='broken', max_length=30)),
                ('number_of_coversheets', models.IntegerField(default=0)),
                ('email', models.EmailField(default='def@gmail.com', max_length=254)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='coversheetformmodel',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='animalwellbeing.Researchers'),
        ),
    ]