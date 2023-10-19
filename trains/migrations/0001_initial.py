# Generated by Django 4.1.12 on 2023-10-12 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Days",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("choice", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Station",
            fields=[
                (
                    "station_code",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("station_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="TrainClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("class_code", models.CharField(max_length=3)),
                ("coach_prefix", models.CharField(max_length=3)),
                ("class_name", models.CharField(max_length=50)),
                ("seat_per_coach", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="TrainDetails",
            fields=[
                (
                    "train_code",
                    models.CharField(max_length=5, primary_key=True, serialize=False),
                ),
                ("distance", models.IntegerField()),
                ("train_name", models.CharField(max_length=50)),
                ("start_time", models.TimeField()),
                ("duration", models.DurationField()),
                ("end_time", models.TimeField()),
                ("classes", models.ManyToManyField(to="trains.trainclass")),
            ],
        ),
        migrations.CreateModel(
            name="ViaDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("relative_pos", models.IntegerField()),
                (
                    "for_train",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="trains.traindetails",
                    ),
                ),
                (
                    "station_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="trains.station"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="traindetails",
            name="route",
            field=models.ManyToManyField(
                through="trains.ViaDetails", to="trains.station"
            ),
        ),
        migrations.AddField(
            model_name="traindetails",
            name="running_days",
            field=models.ManyToManyField(to="trains.days"),
        ),
        migrations.CreateModel(
            name="TicketReservation",
            fields=[
                (
                    "PNR_no",
                    models.CharField(max_length=18, primary_key=True, serialize=False),
                ),
                ("reservation_time", models.DateTimeField(auto_now=True)),
                ("from_date", models.DateField(auto_now=True)),
                ("total_fare", models.IntegerField()),
                ("passenger_name", models.CharField(max_length=30)),
                ("passenger_age", models.IntegerField()),
                (
                    "passenger_sex",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("O", "Other"),
                            ("P", "Prefer Not to Say"),
                        ],
                        max_length=20,
                    ),
                ),
                ("ticket_status", models.CharField(max_length=5)),
                ("ticket_seat_no", models.IntegerField(blank=True, null=True)),
                (
                    "from_station",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="from_station_r",
                        to="trains.station",
                    ),
                ),
                (
                    "to_station",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="to_station_r",
                        to="trains.station",
                    ),
                ),
                (
                    "train",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="trains.traindetails",
                    ),
                ),
                (
                    "train_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="trains.trainclass",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SeatAvailability",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fare_per_passenger", models.IntegerField()),
                ("total_seats", models.IntegerField()),
                ("booked_seats", models.IntegerField(default=0)),
                ("waiting_list", models.IntegerField(default=0)),
                (
                    "classes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="train_class_seat",
                        to="trains.trainclass",
                    ),
                ),
                (
                    "train",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="trains.traindetails",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Fare",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fare_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "station",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="trains.station"
                    ),
                ),
                (
                    "train",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trains.traindetails",
                    ),
                ),
                (
                    "train_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trains.trainclass",
                    ),
                ),
            ],
        ),
    ]