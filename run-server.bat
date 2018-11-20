::export FLASK_APP=gnucash_portfolio_webui/app
@echo off

set FLASK_ENV=development
::pushd gnucash_portfolio_webui
::flask run
::popd

gnucash_portfolio_webui\app.py