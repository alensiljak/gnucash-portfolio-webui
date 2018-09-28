:: Run the web app
@echo off

::set FLASK_APP=app
::flask run

::start "" http://localhost:5000

:: python app/
:: py gnucash_portfolio_webui/ :: This requires __main__.py
::py gnucash_portfolio_webui:app

:: Run run.py
::set FLASK_APP=gnucash_portfolio_webui/app.py
::flask run

:: To run Flask only:
:: py gnucash_portfolio_webui/app.py

:: To run the server & the client:
py gnucash_portfolio_webui\run.py
