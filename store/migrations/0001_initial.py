# Generated by Django 3.2.5 on 2023-06-21 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(default=0)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
                ('Specialization', models.CharField(max_length=200)),
                ('Experience', models.IntegerField()),
                ('Image', models.ImageField(blank=True, null=True, upload_to='doctors')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOrdered', models.DateField(auto_now=True, null=True)),
                ('complete', models.BooleanField(default=False)),
                ('paymentDone', models.BooleanField(default=False)),
                ('transactionId', models.CharField(blank=True, max_length=12, null=True)),
                ('total_price', models.FloatField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pathological_Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TestName', models.CharField(max_length=100)),
                ('Desc', models.TextField()),
                ('Image', models.ImageField(blank=True, null=True, upload_to='shops')),
                ('SampleType', models.CharField(max_length=100)),
                ('FastingRequirement', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDetailsDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], max_length=10, null=True)),
                ('ServiceID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serviceDetailsDays', to='store.service')),
            ],
            options={
                'unique_together': {('ServiceID', 'Day')},
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=190, unique=True)),
                ('Address', models.CharField(max_length=300)),
                ('Status', models.CharField(choices=[('E', 'ENABLE'), ('D', 'DISABLE')], default='E', max_length=2)),
                ('Interior_image', models.ImageField(blank=True, null=True, upload_to='shops')),
                ('OffDay', models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], default='Sunday', max_length=10)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='shops')),
                ('Opening_time', models.TimeField(blank=True, null=True)),
                ('Closing_time', models.TimeField(blank=True, null=True)),
                ('Shop_url', models.URLField(default='www.watduwant.com/show_details')),
                ('Shop_owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FlatName', models.CharField(max_length=200)),
                ('StreetName', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=10)),
                ('AddressType', models.CharField(max_length=200)),
                ('MobileNumber', models.CharField(max_length=15)),
                ('AppointmentDate', models.DateField()),
                ('AppointmentTimeSlot', models.TimeField()),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shippingAddress', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='Clinic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='store.shop'),
        ),
        migrations.AddField(
            model_name='service',
            name='Doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='store.doctor'),
        ),
        migrations.CreateModel(
            name='Phlebotomist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('Shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Phlebotomists', to='store.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Pathological_Test_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.IntegerField()),
                ('ReportDeliveryTime', models.TimeField()),
                ('Shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PathologicalTestServices', to='store.shop')),
                ('Tests', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PathologicalTestServices', to='store.pathological_test')),
            ],
        ),
        migrations.CreateModel(
            name='OrderService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateAdded', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('0', 'Not assigned'), ('1', 'Assigned'), ('2', 'delivered'), ('3', 'Not Delivered'), ('4', 'Collected'), ('5', 'Not Collected')], default='0', max_length=1)),
                ('collected_date', models.DateField(null=True)),
                ('report', models.FileField(blank=True, null=True, upload_to='reports')),
                ('Cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderServices', to='store.cart')),
                ('Order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderServices', to='store.order')),
                ('PathologicalTestService', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderServices', to='store.pathological_test_service')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDetailsDayTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.TimeField()),
                ('Visit_capacity', models.IntegerField()),
                ('ServiceDetailsDayID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='serviceDetailsDayTimes', to='store.servicedetailsday')),
            ],
            options={
                'unique_together': {('ServiceDetailsDayID', 'Time')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together={('Clinic', 'Doctor')},
        ),
    ]
