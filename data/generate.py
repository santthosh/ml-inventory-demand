from rich.console import Console
from rich.table import Table
from faker import Faker
from faker.providers import BaseProvider
import datetime
from datetime import timedelta
import random
import csv

console = Console()
fake = Faker()


class SchedulingProvider(BaseProvider):
    def channel(self):
        channels = ['online', 'phone', 'store']

        return random.choice(channels)

    def status(self):
        status = ['show', 'noshow', 'cancelled', 'rescheduled']

        return random.choice(status)

    def service_type(self):
        service_type = ['DEEP_TISSUE', 'SWEDISH', 'SPORTS', 'TRIGGER', 'STRETCH', 'PRENATAL', 'COUPLES']

        return random.choice(service_type)

    def service_provider(self):
        service_provider = ['Albert', 'Aries', 'Cindy', 'Delores', 'Joel', 'Sam', 'Sandra', 'Xerez']

        return random.choice(service_provider)

    def scheduled_time_start(self):
        scheduled_time_start = ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

        return f'{random.choice(scheduled_time_start)}:00:00'

    def sunday_scheduled_time_start(self):
        sunday_scheduled_time_start = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19']

        return f'{random.choice(sunday_scheduled_time_start)}:00:00'


fake.add_provider(SchedulingProvider)

table = Table(title="Relax Spa - Appointments Scheduled 2018/2019")

table.add_column("Customer Name", justify="left", style="cyan")
table.add_column("Scheduled Date", style="magenta")
table.add_column("Scheduled Time", style="magenta")
table.add_column("Scheduled Day of Week", style="magenta")
table.add_column("Service Type", style="cyan")
table.add_column("Service Provider", style="cyan")
table.add_column("Booking Date", style="magenta")
table.add_column("Booking Time", style="magenta")
table.add_column("Status", style="cyan")
table.add_column("Channel", style="cyan")

i = 0

with open('./reservations.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['customer_name', 'scheduled_date', 'scheduled_time', 'scheduled_day_of_week', 'service_type',
                     'service_provider', 'booking_date', 'booking_time', 'status', 'channel'])
    # Please refer to README.md on why we are generating 52,480 rows
    for _ in range(52480):
        customer_name = fake.name()
        scheduled_date = fake.date_between_dates(date_start=datetime.datetime(2018, 1, 1),
                                                 date_end=datetime.datetime(2019, 1, 31))

        scheduled_day_of_the_week = scheduled_date.strftime('%A')

        scheduled_time_start = fake.scheduled_time_start()
        if scheduled_day_of_the_week == 'Sunday':
            scheduled_time_start = fake.sunday_scheduled_time_start()

        weather = ''
        service_type = fake.service_type()
        service_provider = fake.service_provider()
        # Make sure its booked upto 60 days before the scheduled appointment
        booking_date = scheduled_date - timedelta(days=fake.pyint(min_value=1, max_value=60))
        booking_time = fake.time_object().strftime('%H:%M:%S')
        status = fake.status()
        channel = fake.channel()

        i += 1

        # Print only a small list of rows
        if i < 25:
            table.add_row(
                customer_name,
                scheduled_date.strftime("%m/%d/%Y"),
                scheduled_time_start,
                scheduled_day_of_the_week,
                service_type,
                service_provider,
                booking_date.strftime("%m/%d/%Y"),
                booking_time,
                status,
                channel
            )

        if i % 50 == 0:
            console.print(f'[bold green]{i}[/bold green] records generated')

        writer.writerow([customer_name, scheduled_date.strftime("%m/%d/%Y"), scheduled_time_start,
                         scheduled_day_of_the_week, service_type, service_provider,
                         booking_date.strftime("%m/%d/%Y"), booking_time, status, channel])

console.print(table)
console.print(f'A total of [bold blue]{i}[/bold blue] records generated')