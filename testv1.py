# age
# height
# weight
# activity level


#location
#allergy based
#dietary preference
#gender


idly = {
    'foodname' : 'idly',
    'state' : 'tamilnadu',
    'diet_pref' : 'veg',
    'gender' : 'male',
}

dosa = {
    'foodname' : 'dosa',
    'state' : 'tamilnadu',
    'diet_pref' : 'veg',
    'gender' : 'male',
}

poori = {
    'foodname' : 'poori',
    'state' : 'bihar',
    'diet_pref' : 'non-veg',
    'gender' : 'female',
}

Foods = [idly, dosa, poori]

Recommendations = []
Recommendations1 = []
Recommendations2 = []
Recommendations3 = []

user_input = {
    'state' : 'tamilnadu',
    'diet_pref' : 'veg',
    'gender' : 'male',
}

# print(user_input['state'])
# print(dosa['state'])

for food in Foods:
    if(user_input['state']==food['state']):
        Recommendations.append(food)

for food in Recommendations:
    if(user_input['diet_pref']==food['diet_pref']):
        Recommendations1.append(food)

for food in Recommendations1:
    if(user_input['gender']==food['gender']):
            Recommendations2.append(food)
                
print(Recommendations2)