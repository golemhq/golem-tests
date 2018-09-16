from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'assert_element_present action'

def test(data):
    actions.navigate(data.env.url+'elements/')
    actions.assert_element_text('#link1', 'this is a link to index')
    golem_steps.assert_last_step_message("Assert element #link1 text is 'this is a link to index'")
    try:
        actions.assert_element_text('#link1', 'incorrect text')
    except AssertionError as e:
        expected = ("expected element #link1 text to be 'incorrect text' but "
                    "was 'this is a link to index'")
        assert expected in e.args[0]
