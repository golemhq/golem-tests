from golem import actions


description = 'Verify get_window_handle and get_window_handles actions'

def test(data):
    actions.navigate(data.env.url+'tabs/')
    actions.click('#openTab')
    actions.wait_for_window_present_by_title('Tab', timeout=5)
    current_window_handle = actions.get_window_handle()
    all_handles = actions.get_window_handles()
    assert len(all_handles) == 2
    assert current_window_handle in all_handles