# Traffic Control Web Application

This is a simple traffic control web application that provides RESTful APIs for managing cars, car owners, and tolls. The project is implemented using the Django web framework with RESTful API design.

## API Endpoints

The following API endpoints are available:

- `GET /red-blue-cars`: Returns a list of all red and blue cars.
- `POST /register-owner-car`: Creates a new car owner.
- `GET /owners/older-than-70`: Returns a list of all owners who are older than 70 years.
- `GET /old-owner`: Returns a list of all big cars that have been on roads with a length less than 20 meters.
- `GET /tolls-of-car`: Returns the tolls paid by a specific owner or car; depends on what user enters.
- `GET /location-lists`: Returns the location list of all small cars that are about 600 meters far from the first toll.
- `GET /name-and-national-code`: Returns the name and national code of owners who have had toll orders by their toll payment.

## Technology Stack

The project is implemented using the Django web framework with RESTful API design. No external libraries or databases are used, and the data is stored in memory.

## Installation and Usage

1. Clone the repository:
   ```
   git clone https://github.com/MostafaMoradi7/Cherry_Test_Example.git
   ```
2. Run the server:
   ```
   python manage.py runserver
   ```
3. The API endpoints are now accessible at `http://localhost:8000/`.

## Contributors

This project was implemented as an internship project for Ofogh Company. If you have any suggestions or improvements, feel free to create a pull request or open an issue.
