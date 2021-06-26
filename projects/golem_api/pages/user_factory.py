from golem import actions

from projects.golem_api.pages import users, project as project_page


def user_exists(username):
    response = users.get_user(username)
    return response.json() is not None


def create_random_user(project_permissions=None):
    username = actions.random_str()
    password = actions.random_str()
    permissions = [{'project': pp[0], 'permission': pp[1]} for pp in project_permissions]
    users.create_new_user(username, password, project_permissions=permissions)
    return {'username': username, 'password': password}


def create_user_if(username):
    """Create a user if it does not exist.
    username should be `project__permission`
    eg: 'project_name__read-only'
    """
    password = '123'
    split_ = username.split('__')
    if len(split_) != 2:
        raise Exception('Expected username to be "project__permission"')
    if not user_exists(username):
        project = split_[0]
        permission = split_[1]
        if permission not in ['super-user', 'admin', 'standard', 'read-only', 'reports-only']:
            raise Exception('Invalid permission: {}'.format(permission))
        project_page.create_project_if(project)
        permissions = [{'project': project, 'permission': permission}]
        users.create_new_user(username, password, project_permissions=permissions)
    return {'username': username, 'password': password}
