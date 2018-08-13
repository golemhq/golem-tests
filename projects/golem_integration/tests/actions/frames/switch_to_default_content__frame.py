from golem import actions


description = 'Verify switch_to_default_content action on framesets and frames'

def test(data):
    # switch to frame
    actions.navigate(data.env.url+'frames/')
    # first frame in frameset is considered main content
    actions.verify_page_contains_text('Top')
    actions.switch_to_frame('frame-bottom')
    # switch to nested frame
    actions.switch_to_frame('frame-bottom-left')
    actions.verify_page_contains_text('Bottom Left')
    actions.verify_page_not_contains_text('Top')
    actions.verify_page_not_contains_text('Bottom Right')
    # switch back to parent frame
    actions.switch_to_parent_frame()
    actions.switch_to_parent_frame()
    actions.verify_page_contains_text('Top')
    actions.verify_page_not_contains_text('Bottom Right')
    actions.verify_page_not_contains_text('Bottom Left')
