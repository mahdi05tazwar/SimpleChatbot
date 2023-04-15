from SentenceMatcher import SentenceMatch
from json import loads
from random import choice
def getResponse(userin):
    datafile = loads(open('data.json', 'r').read())
    data = datafile["data"]
    sentences = []
    for block in data:
        sentences.extend(block["sample"])
    output, accr = SentenceMatch(userin, sentences)
    for block in data:
        if output in block["sample"]:
            response = choice(block["responses"])
            break
    return response
while True:
    userin = input("ENTER: ")
    if userin == "0":
        break
    response = getResponse(userin)
    print(response)
