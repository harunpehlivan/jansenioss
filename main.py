# A quick rundown on dictionaries.
# First, I have a simple dictionary with 2 keys
# and each key has a value associated to it.
# Second, I have a nested dictionary ( dict of dict)
#
# In both cases, I use dictionary methods .keys(), .values(), and .items() to access the various dictionary elements.
#  
print('''
******************************      
*     Simple Dictionary      *
******************************     
      ''')

full_name = {'first_name': 'Jansenio', 'last_name': 'Amado'}
print('Entire dictionary:',full_name)

# accessing the keys...
keys = [k for k in full_name.keys()]
print('\nkeys:',keys)

# accessing the values...
values = [v for v in full_name.values()]
print('\nvalues:', values)

# accessing both keys and values...
key_val = [(k, v) for (k, v) in full_name.items()]
print('\nKey-value pairs:', key_val)

# printing the full name as a string ...
print('\nFull name:',(' ').join(values))

# printing the first name ...
print('\nFirst name:',(' ').join(values)[:8])

# printing the last name...
print('\nLast name:',(' ').join(values)[-5:]);print()

print('''
**********************************************************      
*      Dictionary of dictionary (nested dictionaries)    *
**********************************************************     
      ''')

name_dict = {'first_name':{'Jansenio':'compassion, creativity, generosity, loyalty, love'},\
             'last_name':{'Amado':'seriousness, thought, intuition, intent, wisdom'}}
    
print('>> Entire dictionary:', name_dict); print()
#print(name_dict.keys())


# To print the keys of the outer dictionary...
outer_keys = []
for k in name_dict.keys():
    outer_keys.append(k)
print('>> Outer keys:', outer_keys); print() 
# It will print a list with "First" and "Last".
       

# To print the keys of the inner dictionary...
def rec_keys(dictionary):
    inner_keys = []
    for (key,value) in dictionary.items():
        if isinstance(value, dict):
            inner_keys.extend(rec_keys(value))
        else:
            inner_keys.append(key)
    return inner_keys
# It will print a list with "Jansenio" and "Amado".
print('>> Inner keys:', rec_keys(name_dict))

# To print the values of the outer dictionary...
outer_values = []
for k in name_dict.values():
    outer_values.append(k)
# It will print a list with 2 dictionaries.  
print('\n>> Outer values:', outer_values); print() 

# To print the values of the inner dictionary...
def rec_keys(dictionary):
    inner_values = []
    for (key,value) in dictionary.items():
        if isinstance(value, dict):
            inner_values.extend(rec_keys(value))
        else:
            inner_values.append(value)
    return inner_values
#print('Inner values:', rec_keys(name_dict)[0],rec_keys(name_dict)[1])
print('>> Values for Jansenio:', list(rec_keys(name_dict)[0].split(", ")))
print('\n>> Values for Amado:', list(rec_keys(name_dict)[1].split(", ")))
