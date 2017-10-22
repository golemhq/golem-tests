
description = ('Verify that the application gives the correct error '
               'message when the user logs in with invalid credentials')

pages = ['header',
         'my_account']

def test(data):
    navigate('http://store.demoqa.com/')
    click(header.my_account)
    send_keys(my_account.username, 'my_username')
    send_keys(my_account.password, 'some_password')
    click(my_account.login_button)
    verify_text_in_element(my_account.error_message, 'ERROR: Invalid login credentials.')
    capture('Error message')
