# Chanllenge 1
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

# 1. Change the value 10 in X to 15
x[1][0] = 15
print(x)

# 2. Change the last_name of the first student from "Jordan" to "Bryant"
students[0]['last_name'] = "Bryant"
print(students)

# 3. In the sport_directory, change "Messi" to "Andes"
sports_directory['soccer'][0] = 'Andes'
print(sports_directory)

# 4. Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# Challenge 2
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for name in some_list:
        print(f"first_name - {name['first_name']}, last_name - {name['last_name']}")
    return some_list
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on two separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# Challenge 3
def iterateDictionary2(key_name, some_list):
    for val in some_list:
        print(val[key_name])
iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

# Challenge 4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


def printInfo(some_dict):
  # Your code here
    for key in some_dict:
        print(len(some_dict[key]), key)
        for val in some_dict[key]:
            print(val)
    # for i in some_dict:
    #     print(i, len(some_dict[i]))
    #     for i in some_dict:
    #         print(some_dict[i])
printInfo(dojo)