
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wbchina', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
