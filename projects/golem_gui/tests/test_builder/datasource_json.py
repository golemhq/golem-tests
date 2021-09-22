from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_builder_common


description = 'Verify the user can add json data to the test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')


def test_add_then_remove_json_datasource(data):
    api.test.create_access_test(data.project)
    test_builder_common.add_json_datasource()
    test_builder_common.set_value_to_json_editor('[{"foo": "bar"}]')
    test_builder.save_test()
    actions.refresh_page()
    assert test_builder_common.get_value_of_json_editor() == '[{"foo": "bar"}]'
    # remove json datasource
    test_builder_common.remove_json_datasource()
    test_builder.save_test()
    actions.refresh_page()
    assert not test_builder_common.json_datasource_is_present()


def test_add_invalid_json(data):
    api.test.create_access_test(data.project)
    test_builder_common.add_json_datasource()
    test_builder_common.set_value_to_json_editor('[{"foo": "bar"]')
    test_builder.save_test()
    common.assert_toast_message_is_displayed_and_contains('json.decoder.JSONDecodeError')
