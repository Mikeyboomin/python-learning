# example output
# Active Admins: boomin, diana
# Active Editors: alice
# Inactive Users: bob, charlie

users = [
    ("boomin", "admin", True),
    ("alice", "editor", True),
    ("bob", "viewer", False),
    ("charlie", "editor", False),
    ("diana", "admin", True),
]


def user_access_checker(users):
    active_admins = []
    active_editors = []
    inactive_users = []

    for user in users:
        name, role, status = user
        if role == 'admin' and status:
            active_admins.append(name)
        elif role == 'editor' and status:
            active_editors.append(name)
        elif role == 'editor' or role == 'viewer' and not status:
            inactive_users.append(name)

    return f"Active Admins: {", ".join(active_admins)}\nActive Editors: {", ".join(active_editors)}\nInactive users: {", ".join(inactive_users)}"        

print(user_access_checker(users))
