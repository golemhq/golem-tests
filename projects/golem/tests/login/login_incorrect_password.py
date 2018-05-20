
description = 'Verify the user cannot log in with incorrect password'

pages = ['login']

def test(data):
    navigate(data.env.url)
    send_keys(login.username_input, 'admin')
    send_keys(login.password_input, 'incorect password')
    click(login.login_button)
    capture('Verify the correct error message is shown')
    verify_text_in_element(login.error_list, 'Username and password do not match')
