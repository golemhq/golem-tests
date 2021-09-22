from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_builder_common


description = 'Verify the user can add json data to the test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')


def test_add_then_remove_internal_datasource(data):
    api.test.create_access_test(data.project)
    test_builder_common.add_internal_datasource()
    test_builder_common.set_value_to_internal_data_editor('data = [{"foo": "bar"}]')
    test_builder.save_test()
    actions.refresh_page()
    assert test_builder_common.get_value_of_internal_data_editor() == ('data = [\n'
                                                                       '    {\n'
                                                                       '        \'foo\': \'bar\',\n'
                                                                       '    },\n'
                                                                       ']\n')
    # remove internal datasource
    test_builder_common.remove_internal_datasource()
    test_builder.save_test()
    actions.refresh_page()
    assert not test_builder_common.internal_datasource_is_present()


def test_add_internal_datasource_with_invalid_python(data):
    api.test.create_access_test(data.project)
    test_builder_common.add_internal_datasource()
    test_builder_common.set_value_to_internal_data_editor('data = [{"foo": "bar"}')
    test_builder.save_test()
    common.assert_toast_message_is_displayed_and_contains('SyntaxError: unexpected EOF')
