from golem import actions

description = 'Verify submit_form action'

def test(data):
    # submit from form element
    actions.navigate(data.env.url + 'form-basic/')
    actions.submit_form('#form1')
    actions.verify_title('Basic Form Result')
    # submit from child element
    actions.navigate(data.env.url + 'form-basic/')
    actions.submit_form('#name')
    actions.verify_title('Basic Form Result')

