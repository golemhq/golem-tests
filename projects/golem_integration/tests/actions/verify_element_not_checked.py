from golem import actions


description = 'verify_element_not_checked action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_not_checked('#unselected-checkbox')
    try:
        actions.verify_element_not_checked('#selected-checkbox')
    except Exception as e:
        assert 'element #selected-checkbox is checked' in e.args[0]
    actions.verify_element_not_checked('#exampleRadios2')
    try:
        actions.verify_element_not_checked('#exampleRadios1')
    except Exception as e:
        assert 'element #exampleRadios1 is checked' in e.args[0]
