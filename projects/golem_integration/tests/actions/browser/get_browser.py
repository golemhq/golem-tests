from golem import actions
from golem import execution


description = 'Verify get_browser action'

def test(data):
    actions.navigate(data.env.url)
    assert actions.get_browser() == execution.browser
