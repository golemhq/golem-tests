
description = 'Verify that the user can log in to Golem web module'

pages = ['login',
         'index']

def test(data):
    navigate(data.env.url)
    click(login.login_button)
    send_keys(login.username_input, 'admin')
    send_keys(login.password_input, 'admin')
    click(login.login_button)
    capture('Verify the user is logged in')
    verify_element_text(index.title, 'Select a Project')
