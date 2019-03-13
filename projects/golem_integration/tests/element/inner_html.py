from golem import actions
from golem.browser import element


description = 'Verify webelement.inner_html method'

def test(data):
    actions.navigate(data.env.url+'elements/')
    logo = element('a.logo')
    assert logo.inner_html == '<strong>Web Playground</strong>'
