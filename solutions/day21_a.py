from utils import Timer
from utils import Vec2
from utils import pi
from utils import print_dict, print_list
import math

DAY=21
PART='a'

print("###############################")
print ("Running solution for day {d} part {p}".format(d=DAY, p=PART))
print("###############################")

timer = Timer()

# Write your code here

lines = []
result = 0

def get_food_list():
    foods = []
    for l in lines:
        parts = l.split(' (')
        foods.append((
            set(parts[0].split(' ')),
            parts[1].replace(')','').replace('contains ', '').split(', ')
        ))

    return foods

def get_allergens(food_list):
    A = []
    for f in food_list:
        for a in f[1]:
            if a not in A:
                A.append(a)
    return A

def get_ingredients(food_list):
    I = []
    for f in food_list:
        for i in f[0]:
            if i not in I:
                I.append(i)
    return I

def get_possible_ingredients(food_list):
    allergens = {}
    for f in food_list:
        print(f)
        for a in f[1]:
            if a not in allergens:
                allergens[a] = []
            for i in f[0]:
                if i not in allergens[a]:
                    allergens[a].append(i)
    return allergens
    

def get_foods_with_allergen(food_list, allergens):
    foods = []
    for f in food_list:
        for allergen in allergens:
            if allergen in f[1]:
                foods.append(f)
    return foods

def get_ing_with_no_allergens(food_list):
    no_allergens = []

    for F in food_list:
        for I in F[0]:
            print("Assuming {i} is an allergen".format(i=I))
            contradictions = 0
            for A in F[1]:
                print ("Assuming {i} is allergen {a}".format(i=I, a=A))
                for f in food_list:
                    if f != F:
                        if A in f[1] and I not in f[0]:
                            print("Contradiction found")
                            contradictions += 1
            if contradictions == len(F[1]) and I not in no_allergens:
                no_allergens.append(I)

    return no_allergens


with open('files/day{day}.txt'.format(day=DAY), 'r') as f:
    lines = [l.strip() for l in f.readlines()]

food_list = get_food_list()

allergens = get_allergens(food_list)
ing = get_ingredients(food_list)

print (allergens)

allergy_poss = {}
allergy_match = {}

for a in allergens:
    print(a)
    foods = get_foods_with_allergen(food_list, [a])
    intersection = set.intersection(*[f[0] for f in foods])
    print(intersection)
    allergy_poss[a] = intersection

print_dict(allergy_poss)

while len(allergy_match) < len(allergens):
    matched = None
    for a in allergens:
        if a in allergy_poss and len(allergy_poss[a]) == 1:
            # Must be the allergen then!
            allergy_match[a] = allergy_poss[a].pop()
            del allergy_poss[a]
            matched = allergy_match[a]
            print(matched)
            break
    for a in allergens:
        if a in allergy_poss and matched in allergy_poss[a]:
            allergy_poss[a].remove(matched)
    
print(allergy_match)

no_allergens = []

for i in ing:
    if i not in allergy_match.values():
        no_allergens.append(i)

for f in food_list:
    for i in no_allergens:
        for I in f[0]:
            if i == I:
                result += 1

print(no_allergens)

print ("Result = {result}".format(result=result))

# And stop here

execution_time = timer.stop()

print("###############################")
print("Executed in {t} seconds".format(t=execution_time))
print("###############################")