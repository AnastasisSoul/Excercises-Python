max_words = ['', '', '', '', ''] 
i = 0
f = open('input_file.txt', 'r')
text = f.read()
words = text.split()
for i in range(len(words)):
    letters_list = list(words[i])
    new_letters_list= ''
    for j in range(len(words[i])):
        letter = letters_list[j]
        if (not(letter.isalpha())):
            continue
        else:
            new_letters_list = new_letters_list + letters_list[j]
    if (new_letters_list.isalpha()):
        words[i] = new_letters_list
    else:
        words[i] = []
print('*****WORDS OF TEXT*****')
for i in range(len(words)):
    print(words[i])
for i in range(len(words)):
    if (len(words[i]) > len(max_words[0])):
        max_words[4] = max_words[3]
        max_words[3] = max_words[2]
        max_words[2] = max_words[1]
        max_words[1] = max_words[0]
        max_words[0] = words[i]
    else:
        if (len(words[i]) > len(max_words[1])):
            max_words[4] = max_words[3]
            max_words[3] = max_words[2]
            max_words[2] = max_words[1]
            max_words[1] = words[i]
        else:
            if (len(words[i]) > len(max_words[2])):
                max_words[4] = max_words[3]
                max_words[3] = max_words[2]
                max_words[2] = words[i]
            else:
                if (len(words[i]) > len(max_words[3])):
                    max_words[4] = max_words[3]
                    max_words[3] = words[i]
                else:
                    if (len(words[i]) > len(max_words[0])):
                        max_words[4] = words[i]
print('*****FIVE LONGER WORDS OF TEXT*****')
for i in range(len(max_words)):
    print(max_words[i])
for i in range(len(max_words)):
    letters_list = list(max_words[i])
    new_letters_list= ''
    for j in range(len(max_words[i])):
        letter = letters_list[j]
        if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y'or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' or letter == 'Y'):
            continue
        else:
            new_letters_list = new_letters_list + letters_list[j]
    max_words[i] = new_letters_list
print('*****FIVE LONGER WORDS OF TEXT WITHOUT VOWELS*****')
for i in range(len(max_words)):
      print(max_words[i])
print('*****REVERSE ORDER*****')
for i in range (len(max_words)):
    start = len(max_words[i])
    end = (start + 1) * (-1)
    print(max_words[i][start:end:-1])
f.close()
