###include the code to make migrations with data for this dropdowns

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='first_dropdown',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mymodel',
            name='second_dropdown',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RunPython(
            code='''
import random

for i in range(10):
    myapp.models.MyModel.objects.create(
        first_dropdown='option%d' % i,
        second_dropdown='option%d' % random.randint(1, 3),
    )
''',
        ),
    ]
