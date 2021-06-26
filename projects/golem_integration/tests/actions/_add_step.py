from golem import actions
from golem import execution

from projects.golem_integration.pages import golem_logger


description = 'Verify _add_step adds a step to execution.steps'


def test(data):
    actions._add_step('step message')
    assert 'INFO step message' in golem_logger.get_last_info_log_line()
    assert execution.steps == [{'message': 'step message', 'screenshot': None, 'error': None}]
