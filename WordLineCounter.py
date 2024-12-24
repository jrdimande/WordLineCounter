
text = 'text'

with open(text) as file_object:
    lines = file_object.readlines()

search = input('Search a word: ').lower()

num_words = 0
num_search = 0

for line in lines:
    current_line = line.split()
    aux = []


    for word in current_line:
        aux.append(word.lower())

    for word in aux:
        if word == search:
            num_search +=
            
print(f'Number of words: {len(aux)}')

if num_search > 0:
    print(f'The word {search} appears {num_search} times')
else:
    print('word not founded')





