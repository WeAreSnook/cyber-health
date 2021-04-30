# Generated by Django 3.1.7 on 2021-04-30 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0004_load_intial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('domain_name', models.CharField(max_length=253)),
                ('organisation_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.organisationregion')),
                ('organisation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.organisationtype')),
            ],
        ),
    ]
