::export FLASK_APP=gnucash_portfolio_webui/app
@echo off

set FLASK_ENV=development
cd gnucash_portfolio_webui
flask run
