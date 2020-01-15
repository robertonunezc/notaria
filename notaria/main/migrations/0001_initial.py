# Generated by Django 2.2.7 on 2020-01-11 21:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='NCodigoPostal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=80, unique=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, unique=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_paterno', models.CharField(max_length=80)),
                ('apellido_materno', models.CharField(max_length=80)),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='TipoIdentificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='NMunicipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('activo', models.BooleanField(default=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.NEstado')),
            ],
        ),
        migrations.CreateModel(
            name='NColonia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('activo', models.BooleanField(default=True)),
                ('codigo_postal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.NCodigoPostal')),
            ],
        ),
        migrations.AddField(
            model_name='ncodigopostal',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.NMunicipio'),
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=250)),
                ('numero_ext', models.CharField(max_length=250)),
                ('numero_int', models.CharField(blank=True, max_length=250, null=True)),
                ('colonia', models.CharField(blank=True, max_length=250, null=True)),
                ('active', models.BooleanField(default=True)),
                ('codigo_postal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.NColonia')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DatosBasicos',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Persona')),
                ('titulo', models.IntegerField(choices=[(0, 'Sr'), (1, 'Sra')])),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.IntegerField(choices=[(0, 'MASCULINO'), (1, 'FEMENINO')])),
                ('ciudad_de_origen', models.CharField(max_length=80, unique=True)),
                ('documento_migratorio', models.CharField(max_length=80, unique=True)),
                ('calidad_migratoria', models.CharField(max_length=80, unique=True)),
                ('folio_de_identificacion', models.CharField(max_length=80, unique=True)),
                ('emite_identificacion', models.CharField(max_length=80, unique=True)),
                ('clave_larga_distancia', models.IntegerField(unique=True)),
                ('telefono_casa', models.IntegerField(unique=True)),
                ('telefono_casa_2', models.IntegerField(unique=True)),
                ('extension', models.IntegerField(unique=True)),
                ('celular', models.IntegerField(unique=True)),
                ('celular_2', models.IntegerField(unique=True)),
                ('telefono_oficina', models.IntegerField(unique=True)),
                ('telefono_oficina_2', models.IntegerField(unique=True)),
                ('telefono_nextel', models.IntegerField(unique=True)),
                ('id_nextel', models.IntegerField(unique=True)),
                ('email', models.CharField(max_length=80, unique=True)),
                ('email_2', models.CharField(max_length=80, unique=True)),
                ('email_3', models.CharField(max_length=80, unique=True)),
                ('facebook', models.CharField(max_length=80, unique=True)),
                ('twitter', models.CharField(max_length=80, unique=True)),
                ('web', models.CharField(max_length=80, unique=True)),
                ('estado_civil', models.IntegerField(choices=[(0, 'CASADO'), (1, 'SOLTERO'), (2, 'DIVORCIADO'), (3, 'VIUDO')])),
                ('conyuge_apellido_paterno', models.CharField(max_length=80)),
                ('conyuge_apellido_materno', models.CharField(max_length=80)),
                ('conyuge_nombre', models.CharField(max_length=80)),
                ('fecha_matrimonio', models.DateField()),
                ('registro_civil', models.CharField(max_length=80, unique=True)),
                ('nro_acta', models.CharField(max_length=80, unique=True)),
                ('ocupacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Ocupacion')),
                ('pais_nacimiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='natural', to='main.Pais')),
                ('pais_nacionalidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nacionalidad', to='main.Pais')),
                ('tipo_de_identificacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.TipoIdentificacion')),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('main.persona',),
        ),
    ]
