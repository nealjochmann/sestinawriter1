# Methods that write a stanza to a text file


def writeStanzaToFile(stanza, file):
	for l in stanza:
		file.write(l+'\n')

def composeEnvoiLines(envoi):
	envoiLines = [];
	for i in [0,2,4]:
		envoiLine = envoi[i]+" "+envoi[i+1]
		envoiLines.append(envoiLine)
	return envoiLines

def writeEnvoiToFile(envoi, file):
	envoiLines = composeEnvoiLines(envoi)
	writeStanzaToFile(envoiLines, file)

def writeSestinaToFile(sestina):
	with open("sestina.txt", "w") as sf:
		for s in sestina[0:6]:
			writeStanzaToFile(s, sf)
			sf.write('\n')
		writeEnvoiToFile(sestina[6], sf)
	sf.close()