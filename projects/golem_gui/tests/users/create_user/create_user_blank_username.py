from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import create_user


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    create_user.navigate_to_page()


def test(data):
    actions.send_keys(create_user.password, '123456')
    actions.click(create_user.create_user_button)
    common.assert_toast_message_is_displayed('Username cannot be blank')
