
description = 'Verify the user cannot log in if username value is missing'

pages = ['login']

def test(data):
    navigate(data.env.url)
    send_keys(login.password_input, 'admin')
    click(login.login_button)
    capture('Verify the correct error message is shown')
    verify_element_text(login.error_list, 'Username is required')
