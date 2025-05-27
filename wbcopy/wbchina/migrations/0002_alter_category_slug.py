
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wbchina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
