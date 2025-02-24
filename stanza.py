testStanza = ['first','second','third','fourth','fifth','sixth']


# given an array of the endwords for one sestina stanza,
# return an array of the endwords for the next stanza.
def generateNextStanza(stanza):
	newStanza = [];
	for i in [5,0,4,1,3,2]:
		newStanza.append(stanza[i])
	return newStanza

# given an array of endwords and an index,
# return an array of the endwords for the stanza at that index.
def getStanzaAtIndex(endwords, index):
	stanzaToReturn = endwords
	while index > 0:
		stanzaToReturn = generateNextStanza(stanzaToReturn)
		index -= 1
	return stanzaToReturn


### TESTS ###
def test_generateNextStanza():
	print(testStanza)
	print("Next stanza:");
	print(generateNextStanza(testStanza)) #expect 6,1,5,2,4,3
	print("Next stanza after that:")
	print(generateNextStanza(generateNextStanza(testStanza))) #expect 3,6,4,1,2,5

def test_getStanzaAtIndex():
	print(testStanza)
	print("stanza 2:")
	print(getStanzaAtIndex(testStanza, 1))#expect 6,1,5,2,4,3
	print("stanza 3:")
	print(getStanzaAtIndex(testStanza, 2))#expect 3,6,4,1,2,5
	print("stanza 4:")
	print(getStanzaAtIndex(testStanza, 3))#expect 5,3,2,6,1,4

def tests_run():
	print("Testing generateNextStanza:")
	test_generateNextStanza()
	print("\nTesting getStanzaAtIndex:")
	test_getStanzaAtIndex()

# Uncomment this line to run tests:
#tests_run()