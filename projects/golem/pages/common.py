import time

from golem.browser import elements


def verify_toast_message_is_displayed(toast_message):
    for _ in range(6):
        toasts = elements('div.toast>.toast-message')
        if len(toasts):
            for toast in toasts:
                if toast.text == toast_message:
                    return
        time.sleep(0.5)
    assert False, 'Toast with message "{}" was not found'.format(toast_message)