# Relax Spa - Scheduled Appointments

This is a synthetic data generation tool for a fictitious business called **Relax Spa** which offers massage services to its customers.

```
customer_name - Name of the customer
scheduled_date - Date of the scheduled appointment
scheduled_time_start - Time of the scheduled appointment starts
scheduled_time_end - Time of the scheduled appointment starts
scheduled_day_of_week - Which day of the week appointment falls into
weather - Sunny, windy, rainy, snow etc.,
service_type - Either of the following
    DEEP_TISSUE - Deep Tissue Massage
    SWEDISH - Swedish Massage
    SPORTS - Sports Massage
    TRIGGER - Trigger Point Massage
    STRETCH - Stretch Massage
    PRENATAL - Prenatal Massage
    COUPLES - Couples Massage
service_provider - Either of the following
    Albert
    Aries
    Cindy
    Delores
    Joel
    Sam
    Sandra
    Xerez
booking_date - Date of booking the appointment
booking_time - Time of booking the appointment
status - Either of the following
    Fulfilled
    NoShow
    Cancelled
channel - Either of the following
    Online
    Phone
    Store
```

## Assumptions

- Business is open during the following hours 
   * Mon - Sat 9am - 9pm
   * Sun 10am - 8pm
- All appointments are estimated to be 1 hour long 
- All these appointments occurred between 1st January 2018 to 31st December 2019 (Before COVID-19 pandemic)
- This institution is located in Pleasanton, CA (appropriate weather data is used)

## Generation 

We use python's [Faker](https://github.com/joke2k/faker) to generate the synthetic data. Install this dependency as shown below

`pip3 install Faker`

Please run the python script as shown below

`python3 `

## Future Enhancements and Opportunities

- Multiple locations for the business
- Add-On Services, that can potentially extend the service timings
- At present varying time intervals for service types are not supported. 
- Limiting service providers to specific service types
