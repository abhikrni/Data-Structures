#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

"""
Thanks to Kevin Meyers for the idea of mapping digits and alphabets
"""
BASE_ENCODE = string.digits + string.ascii_lowercase
BASE_DECODE = {digit: val for val, digit in enumerate(BASE_ENCODE)}


def decode(digits, base):
	"""
	Time complexity: O(n)
	Decode given digits in given base to number in base 10.
	digits: str -- string representation of number (in given base)
	base: int -- base of given number
	return: int -- integer representation of number (in base 10)"""
	# Handle up to base 36 [0-9a-z]
	assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
	nums = []
	for index, digit in enumerate(digits[::-1]):
		nums.append((base ** index) * BASE_DECODE[digit])
	return sum(nums)


"""Thanks to Audi Blades for help with encode function"""
def encode(number, base):
	"""
	Time complexity: O(n)
	Encode given number in base 10 to digits in given base.
	number: int -- integer representation of number (in base 10)
	base: int -- base to convert to
	return: str -- string representation of number (in given base)"""
	# Handle up to base 36 [0-9a-z]
	assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
	# Handle unsigned numbers only for now
	assert number >= 0, 'number is negative: {}'.format(number)
	
	encoded_number = []
	
	while number > 0:
		number, remainder = divmod(number, base)
		if remainder >= 10:
			encoded_number.append(str(BASE_ENCODE[remainder]))
		else:
			encoded_number.append(str(remainder))
	return "".join(encoded_number[::-1])


def convert(digits, base1, base2):
	
	"""
	Time complexity: O(n)
	Convert given digits in base1 to digits in base2.
	digits: str -- string representation of number (in base1)
	base1: int -- base of given number
	base2: int -- base to convert to
	return: str -- string representation of number (in base2)"""
	# Handle up to base 36 [0-9a-z]
	assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
	assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
	
	return encode(decode(digits, base1), base2)


def main():
	"""Read command-line arguments and convert given digits between bases."""
	import sys
	args = sys.argv[1:]  # Ignore script file name
	if len(args) == 3:
		digits = args[0]
		base1 = int(args[1])
		base2 = int(args[2])
		# Convert given digits between bases
		result = convert(digits, base1, base2)
		print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
	else:
		print('Usage: {} digits base1 base2'.format(sys.argv[0]))
		print('Converts digits from base1 to base2')


if __name__ == '__main__':
	main()
