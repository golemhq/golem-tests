from projects.golem_gui.pages import common
from projects.golem_gui.pages.users import create_user


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    create_user.navigate_to_page()


def test(data):
    create_user.assert_project_suggestion_list()
