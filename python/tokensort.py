import re, sys
from types import *

tokeniser = re.compile("(?:[A-Za-z]+)|(?:-?[0-9]+(?:\.[0-9]+)?)")

pairs = {}

for line in sys.stdin:
	if len(line.strip()) == 0:
		continue
	tokens = tokeniser.findall(line)
	fixedTokens = []
	for t in tokens:
		if t.isalpha():
			fixedTokens.append(t.lower())
		elif t[0].isdigit() or t[0] == '-':
			fixedTokens.append(float(t))
		else:
			print "other", t
	
	key = tuple(fixedTokens)
	if key not in pairs:
		pairs[key] = []

	pairs[key].append(line.rstrip("\n"))

def tokenSort(first, second):
	for i in range(min(len(first), len(second))):
		f = first[i]
		s = second[i]
		if type(f) is StringType:
			if type(s) is FloatType:
				return 1
			else:
				ret = cmp(f, s)
				if ret != 0:
					return ret
		else: # type(f) must be float
			if type(s) is FloatType:
				ret = cmp(f, s)
				if ret != 0:
					return ret
			else:
				return -1
	if len(first) == len(second):
		return 0
	elif len(first) < len(second):
		return -1
	else:
		return 1

keys = sorted(pairs.keys(), cmp = tokenSort)

for k in keys:
	#print k,
	for l in sorted(pairs[k]):
		print l
