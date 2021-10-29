
# Trash Collector – Django Web Application

## Django based web app which simulates a trash collection service

An application for a business specializing in trash collection.

The application includes a fully-functional customer side that allows users to register as customers and utilize the application to start their service.

Using the application, customers are able to:

- Choose a day of the week to get their regular trash picked up
- Choose a date for an additional, one-time pickup
- Temporarily suspend their service between two chosen dates
- Track their current account balance

## Features

- Utilizes Django Auth Groups
- Adhere to established naming conventions & best practices
- Newly-registered User can complete the registration process and create Employee profile
- Registered employees can:
  - **Edit** employee information to change name and/or zip code
  - Access **index** view which list the current day's customers who meet ALL the following criteria:
    - Customers in employee assigned zip code
    - Pickup day is today’s day of week OR One-time pickup date that falls on today
    - Non-suspended accounts
    - Trash has not yet been picked up today
  - Confirm a pickup via Button/link displayed with each pickup in employee's daily list
  - Charge customers $20 for all confirmed pickups (applied to customer account)
  - Select a day of the week to filter by, and see all customers who gets a weekly pickup on the day selected (One time pickups NOT displayed)
  - Utilize ‘employee_base.html’ parent template that includes a navbar to direct to links for default daily view, profile edit, and any other pages needed
  - Select a customer profile and see their address with a pin on a map (Google Maps API, Google Geocoding API)
  - See all employee's customers on a map for delivery (multiple pins displayed on one map, unique by day)

- Customers can:
  - Make payments on the application via integrated payment API

## Technology

- Bootstrap Content Delivery Network (CDN) on the base.html parent template to stylize templates and front end elements
- Django
- Google Maps API
- Google Places API
- Google Geocoding API
