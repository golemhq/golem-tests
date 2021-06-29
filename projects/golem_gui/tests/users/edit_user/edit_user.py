from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import users
from projects.golem_gui.pages.users import create_user
from projects.golem_gui.pages import utils


def setup(data):
    actions.store('username', actions.random_str())
    utils.create_user(data.username, '123456')
    common.access_golem(data.env.url, data.env.admin)
    common.navigate_menu('Users')
    users.wait_for_table_to_load()


def test(data):
    users.click_edit_button(data.username)
    new_username = actions.random_str()
    new_email = 'test@test.com'
    actions.clear_element(create_user.username)
    actions.send_keys(create_user.username, new_username)
    actions.clear_element(create_user.email)
    actions.send_keys(create_user.email, new_email)
    actions.click(create_user.update_user_button)
    users.wait_for_table_to_load()
    assert not users.user_in_table(data.username)
    assert users.user_in_table(new_username)
    users.assert_user_values(new_username, email=new_email)
