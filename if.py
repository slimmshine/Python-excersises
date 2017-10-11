x = int(raw_input("Enter integer: "))
if x < 0:
	print "Negative"
elif x == 0:
	print 'Zero'
else:
	print 'Positive'


list = [1,2,3,4,5,6,7,8,9]
for i in list:
	print i, "-pow2-", i**2

words = ['cat', 'window', 'defenestrate']
for w in words[:]:
	if len(w) > 6:
		words.insert(0,w)
		print words

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print i, a[i]
