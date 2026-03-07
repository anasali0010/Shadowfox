Friends_name=['Anas','Faiz','Himanshu','Adeeb','Uzaif']
friends_name_length =[]
for name in Friends_name:
 friends_name_length .append((name,len(name)))
print(friends_name_length )

# optimised way to do the same thing using list comprehension:
'''
Friends =['Anas','Faiz','Himanshu','Adeeb','Uzaif']
friends_with_length =[(name,len(name)) for name in Friends ]
print(friends_with_length)
'''

