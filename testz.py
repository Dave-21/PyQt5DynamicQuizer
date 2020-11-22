source = open("qa.txt", "r")
book = source.read()

questions = []
options = []
answers = []
word = str
wrdCounter = 0
for i in book:
    word = str(word) + i
    if "?" in word:
        questions.append(word.strip())
        word = ""
    elif "\t" in word:
        if wrdCounter <= 3:
            options.append(word.strip())
            wrdCounter += 1
        else:
            options.append([word.strip()])
            wrdCounter = 0
        word = ""
    elif "\n" in word:
        answers.append(word.strip())
        word = ""
    elif "":
        pass
print(options)
