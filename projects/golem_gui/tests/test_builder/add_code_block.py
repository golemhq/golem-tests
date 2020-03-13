from golem import actions

from projects.golem_gui.pages import common
from projects.golem_gui.pages import index
from projects.golem_gui.pages import api
from projects.golem_gui.pages import test_builder
from projects.golem_gui.pages import test_builder_code


description = 'Verify the user can add an action to a test and save it successfully'

tags = ['smoke']


def setup(data):
    common.access_golem(data.env.url, data.env.admin)
    index.create_access_project('test')
    api.test.create_access_random_test('test')


def test(data):
    test_builder.add_action('code_block')
    step = test_builder.get_step(0)
    assert step.step_type == 'code-block'
    step.set_code_value('if(True):\n    print("True")')
    assert step.get_code_value() == 'if(True):\n    print("True")'
    test_builder.save_test()
    actions.click(test_builder.code_button)
    expected = ('def test(data):\n'
                '    if(True):\n'
                '        print("True")\n')
    assert expected in test_builder_code.get_value()
