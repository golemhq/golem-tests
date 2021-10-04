from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the user can add test hooks'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    api.project.using_project('test_builder')
    api.test.create_access_test(data.project)


def test_add_before_test_hook(data):
    test_builder.add_test_hook('before_test')
    test_builder.add_step_to_test('before_test', 'click')
    test_builder.save_test()
    actions.refresh_page()
    assert test_builder.get_steps('before_test')[0].action_name == 'click'


def test_add_before_each_hook(data):
    test_builder.add_test_hook('before_each')
    test_builder.add_step_to_test('before_each', 'log')
    test_builder.save_test()
    actions.refresh_page()
    assert test_builder.get_steps('before_each')[0].action_name == 'log'


def test_add_after_each_hook(data):
    test_builder.add_test_hook('after_each')
    test_builder.add_step_to_test('after_each', 'add_cookie')
    test_builder.save_test_and_refresh_page()
    assert test_builder.get_steps('after_each')[0].action_name == 'add_cookie'


def test_add_after_test_hook(data):
    test_builder.add_test_hook('after_test')
    test_builder.add_step_to_test('after_test', 'double_click')
    test_builder.save_test_and_refresh_page()
    assert test_builder.get_steps('after_test')[0].action_name == 'double_click'
