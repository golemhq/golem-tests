from golem import actions


description = 'Verify get_element_text action'

def test(data):
    actions.navigate(data.env.url + 'elements/')
    # text of input
    actions.send_keys('#input-one', 'foo')
    assert actions.get_element_text('#input-one') == 'foo'
    # text of text area
    actions.send_keys('#textarea-1', 'bar')
    assert actions.get_element_text('#textarea-1') == 'bar'
    # text of h1
    assert actions.get_element_text('h1') == 'Commmon Elements'
