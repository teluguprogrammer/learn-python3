text = 'this is my first python programming class.'
count = {}
 
for c in text:
    if c in count: # check if c is there in count dictionary or not.
        count[c] =count[c] + 1
    else:
        count[c] = 1

print(count)
