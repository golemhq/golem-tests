from golem import actions


description = 'Verify that the webdriver.find_all method can be called from another webelement'

def test(data):
    actions.navigate(data.env.url+'elements/')
    browser = actions.get_browser()
    actions.step('Find parent element')
    body = browser.find('body')
    actions.step('Find child element by id')
    inputs = body.find_all(tag_name='input')
    assert len(inputs) == 5

