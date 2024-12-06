# exchange_project

Django REST API - yfinance API

 Open terminal in project folder and start django project.

    python manage.py runserver

To add some api's data you need use these command in the python console in your opened terminal.

    python manage.py shell
    from currency.utils import update_currencies, update_exchange_rate
    update_currencies()
    update_exchange_rate("EUR", "USD")

These commands add data from yfinance api to local database. 
Now you can search this address in your brownser

> http://127.0.0.1:8000/currency/

> http://127.0.0.1:8000/currency/EUR/USD/




