__author__ = 'Krish'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    if first is None or second is None: return False
    word1 = list(first.lower())
    word2 = list(second.lower())
    for c in word1:
        if c not in word2: return False
        word2.remove(c)
    return True

    pass


# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert True == are_anagrams("wowwie","ewwwio")
    assert False == are_anagrams(None,None)
    assert False == are_anagrams(None,"none")
    assert True == are_anagrams("Anna Madrigal","a man and a girl")
    assert True == are_anagrams("Tom Marvolo Riddle","I am Lord Voldemort")
    assert False == are_anagrams("Tom Marvelo Riddle","I am Lord Voldemort")


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)
