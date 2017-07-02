import re

words = []
seen = {}

translate_table = [[]]
current_index = 0

with open('backtothefuture_transcript.txt', 'r') as f:
    regex = re.compile('[^a-zA-Z \n]')
    words = regex.sub('', f.read()).lower().split()

for word in words:
    if word not in seen:
        seen[word] = True
        translate_table[current_index].append(word)

        if len(translate_table[current_index]) >= 32:
            translate_table.append([])
            current_index += 1

def translate(word):
    word = list(word)
    translated = []

    for index, char in enumerate(word):
        char_ord = ord(char)
        if char_ord == 32:
            # handle special space case
            char_ord = 26
        else:
            char_ord -= 97

        translated.append(translate_table[index][char_ord])

    return ' '.join(translated)

print translate('the groupon of health but like google')
