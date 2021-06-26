from golem import actions

from projects.golem_integration.pages import golem_steps


description = 'Verify switch_to_parent_frame action'


def test_switch_to_parent_frame(data):
    # switch to frame
    actions.navigate(data.env.url+'frames/')
    # first frame in frameset is considered main content
    actions.assert_page_contains_text('Top')
    actions.switch_to_frame('frame-bottom')
    # switch to nested frame
    actions.switch_to_frame('frame-bottom-left')
    actions.assert_page_contains_text('Bottom Left')
    actions.assert_page_not_contains_text('Top')
    actions.assert_page_not_contains_text('Bottom Right')
    # switch to default content
    actions.switch_to_parent_frame()
    golem_steps.assert_last_step_message('Switch to parent frame')
    actions.switch_to_parent_frame()
    actions.assert_page_contains_text('Top')
    actions.assert_page_not_contains_text('Bottom Right')
    actions.assert_page_not_contains_text('Bottom Left')


def test_switch_to_parent_frame_iframe(data):
    actions.navigate(data.env.url+'iframes/')
    # switch to iframe
    actions.switch_to_frame('iframe-bottom')
    actions.verify_page_contains_text('IFrame Bottom')
    actions.verify_page_not_contains_text('Iframes')
    # switch to nested iframe
    actions.switch_to_frame('iframe-bottom-left')
    actions.verify_page_contains_text('IFrame Bottom Left')
    actions.verify_page_not_contains_text('Iframe Bottom')
    # switch back to parent iframe
    actions.switch_to_parent_frame()
    actions.verify_page_contains_text('IFrame Bottom')
    actions.verify_page_not_contains_text('Iframe Bottom Left')
    actions.verify_page_not_contains_text('IFrames')
    # switch back to main content
    actions.switch_to_parent_frame()
    actions.verify_page_contains_text('IFrames')
    actions.verify_page_not_contains_text('IFrame Bottom')
    actions.verify_page_not_contains_text('Iframe Bottom Left')
