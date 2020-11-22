source = open("qa.txt", "r")
book = source.read()

questions = []
options = []
answers = []

opCount = 0
opListCount = 0
content_list = book.split(",")
for i in content_list:
    if "\n" in i:
        questions.append(i.strip())
    elif "\t" in i:
        try:
            if opCount < 3:
                options[opListCount].append(i.strip())
                opCount += 1
        except IndexError:
            options.append([])
            if opCount < 3:
                options[opListCount].append(i.strip())
                opCount += 1
    elif "|" in i:
        answers.append(i.replace("|", "").strip())
        opListCount += 1
        opCount = 0

print(f"Questions {questions}\nOptions {options}\nAnswers {answers}")
source.close()