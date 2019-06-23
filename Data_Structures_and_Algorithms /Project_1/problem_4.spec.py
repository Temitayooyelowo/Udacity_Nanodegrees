import unittest

from problem_4 import Group, is_user_in_group

class Problem4(unittest.TestCase):

    def test_empty_user_in_group(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        child.add_group(sub_child)
        parent.add_group(child)

        empty_user = ""

        self.assertFalse(is_user_in_group(empty_user, parent))

    def test_is_false_user_in_group(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        child.add_group(sub_child)
        parent.add_group(child)

        false_user = "false_user"

        self.assertFalse(is_user_in_group(false_user, parent))
    
    def test_is_valid_user_in_child_group(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        child_user = "child_user"
        child.add_user(child_user)

        child.add_group(sub_child)
        parent.add_group(child)

        self.assertTrue(is_user_in_group(child_user, parent))

    def test_is_valid_user_in_subchild_group(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")

        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)

        child.add_group(sub_child)
        parent.add_group(child)

        self.assertTrue(is_user_in_group(sub_child_user, parent))


if __name__ == '__main__':
    unittest.main()