from golem.browser import element


create_user_link = ('css', 'a#createUser', 'Create User link')
user_table = ('id', 'userTable', 'User table')


def user_in_table(username):
    rows = element(user_table).find_all('tbody>tr')
    for row in rows:
        tds = row.find_all('td')
        if tds[0].text == username:
            return row
    return False


def assert_user_in_table(username):
    if not user_in_table(username):
        raise AssertionError('{} was not found in users table'.format(username))


def click_delete_button(username):
    row = user_in_table(username)
    row.find('button.delete-user-button').click()


def click_edit_button(username):
    row = user_in_table(username)
    row.find('a.edit-user-button').click()


def assert_user_values(username, email=None, superuser=None, projects=None):
    row = user_in_table(username)
    tds = row.find_all('td')
    if email is not None:
        actual_email = tds[1].text
        msg = 'Expected email to be {} but was {}'.format(email, actual_email)
        assert actual_email == email, msg


def wait_for_table_to_load(timeout=10):
    loading_icon = element('#usersTableLoadingIconContainer', wait_displayed=False)
    loading_icon.wait_not_displayed(timeout)
