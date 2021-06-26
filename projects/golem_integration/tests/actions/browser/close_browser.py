from golem import actions
from golem import execution


description = 'Verify close_browser action'


def test_close_browser(data):
    actions.navigate(data.env.url)
    actions.close_browser()
    assert execution.browser is None
