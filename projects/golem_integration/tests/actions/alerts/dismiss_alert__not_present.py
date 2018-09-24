from golem import actions
from selenium.common.exceptions import NoAlertPresentException


from projects.golem_integration.utils import expected_exception

description = 'Verify dismiss_alert action when alert is not present'

def test(data):
    actions.navigate(data.env.url+'alert/')
    actions.dismiss_alert(ignore_not_present=True)
    with expected_exception(NoAlertPresentException):
        actions.dismiss_alert()
