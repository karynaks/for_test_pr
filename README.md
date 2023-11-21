# Currency Server

Currency Server is a simple REST API server that performs basic calculations
on foreign exchange rates using [the Narodowy Bank Polski's public APIs](http://api.nbp.pl/).
The server is written in Python 3 and Django.

## Installation

1. Clone the repository to your local machine.
```commandline
git clone https://github.com/username/currency-server.git
```
2. Change into the currency-server directory.
```commandline
cd currency-server
```
3. Install the required packages.
```commandline
pip install -r requirements.txt
```
4. Migrate the database.
```commandline
python manage.py migrate
```

## Usage
To start the server, run the following command:
```text
python manage.py runserver <port>
```
You can use any available port instead of `<port>` (for example 8888). 
The server will start listening on the specified port, and you can then use the API.

### API Endpoints
The Currency Server provides the following API endpoints:

1) Average exchange rate by the currency code and the date (formatted `YYYY-MM-DD`)
```link
http://localhost:<port>/exchanges/one-day-rate/<code>/<date>
```
Example (answer should be `5.2086`): 
```link
http://localhost:8888/exchanges/one-day-rate/GBP/2023-04-21
```

2) Max and min average  exchange rate by the currency code and the number of last quotations `N` (N <= 255)

```link
http://localhost:<port>/exchanges/maximum-and-minimum/<code>/<N>
```
Example: 
```link
http://localhost:8888/exchanges/maximum-and-minimum/GBP/23
```

3) The major difference between the buy and ask rate by the currency code and the number of last quotations `N` (N <= 255)

```link
http://localhost:<port>/buy-and-sell-rates/<code>/<N>
```
Example: 
```link
http://localhost:8888/buy-and-sell-rates/GBP/23
```

## Tests
The Currency Server has unit tests that cover the calculation module, the nbp_api module and the views module.

* To run the calculation module tests, use the following command:
```commandline
pytest currency_server/tests/test_calculations.py
```

* To run the nbp_api module tests, use the following command:
```commandline
pytest currency_server/tests/test_nbp_api.py
```

* To run the views module tests, use the following command:
```commandline
python manage.py test
```

## License
This project is licensed under the terms of the MIT license.
