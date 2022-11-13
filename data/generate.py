from rich.console import Console
from rich.table import Table
from faker import Faker
from faker.providers import BaseProvider
import datetime
import random

console = Console()
fake = Faker()


class SchedulingProvider(BaseProvider):
    def channel(self):
        channels = ['online', 'phone', 'store']

        return random.choice(channels)

    def status(self):
        status = ['show', 'noshow', 'cancelled', 'rescheduled']

        return random.choice(status)


fake.add_provider(SchedulingProvider)

# customer_name - Name of the customer
# scheduled_date - Date of the scheduled appointment
# scheduled_time_start - Time of the scheduled appointment starts
# scheduled_day_of_week - Which day of the week appointment falls into
# weather - Sunny, windy, rainy, snow etc.,
# service_type - Either of the following
#     DEEP_TISSUE - Deep Tissue Massage
#     SWEDISH - Swedish Massage
#     SPORTS - Sports Massage
#     TRIGGER - Trigger Point Massage
#     STRETCH - Stretch Massage
#     PRENATAL - Prenatal Massage
#     COUPLES - Couples Massage
# service_provider - Either of the following
#     Albert
#     Aries
#     Cindy
#     Delores
#     Joel
#     Sam
#     Sandra
#     Xerez
# booking_date - Date of booking the appointment
# booking_time - Time of booking the appointment

table = Table(title="Relax Spa - Appointments Scheduled 2018/2019")

table.add_column("Customer Name", justify="left", style="cyan")
table.add_column("Scheduled Date", style="magenta")
table.add_column("Scheduled Time", style="magenta")
table.add_column("Scheduled Day of Week", style="magenta")
table.add_column("Weather", style="cyan")
table.add_column("Service Type", style="cyan")
table.add_column("Service Provider", style="cyan")
table.add_column("Booking Date", style="cyan")
table.add_column("Booking Time", style="cyan")
table.add_column("Status", style="cyan")
table.add_column("Channel", style="cyan")

for _ in range(10):
    customer_name = fake.name()
    scheduled_date = fake.date_between_dates(date_start=datetime.datetime(2018, 1, 1),
                                             date_end=datetime.datetime(2019, 1, 31))
    scheduled_time_start = ''
    scheduled_day_of_the_week = ''
    weather = ''
    service_type = ''
    service_provider = ''
    booking_date = ''
    booking_time = ''
    status = fake.status()
    channel = fake.channel()

    table.add_row(
        customer_name,
        scheduled_date.strftime("%m/%d/%Y"),
        scheduled_time_start,
        scheduled_day_of_the_week,
        weather,
        service_type,
        service_provider,
        booking_date,
        booking_time,
        status,
        channel
    )

console.print(table)
