from golem import actions


description = 'verify_element_attribute action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.verify_element_attribute('#input-one', 'class', 'form-control')
