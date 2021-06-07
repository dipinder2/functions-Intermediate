'''
1. Update Values in Dictionaries and Lists
'''
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
#Change the last_name of the first student from 'Jordan' to 'Bryant'
sports_directory['basketball'][0]='Bryant'
#In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]= 'Andres'
#Change the value 20 in z to 30
z[0]['y']= 30


'''
2. Iterate Through a List of Dictionaries
'''
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    lkeys = [key for key in students[0]]
    for student in students:
        print(f'{lkeys[0]} - {student[lkeys[0]]}, {lkeys[1]} - {student[lkeys[1]]}')
iterateDictionary(students)

'''
3. Get Values From a List of Dictionaries
'''
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])
print("\n")
'''
4.Iterate Through a Dictionary with List Values
'''
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    keys = (key for key in some_dict.keys())
    for i in keys:
        print(len(some_dict[i]) , i)
        for item in some_dict[i]:
            print(item)
        print("\n")
printInfo(dojo)