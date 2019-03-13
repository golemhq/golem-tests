from golem import actions
from golem.browser import element


description = 'Verify webelement.outer_html method'

def test(data):
    actions.navigate(data.env.url+'elements/')
    logo = element('a.logo')
    assert logo.outer_html == '<a class="logo" href="/"><strong>Web Playground</strong></a>'
