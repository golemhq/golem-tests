from golem import actions
from golem import execution


description = 'Verify close_browser action'

def test(data):
    actions.navigate(data.env.url)
    actions.close_browser()
    assert execution.browser == None
