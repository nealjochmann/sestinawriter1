testStanza = ['first','second','third','fourth','fifth','sixth']

def generateNextStanza(stanza):
	newStanza = [];
	for i in [5,0,4,1,3,2]:
		newStanza.append(stanza[i])
	return newStanza

def testGenerateNextStanza():
	print(testStanza)
	print(generateNextStanza(testStanza)) #expect 6,1,5,2,4,3
	print(generateNextStanza(generateNextStanza(testStanza))) #expect 3,6,4,1,2,5

# testGenerateNextStanza()