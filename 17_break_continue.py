s = 'Using loops. in Python' 
# automates and repeats the tasks in an efficient manner. But sometimes, there may arise a condition where you want to exit the loop completely, skip an iteration or ignore that condition.'

# for c in s:
#     if c == '.':
#         break
#     print(c)

for c in s:
    if c in 'io':
        continue
    print(c)

# pass 
for c in s:
    pass