def check_user_access(user: dict):
    if user['is_active'] is False:
        return 'Access denied: Inactive account'
    elif user['age'] < 18:
        return 'Access denied: Underage'
    elif user['age'] >= 18 and user['is_active'] is True:
        curr_role = user['roles'][0]
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
editor_dict = {'username': 'doom_guy', 'age': 18, 'is_active': True, 'roles': ['editor']}

# underage acc
underage_acc = {'username': 'little_kid', 'age': 17, 'is_active': True, 'roles': ['admin']}

# just a user
simple_man = {'username': 'simple_man', 'age': 18, 'is_active': True, 'roles': ['user']}


print(check_user_access(user_dict))
print(check_user_access(inactive_user))
print(check_user_access(editor_dict))
print(check_user_access(underage_acc))
print(check_user_access(simple_man))


