def print_rangoli(size):
  generate_strings(reversed(range(97, 97+size)), size)
  generate_strings(range(98, 97+size), size)
  
def generate_strings(rng, size):
  dash = lambda x: x+'-'
  for start in rng:
    alph = []
    for char in range(start, 97+size):
      alph.append(chr(char))
    string = '{0}{1}'.format(''.join(map(dash, reversed(alph))), \
		''.join(map(dash,alph)).lstrip(chr(start)+'-')).rstrip('-').center(size*4-3, '-')
    del alph
    print(string)

print_rangoli(9)