# Generated by Django 2.1.7 on 2019-03-12 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_add_dogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book category (e.g. Javascript)', max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-date_added']},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='author',
            name='category',
            field=models.ManyToManyField(to='core.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(help_text='Select a category for this book', related_name='categories', to='core.Category'),
        ),
    ]