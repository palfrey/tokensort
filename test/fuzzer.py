import random
import sys

random.seed()

for x in range(500):
	for y in range(10):
		sys.stdout.write(chr(random.randint(ord('a'), ord('z'))))
	print '\n',
