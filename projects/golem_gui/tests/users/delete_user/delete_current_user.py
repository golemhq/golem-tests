from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import users


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    common.navigate_menu('Users')
    users.wait_for_table_to_load()


def test(data):
    users.click_delete_button(data.env.admin.username)
    common.assert_toast_message_is_displayed('Cannot delete current user')
