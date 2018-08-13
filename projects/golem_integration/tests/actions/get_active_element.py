from golem import actions


description = 'Verify get_active_element action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    # default active element is body tag
    assert actions.get_active_element().tag_name == 'body'
    actions.click('#button-one')
    # active element is clicked button
    assert actions.get_active_element().tag_name == 'button'
    assert actions.get_active_element().get_attribute('id') == 'button-one'
