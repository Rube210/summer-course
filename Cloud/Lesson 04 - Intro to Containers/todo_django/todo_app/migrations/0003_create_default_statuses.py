from django.db import migrations


def create_statuses(apps, schema_editor):
    Status = apps.get_model('todo_app', 'Status')
    default_statuses = [
        ("Open", "00FF00"),
        ("In Progress", "FFFF00"),
        ("Done", "FF0000"),
    ]
    for name, color in default_statuses:
        Status.objects.get_or_create(statusName=name, defaults={"statusColor": color})


def remove_statuses(apps, schema_editor):
    Status = apps.get_model('todo_app', 'Status')
    Status.objects.filter(statusName__in=["Open", "In Progress", "Done"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("todo_app", "0002_remove_task_user"),
    ]

    operations = [
        migrations.RunPython(create_statuses, remove_statuses),
    ]
