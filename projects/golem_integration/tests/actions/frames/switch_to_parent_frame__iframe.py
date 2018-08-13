from golem import actions


description = 'Verify switch_to_parent_frame action on iframes'

def test(data):
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
