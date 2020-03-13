from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import users
from projects.golem_gui.pages.users import create_user


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    create_user.navigate_to_page()


def test(data):
    new_username = actions.random_str()
    actions.send_keys(create_user.username, new_username)
    actions.send_keys(create_user.password, '123456')
    actions.click(create_user.create_user_button)
    users.wait_for_table_to_load()
    users.assert_user_in_table(new_username)
