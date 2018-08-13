from golem import actions


description = 'Verify webdriver.get_window_titles method'

def test(data):
    tabs_url = data.env.url + 'tabs/'
    tab_url = data.env.url + 'tab/'
    actions.navigate(tabs_url)
    actions.click('#openTab')
    actions.wait_for_window_present_by_title('Tab')
    window_urls = actions.get_browser().get_window_urls()
    assert window_urls == [tabs_url, tab_url]