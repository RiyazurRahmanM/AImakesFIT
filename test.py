
idly = {
    'foodname' : 'idly',
    #this food is best for =>
    'goal' : 'loss',
    'height' : 'heightgroup4',
    'weight' : 'weightgroup3',
    'gender' : 'male',
    'allergies' : 'peanuts',
    'activity' : 'lightlyactive',
    'dietpref' : 'vegan',
    'age' : 'agegroup3',
    'location' : 'india',
}

poori = {
    'foodname' : 'poori',
    #this food is best for =>
    'goal' : 'loss',
    'height' : 'heightgroup4',
    'weight' : 'weightgroup3',
    'gender' : 'male',
    'allergies' : 'peanuts',
    'activity' : 'lightlyactive',
    'dietpref' : 'vegan',
    'age' : 'agegroup3',
    'location' : 'usa',
}

dosa = {
    'foodname' : 'dosa',
    #this food is best for =>
    'goal' : 'loss',
    'height' : 'heightgroup4',
    'weight' : 'weightgroup3',
    'gender' : 'male',
    'allergies' : 'peanuts',
    'activity' : 'lightlyactive',
    'dietpref' : 'vegan',
    'age' : 'agegroup3',
    'location' : 'india',
}

foods = [idly,dosa,poori]

userinput = {
    'foodname' : 'idly',
    #this food is best for =>
    'goal' : 'loss',
    'height' : 'heightgroup4',
    'weight' : 'weightgroup3',
    'gender' : 'male',
    'allergies' : 'peanuts',
    'activity' : 'lightlyactive',
    'dietpref' : 'vegan',
    'age' : 'agegroup3',
    'location' : 'india',
}

recomendations = []

for i in range(0,len(foods)):

    if(userinput['location']==foods[i]['location']):
        recomendations.append(
            foods[i]
        )
for i in recomendations:
    print(i)