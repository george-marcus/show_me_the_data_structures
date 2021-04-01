from group import Group
from is_user_in_group import is_user_in_group


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user, None))  # False
print(is_user_in_group(sub_child_user, parent))  # True
print(is_user_in_group(sub_child_user, sub_child))  # True
print(is_user_in_group("child", child))  # True
print(is_user_in_group("", child))  # False
print(is_user_in_group("sub_child_user", parent))  # True
print(is_user_in_group(sub_child_user, child))  # True
