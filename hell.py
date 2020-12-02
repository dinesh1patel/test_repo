#str_object[start_pos:end_pos:step]
s1 = "this is my string"
s1_reversed = s1[::-1]
print("sting '{}' reversed is {}".format(s1,s1_reversed))
s1_odds = s1[::2]
print("sting '{}' odds is {}".format(s1,s1_odds))

# Iterate over the string 
for element in s1: 
    print(element, end=' ') #end=' 'puts a space between each character printed
print("\n") 

# Iterate over index 
for element in range(0, len(s1)): 
    print(s1[element])

print("commited")
