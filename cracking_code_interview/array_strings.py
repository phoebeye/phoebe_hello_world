import sys


# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structure? 


'''
	Approach 1 => use a hash table that stores all the unique characters, and if there is a collision exit with a status false 

	Approach 2 => sort the string and iterate through the sorted string and see if there are repeated characters 

	Appraoch 3 => do a search algorithm that compares all the characters together 


	Assumption: 
		If the string is null, return false 
'''
def main(argv):

	test_case_1='aaaaa'
	test_case_2='abcde'
	test_case_3='1234567a'
	test_case_4='a1234567a'
	test_case_5='a1234a567a'
	test_case_6=''

	test_case_list=[test_case_1,test_case_2,test_case_3,test_case_4,test_case_5,test_case_6]
	for test_case in test_case_list:
		#print test_case, check_unique_char_hash(test_case)
		#print test_case, check_unique_char_sort(test_case)
		print test_case, check_unique_char_match(test_case)
def check_unique_char_hash(input_string):

	# looking at the answer, you can use an integer list that represents the characters 
	
	# overall algorithm is O(n)
	if not input_string:
		return False
	char_hash={}

	# O(n)
	for input_char in input_string:
		# O(1)
		if input_char in char_hash:
			#print input_char, char_hash
			return False
		else: 
			# O(1)
			char_hash[input_char]=True
	return True
def check_unique_char_sort(input_string):
	# O(nLogn) + O(n) => O(nLogn)
	if not input_string:
		return False
	'''
		sorting best case should be O(nLogn) => Timsort which is a hybrid between merge sort and insertion sort 
		O(nLogn) => https://en.wikipedia.org/wiki/Timsort
		youtube => https://www.youtube.com/watch?v=jVXsjswWo44 


		Adaptive Sort 
			1. Small sized input => binary linear search 
			2. Natural runs identiied via binary insertion sort => if under certain size 
			3. Natural runs merged using "one pair at a time"


		Binary insertion sort is modified binary sort that uses binary search to find the location to be inserted thus reducing each insertion from O(n) to O(logn)
	'''
	sorted_input_string=sorted(input_string)
	temp_char=''
	for input_char in sorted_input_string:
		if not input_char==temp_char:
			temp_char=input_char
		else: 
			return False
	return True
def check_unique_char_match(input_string):
	# O(n^2)
	if not input_string:
		return False
	# O(n)
	for char_index in range(len(input_string)-1):
		# this is an O(n) opeartion 
		if input_string[char_index] in input_string[char_index+1:]:
			return False
	return True
if __name__ == '__main__':
	main(sys.argv)
