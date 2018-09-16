from golem import actions


description = 'verify_element_checked action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_checked('#selected-checkbox')
    try:
        actions.verify_element_checked('#unselected-checkbox')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'element #unselected-checkbox is not checked' in e.args[0]
    actions.verify_element_checked('#exampleRadios1')
    try:
        actions.verify_element_checked('#exampleRadios2')
        assert False, 'Expected Exception'
    except Exception as e:
        assert 'element #exampleRadios2 is not checked' in e.args[0]
