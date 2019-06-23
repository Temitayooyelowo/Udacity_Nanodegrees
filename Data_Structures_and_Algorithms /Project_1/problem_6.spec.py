import unittest

from problem_6 import LinkedList, union, intersection

class Problem6(unittest.TestCase):

    def test_union_of_empty_lists(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        union_list = union(linked_list_1,linked_list_2)
        self.assertEqual(union_list.size(), 0)

    def test_intersection_of_empty_lists(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        union_list = intersection(linked_list_1,linked_list_2)
        self.assertEqual(union_list.size(), 0)
    
    def test_valid_union(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        element_1 = [3,2,4,35,6,65,6,4,3,21]
        element_2 = [6,32,4,9,6,1,11,21,1]

        for i in element_1:
            linked_list_1.append(i)

        for i in element_2:
            linked_list_2.append(i)

        expected_result = "3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 32 -> 9 -> 1 -> 11 -> "
        actual_result = str(union(linked_list_1,linked_list_2))

        self.assertEqual(actual_result, expected_result)

    def test_valid_intersection(self):
        linked_list_1 = LinkedList()
        linked_list_2 = LinkedList()

        element_1 = [3,2,4,35,6,65,6,4,3,21]
        element_2 = [6,32,4,9,6,1,11,21,1]

        for i in element_1:
            linked_list_1.append(i)

        for i in element_2:
            linked_list_2.append(i)

        expected_result = "6 -> 4 -> 6 -> 21 -> "
        actual_result = str(intersection(linked_list_1,linked_list_2))
        
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()

# # Test case 1

# linked_list_1 = LinkedList()
# linked_list_2 = LinkedList()

# element_1 = [3,2,4,35,6,65,6,4,3,21]
# element_2 = [6,32,4,9,6,1,11,21,1]

# for i in element_1:
#     linked_list_1.append(i)

# for i in element_2:
#     linked_list_2.append(i)

# print (union(linked_list_1,linked_list_2))
# print (intersection(linked_list_1,linked_list_2))

# # Test case 2

# linked_list_3 = LinkedList()
# linked_list_4 = LinkedList()

# element_1 = [3,2,4,35,6,65,6,4,3,23]
# element_2 = [1,7,8,9,11,21,1]

# for i in element_1:
#     linked_list_3.append(i)

# for i in element_2:
#     linked_list_4.append(i)

# print("\n")
# print (union(linked_list_3,linked_list_4))
# print (intersection(linked_list_3,linked_list_4))