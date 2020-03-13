from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the application displays a toast message when saving a test'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.test.create_access_random_test('test')


def test(data):
    test_builder.add_action('click')
    actions.click(test_builder.save_button)
    common.assert_toast_message_is_displayed('Test '+data.test_name+' saved')
