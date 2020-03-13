from projects.golem_gui.pages.users.reset_password_prompt import send_reset_password_prompt as reset_password


reset_password_button = ('css', 'button#resetPassword', 'Reset Password button')


def send_reset_password_prompt(new_password):
    reset_password(new_password)
