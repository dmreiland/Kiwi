# Generated by Django 2.1.2 on 2018-10-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('testplans', '0002_squashed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='TestPlanTag',
            name='tag',
            field=models.ForeignKey(on_delete=models.deletion.CASCADE, to='management.Tag'),
        ),
        migrations.AlterField(
            model_name='TestPlan',
            name='tag',
            field=models.ManyToManyField(related_name='plan',
                                         through='testplans.TestPlanTag',
                                         to='management.Tag'),
        ),
        migrations.RemoveField(
            model_name='testplanemailsettings',
            name='notify_on_plan_delete',
        ),
        migrations.AlterField(
            model_name='testplantext',
            name='checksum',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterModelOptions(
            name='testplantext',
            options={'ordering': ['plan', '-pk']},
        ),
        migrations.AlterUniqueTogether(
            name='testplantext',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='testplantext',
            name='plan_text_version',
        ),
        migrations.RemoveField(
            model_name='testplantext',
            name='checksum',
        ),
        migrations.AlterModelTable(
            name='envplanmap',
            table=None,
        ),
        migrations.AlterModelTable(
            name='plantype',
            table=None,
        ),
        migrations.AlterModelTable(
            name='testplan',
            table=None,
        ),
        migrations.AlterModelTable(
            name='testplantag',
            table=None,
        ),
        migrations.AlterModelTable(
            name='testplantext',
            table=None,
        ),
    ]
