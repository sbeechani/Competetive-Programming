import unittest


def find_rotation_point(words):

    # Find the rotation point in the list
    mini = 0
    l = len(words)
    maxi = l-1
    while(maxi>=mini):
        mid = (mini+maxi)/2
        if(words[mid-1]>words[mid]):
            if(mid+1 <l):
                if(words[mid]<words[mid+1]):
                    return mid
            else:
                return mid
        elif(words[mid-1]>words[mid] and words[mid]>words[mid+1]):
            maxi = mid-1
        else:
            mini = mid+1

    return -1

# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)
