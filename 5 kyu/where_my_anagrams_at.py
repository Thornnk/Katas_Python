# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:
#
# 'abba' & 'baab' == true
#
# 'abba' & 'bbaa' == true
#
# 'abba' & 'abbba' == false
#
# 'abba' & 'abca' == false
#
# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array if there are none. For example:
#
# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
#
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
#
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []


def anagrams(word, words):
	def dict_me(w):
		dict_word = {}
		for c in w:
			if c in dict_word.keys(): dict_word[c] += 1
			else: dict_word[c] = 1
		return dict_word
	return [anag for anag in words if dict_me(anag) == dict_me(word)]


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])) # ['aabb', 'bbaa']
