from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import create_user


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    create_user.navigate_to_page()


def test(data):
    new_username = actions.random_str()
    actions.send_keys(create_user.username, new_username)
    actions.click(create_user.create_user_button)
    common.assert_toast_message_is_displayed('Password cannot be blank')
