from golem import actions


description = 'Verify webdriver.navigate method'

def test(data):
    browser = actions.get_browser()
    browser.navigate(data.env.url)
    assert browser.current_url == data.env.url
    assert browser.title == 'Web Playground'
