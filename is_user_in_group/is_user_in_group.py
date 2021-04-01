def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not group:
        return False

    if user == group.get_name():
        return True

    if user in group.get_users():
        return True

    for group in group.get_groups():
        return is_user_in_group(user, group)

    return False
