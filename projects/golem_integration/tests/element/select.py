from golem import actions
from golem.webdriver.extended_webelement import Select


description = 'Verify webelement.select property'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    element = actions.get_browser().find('#select-1')
    select = element.select
    assert type(select) is Select
