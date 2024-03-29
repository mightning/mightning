'''
opens the .cnf file and analyses it
'''

def del_p_line():
    
    #this deletes the line that starts with 'p'
    
    global filtered_content
    
    file_path = 'mara.cnf'

    # Read the content of the file, skip lines starting with 'p', and write back to the file
    with open(file_path, 'r', encoding='utf8') as file:
        content = file.read()

    # Filter out lines starting with 'p'
    filtered_content = '\n'.join(line for line in content.split('\n') if not line.startswith('p'))

# processes the lines
def process_line(line):
    # Split the input line into a list of numbers
    numbers_list = line.split()

    # Convert the list of strings to a list of integers
    numbers = [int(num) for num in numbers_list]

    return numbers

del_p_line()

# Split the input into lines
lines = filtered_content.split(' 0')

# Process each line
result = [process_line(line) for line in lines]

#get rid of the last empty list
result.pop()


#working variables: list and set
just_one_list = []
for x in result:
    just_one_list.extend(x)
    
just_one_set = set(just_one_list)


#RESULTS:

# Does the number of clausules and variables match the figures in the first line?
print(f'Pocet klauzul je: {len(result)}')
print(f'Pocet promennych je: {int(len(just_one_set)/2)}')

# Is there a variable that has only positive or only negative value?
without_opposite = [x for x in just_one_set if -x not in just_one_set]

# Do all the clausules contain at least two variables?
less_than_two = [x for x in result if len(x) < 2]

if not less_than_two:
    print('Vsechny klauzuly maji alespon dva literaly.')

else:
    print(f'Tyto klauzuly maji mene nez dva literaly: {less_than_two}')

# Does any clausule contain a certain variable more than once?

test_result = result

for x in test_result:
    for a in range(len(x)):
        x[a] = abs(x[a])

big_dupes = []
for b in test_result:
    seen = set()
    dupes = [y for y in b if y in seen or seen.add(y)]
    big_dupes.append(dupes) 

big_dupes = [x for x in big_dupes if x !=[]]

if big_dupes == []:
    print('V zadne klauzule se jedna promenna nevyskytuje vicekrat.')
else:
    print(f'Tyto promenne se vyskytuji vicekrat: {big_dupes}')
