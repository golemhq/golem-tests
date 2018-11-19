
description = 'Verify the user cannot log in with incorrect password'

pages = ['login']

def test(data):
    navigate(data.env.url)
    send_keys(login.username_input, 'admin')
    send_keys(login.password_input, 'incorrect password')
    click(login.login_button)
    take_screenshot('Verify the correct error message is shown')
    assert_element_text(login.error_list, 'Username and password do not match')
