# Generated by Django 4.2.2 on 2023-07-04 17:51

from django.conf import settings
import django.contrib.sites.managers
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import phonenumber_field.modelfields
import sincehence_core.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=251)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExSite',
            fields=[
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sites.site', verbose_name='site')),
                ('site_description', models.TextField(max_length=500)),
                ('site_meta_tag', models.CharField(max_length=255)),
                ('site_favicon', models.ImageField(upload_to='site_image/')),
                ('site_logo', models.ImageField(upload_to='site_image/')),
                ('trademark', models.ImageField(upload_to='site_image/')),
                ('slogan', models.CharField(default='', max_length=150)),
                ('og_image', models.ImageField(upload_to='site_image/')),
                ('mask_icon', models.FileField(upload_to='site_image/', validators=[django.core.validators.FileExtensionValidator(['svg'])])),
                ('facebook_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('instagram_link', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('location', models.TextField()),
                ('phone', models.CharField(max_length=16)),
            ],
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
        migrations.CreateModel(
            name='OurService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='blog/our_service/', verbose_name='Feature Image')),
                ('body', models.TextField(verbose_name='Body')),
            ],
            options={
                'verbose_name': 'Our Service',
                'verbose_name_plural': 'Our Service',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('is_active', models.BooleanField(default=True)),
                ('add_to_page_menu', models.BooleanField(default=False)),
                ('add_to_header_menu', models.BooleanField(default=False)),
                ('add_to_footer_menu', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('top_banenr', models.ImageField(upload_to='blog/top_banenr/', verbose_name='Top Banner')),
                ('top_tagline', models.CharField(max_length=40)),
                ('body', models.TextField(verbose_name='Body')),
                ('meta_description', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('unpublished', 'UnPublished')], default='published', max_length=20)),
                ('consent_required', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='sincehence_core.page', verbose_name='Parent')),
                ('sites', models.ManyToManyField(db_index=True, related_name='%(app_label)s_%(class)s_sites', to='sites.site')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
                'ordering': ['-created_at'],
            },
            bases=(models.Model, sincehence_core.mixins.SaveFromAdminMixin),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('is_active', models.BooleanField(default=True)),
                ('add_to_page_menu', models.BooleanField(default=False)),
                ('add_to_header_menu', models.BooleanField(default=False)),
                ('add_to_footer_menu', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('icon', models.CharField(default='<i class="fa-solid fa-calendar-check"></i>', help_text='HTML Fontawesoome icon', max_length=250, verbose_name='FA Icon')),
                ('description', models.TextField()),
                ('add_to_cat_menu', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='sincehence_core.category', verbose_name='Parent')),
                ('sites', models.ManyToManyField(db_index=True, related_name='%(app_label)s_%(class)s_sites', to='sites.site')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-created_at'],
            },
            bases=(models.Model, sincehence_core.mixins.SaveFromAdminMixin),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('add_to_page_menu', models.BooleanField(default=False)),
                ('add_to_header_menu', models.BooleanField(default=False)),
                ('add_to_footer_menu', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('feature', models.ImageField(upload_to='blog/feature_image/', verbose_name='Feature Image')),
                ('body', models.TextField(verbose_name='Body')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('unpublished', 'UnPublished')], max_length=20)),
                ('categories', models.ManyToManyField(blank=True, db_index=True, related_name='blogs_category', to='sincehence_core.category', verbose_name='Categories')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL)),
                ('sites', models.ManyToManyField(db_index=True, related_name='%(app_label)s_%(class)s_sites', to='sites.site')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ['-created_at'],
            },
            bases=(models.Model, sincehence_core.mixins.SaveFromAdminMixin),
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('action_type', models.CharField(choices=[('view', 'View'), ('like', 'Like')], db_index=True, default='view', max_length=4)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
