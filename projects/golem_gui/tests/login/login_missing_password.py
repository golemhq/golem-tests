
description = 'Verify the user cannot log in if password value is missing'

pages = ['login']

def test(data):
    navigate(data.env.url)
    send_keys(login.username_input, 'admin')
    click(login.login_button)
    take_screenshot('Verify the correct error message is shown')
    assert_element_text(login.error_list, 'Password is required')
