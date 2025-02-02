# Generated by Django 1.11.20 on 2019-08-19 11:33


import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0018_set_ixf_ixp_import_enabled"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="ixlan",
            managers=[
                ("handleref", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name="ixlanixfmemberimportlogentry",
            name="action",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="ixlanixfmemberimportlogentry",
            name="reason",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="commandlinetool",
            name="tool",
            field=models.CharField(
                choices=[
                    (b"pdb_renumber_lans", "Renumber IP Space"),
                    (b"pdb_fac_merge", "Merge Facilities"),
                    (b"pdb_fac_merge_undo", "Merge Facilities: UNDO"),
                    (b"pdb_undelete", "Restore Object(s)"),
                    (b"pdb_ixf_ixp_member_import", "IX-F Import"),
                ],
                help_text="name of the tool",
                max_length=255,
            ),
        ),
    ]
