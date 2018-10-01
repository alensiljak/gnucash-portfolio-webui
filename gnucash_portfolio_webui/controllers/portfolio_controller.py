"""
Portfolio
- cash account balances per currency
- portfolio value report
"""
from pydatum import Datum
from datetime import datetime  # , timedelta
from flask import Blueprint, request, render_template

#from gnucash_portfolio.lib import portfoliovalue, datetimeutils
from gnucash_portfolio.bookaggregate import BookAggregate
from gnucash_portfolio.securitiesaggregate import SecuritiesAggregate
from gnucash_portfolio.reports.portfolio_models import PortfolioValueInputModel, PortfolioValueViewModel

portfolio_controller = Blueprint(  # pylint: disable=invalid-name
    'portfolio_controller', __name__, url_prefix='/portfolio')


@portfolio_controller.route('/value', methods=['GET'])
def portfolio_value():
    """ Portfolio Value report """
    from gnucash_portfolio.reports import portfolio_value
    
    # default filter parameters
    #search = PortfolioValueInputModel()
    #model = __get_model_for_portfolio_value(search)

    parameters = PortfolioValueInputModel()
    today = Datum()
    today.today()
    parameters.as_of_date = today.value
    model = portfolio_value.run(parameters)

    return render_template('portfolio.value.html', model=model)


@portfolio_controller.route('/value', methods=['POST'])
def portfolio_value_post():
    """ Accepts the filter parameters and displays the portfolio value report """
    from gnucash_portfolio.reports import portfolio_value

    input_model = __parse_input_model()

    model = portfolio_value.run(input_model)
    return render_template('portfolio.value.html', model=model)


######################
# Private

def __parse_input_model() -> PortfolioValueInputModel:
    """ Parses the search parameters from the request """
    result = PortfolioValueInputModel()

    date_input_str = request.form.get("filter.as_of_date")
    date_input = datetime.strptime(date_input_str, "%Y-%m-%d")
    result.as_of_date = datetime(date_input.year, date_input.month, date_input.day, 23, 59, 59)

    result.stock = request.form.get("security")

    return result
