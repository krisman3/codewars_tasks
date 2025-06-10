def check_user_access(user: dict):
    if user['is_active'] is False:
        return 'Access denied: Inactive account'
    elif user['age'] < 18:
        return 'Access denied: Underage'
    elif user['age'] >= 18 and user['is_active'] is True:
        curr_role = user['roles']
        if curr_role == 'admin':
            return 'Access granted: Admin'
        elif curr_role == 'editor':
            return 'Access granted: Editor'
    else:
        return f'Access granted: {user['username']}'


# happy path ADMIN
user_dict = {'username': 'Max88verstappen', 'age': 18, 'is_active': True, 'roles': ['admin']}

# inactive account
inactive_user = {'username': 'joro_pochivka', 'age': 18, 'is_active': False, 'roles': ['admin']}

# happy path EDITOR
editor_dict = {'username': 'doom_guy', 'age': 18, 'is_active': True, 'roles': ['admin']}

# underage acc
underage_acc = {'username': 'doom_guy', 'age': 17, 'is_active': True, 'roles': ['admin']}


