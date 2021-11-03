# For a given nonempty string s find a minimum substring t and the maximum number k, such that the entire string s is equal to t repeated k times. The input string consists of lowercase latin letters. Your function should return a tuple (in Python) (t, k) or an array (in Ruby and JavaScript) [t, k]
#
# Example #1:
#
# for string
#
# s = "ababab"
# the answer is
#
# ("ab", 3)
# Example #2:
#
# for string
#
# s = "abcde"
# the answer is
#
# ("abcde", 1)
# ["abcde", 1]
# because for this string "abcde" the minimum substring t, such that s is t repeated k times, is itself.

def f(s):
    def f(s):
        for i in range(len(s), 0, -1):
            if s.count(s[:i]) > 1: return s[:i], s.count(s[:i])
        return s, 1


print(f('ababab'))
