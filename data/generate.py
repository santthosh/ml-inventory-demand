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
    global scheduled_max_per_date

    scheduled_max_per_date = {}

    def scheduled_date(self):
        global scheduled_max_per_date

        weights = [5, 1, 2, 1, 2, 6, 7]
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        found = False

        while not found:
            generated_date = fake.date_between_dates(date_start=datetime.datetime(2018, 1, 1),
                                                     date_end=datetime.datetime(2019, 12, 31))

            generated_day = generated_date.strftime('%A')
            selected_day = random.choices(days, k=1, weights=weights)[0]

            while generated_day != selected_day:
                generated_date += timedelta(days=1)
                generated_day = generated_date.strftime('%A')

            if generated_date in scheduled_max_per_date:
                # Max of 80 hours/day - 8 team members * 10 hours/day (12 hours - 2 hours break)
                if scheduled_max_per_date[generated_date] >= 80:
                    print('.', end="")
                    found = False  # Try another date
                else:
                    scheduled_max_per_date[generated_date] += 1
                    found = True
            else:
                scheduled_max_per_date[generated_date] = 1
                found = True

        return generated_date

    def channel(self):
        weights = [5, 3, 2]
        channels = ['online', 'phone', 'store']

        return random.choices(channels, k=1, weights=weights)[0]

    def status(self):
        weights = [6, 2, 1, 1]
        status = ['show', 'noshow', 'cancelled', 'rescheduled']

        return random.choices(status, k=1, weights=weights)[0]

    def service_type(self):
        weights = [3, 4, 1, 1, 5, 1, 1]
        service_type = ['DEEP_TISSUE', 'SWEDISH', 'SPORTS', 'TRIGGER', 'STRETCH', 'PRENATAL', 'COUPLES']

        return random.choices(service_type, k=1, weights=weights)[0]

    def service_provider(self):
        weights = [1, 2, 2, 2, 1, 3, 4, 1]
        service_provider = ['Albert', 'Aries', 'Cindy', 'Delores', 'Joel', 'Sam', 'Sandra', 'Xerez']

        return random.choices(service_provider, k=1, weights=weights)[0]

    def scheduled_time_start(self):
        weights = [1, 1, 2, 3, 3, 1, 1, 1, 1, 4, 4, 3]
        scheduled_time_start = ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

        return f'{random.choices(scheduled_time_start, k=1, weights=weights)[0]}:00:00'

    def sunday_scheduled_time_start(self):
        weights = [1, 2, 3, 3, 3, 3, 2, 2, 1, 1]
        sunday_scheduled_time_start = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19']

        return f'{random.choices(sunday_scheduled_time_start, k=1, weights=weights)[0]}:00:00'


fake.add_provider(SchedulingProvider)

table = Table(title="Relax Spa - Appointments Scheduled 2018/2019")

table.add_column("Customer Name", justify="left", style="cyan")
table.add_column("Scheduled Date", style="magenta")
table.add_column("Scheduled Day of Week", style="magenta")
table.add_column("Service Type", style="cyan")
table.add_column("Service Provider", style="cyan")
table.add_column("Booking Date", style="magenta")
table.add_column("Status", style="cyan")
table.add_column("Channel", style="cyan")

i = 0

with open('reservations-1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['customer_name', 'scheduled_date', 'scheduled_day_of_week', 'service_type',
                     'service_provider', 'booking_date', 'status', 'channel'])
    # Please refer to README.md on why we are generating 52,480 rows
    for _ in range(52480):
        customer_name = fake.name()
        scheduled_date = fake.scheduled_date()

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

        scheduled_date_time = f'{scheduled_date.strftime("%Y-%m-%d")} {scheduled_time_start}'
        booking_date_time = f'{booking_date.strftime("%Y-%m-%d")} {booking_time}'

        # Print only a small list of rows
        if i < 25:
            table.add_row(
                customer_name,
                scheduled_date_time,
                scheduled_day_of_the_week,
                service_type,
                service_provider,
                booking_date_time,
                status,
                channel
            )

        if i % 50 == 0:
            console.print(f'[bold green]{i}[/bold green] records generated')

        writer.writerow([customer_name, scheduled_date_time,
                         scheduled_day_of_the_week, service_type, service_provider,
                         booking_date_time, status, channel])

console.print(table)
console.print(f'A total of [bold blue]{i}[/bold blue] records generated')
