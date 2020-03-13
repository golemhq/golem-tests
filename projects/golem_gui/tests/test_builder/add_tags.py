from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder


description = 'Verify the user can add tags to a test'


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.test.create_access_random_test('test')


def test(data):
    tag1 = 'foo'
    tag2 = 'bar'
    # add one tag
    test_builder.add_tag(tag1)
    test_builder.save_test()
    actions.refresh_page()
    test_builder.assert_tags([tag1])
    # add two tags
    test_builder.add_tag(tag2)
    test_builder.save_test()
    actions.refresh_page()
    test_builder.assert_tags([tag1, tag2])
