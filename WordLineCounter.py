
text = 'text'

with open(text) as file_object:
    lines = file_object.readlines()

search = input('Search a word: ').lower()

num_words = 0
num_search = 0

aux = []

for line in lines:
    current_line = line.split()

    for word in current_line:
        aux.append(word.lower())

    for word in aux:
        if word == search:
            num_search += 1

print(f'Number of words: {len(aux)}')

if num_search > 0:
    print(f'The word {search} appears {int(num_search / 2)} times')
else:
    print('word not founded')





