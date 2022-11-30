# from django.http import HttpResponse
from django.shortcuts import render
import pip._vendor.requests as requests
import json
import ast
from .models import comorbidity_type, person, daily_log, meal_type, substance, meal
# Create your views here.

def indexPageView(request):
    return render(request, 'index.html')

def infoPageView(request):
    return render(request, 'info.html')

def dashboardPageView(request):
    return render(request, 'dashboard.html')

def testPageView(request):
    return render(request, 'test.html')

def typePageView(request):
    foodType = None
    foodType = request.POST.get('foodGroups')
    search = None
    search = request.POST.get('searchFood')
    parameters = { 
        "api_key": 'EPMl3IkB2Wb9GzdAbcfaaYkCCucSG7JQxbGUoWGK',
        "query": search,
        "dataType": [foodType]
    }
    if search != None:
        response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search", params=parameters)

        data = response.json()
        food_dict = {} # food dictionary
        for i in range(len(data["foods"])): # loop through foods
            food_name = data["foods"][i]['description'] # food name
            food_dict[food_name] = {} # set up dictionary so food id is the key
            
            food_dict[food_name] = {} # set up dictionary with food name 

            for j in range(len(data["foods"][i]['foodNutrients'])): # loop through nutrients
                nutrient_name = data["foods"][i]['foodNutrients'][j]['nutrientName'] # nutrient name

                if nutrient_name == "Potassium, K" or nutrient_name == "Water" or nutrient_name == "Protein" or nutrient_name == "Sodium, Na" or nutrient_name == "Phosphorus, P": # filter nutrients
                    
                    if 'value' in data["foods"][i]['foodNutrients'][j].keys(): # if the food has a value
                        value = data["foods"][i]['foodNutrients'][j]['value'] # the value of nutrients
                        unit = data["foods"][i]['foodNutrients'][j]['unitName'] # the unit of nutrients
                    else: # there were no nutrient values
                        value = 0
                        unit = 0
                    food_dict[food_name][nutrient_name] = [value,unit] # store the value, unit, and nutrient name in the food dictionary
        nutrients = []
        nutrientValues = {}
        for i in food_dict:
            for key in food_dict[i]:
                if key == "Water": # convert water to liters
                    food_dict[i][key][0] = round(food_dict[i][key][0]/1000,2)
                    food_dict[i][key][1] = 'L'
                nutrientValue = str(food_dict[i][key][0]) + " " + food_dict[i][key][1] # becomes the value + unit
                nutrients.append(key)
                nutrientValues[i+key]=nutrientValue

        context = {
            'foods':food_dict,
            'nutrients': nutrients,
            'nutrientValues': nutrientValues
        }
        return render(request, 'type.html', context)
    else:
        return render(request, 'type.html')

    #else:
        #return render(request, 'type.html')

def dataRender(request):
        foodType = None
        foodType = request.POST.get('foodGroups')
        search = None
        search = request.POST.get('searchFood')
        parameters = { 
            "api_key": 'EPMl3IkB2Wb9GzdAbcfaaYkCCucSG7JQxbGUoWGK',
            "query": search,
            "dataType": [foodType]
        }
        if search != None:
            response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search", params=parameters)

            data = response.json()
            food_dict = {} # food dictionary
            for i in range(len(data["foods"])): # loop through foods
                food_name = data["foods"][i]['description'] # food name
                food_dict[food_name] = {} # set up dictionary so food id is the key
                
                food_dict[food_name] = {} # set up dictionary with food name 

                for j in range(len(data["foods"][i]['foodNutrients'])): # loop through nutrients
                    nutrient_name = data["foods"][i]['foodNutrients'][j]['nutrientName'] # nutrient name

                    if nutrient_name == "Potassium, K" or nutrient_name == "Water" or nutrient_name == "Protein" or nutrient_name == "Sodium, Na" or nutrient_name == "Phosphorus, P": # filter nutrients
                        
                        if 'value' in data["foods"][i]['foodNutrients'][j].keys(): # if the food has a value
                            value = data["foods"][i]['foodNutrients'][j]['value'] # the value of nutrients
                            unit = data["foods"][i]['foodNutrients'][j]['unitName'] # the unit of nutrients
                        else: # there were no nutrient values
                            value = 0
                            unit = 0
                        food_dict[food_name][nutrient_name] = [value,unit] # store the value, unit, and nutrient name in the food dictionary
            nutrients = []
            nutrientValues = {}
            for i in food_dict:
                for key in food_dict[i]:
                    if key == "Water": # convert water to liters
                        food_dict[i][key][0] = round(food_dict[i][key][0]/1000,2)
                        food_dict[i][key][1] = 'L'
                    nutrientValue = str(food_dict[i][key][0]) + " " + food_dict[i][key][1] # becomes the value + unit
                    nutrients.append(key)
                    nutrientValues= {key:nutrientValue}

            context = {
                'foods':food_dict,
                'nutrients': nutrients,
                'nutrientValues': nutrientValues,
                'list': nutrients
            }
            return render(request, 'test.html', context)
        else:
            return render(request, 'test.html')

def loginPageView(request):
    return render(request, 'login.html')

def registrationPageView(request):
    return render(request, 'register.html')
    
def addFoodPageView(request):
    foodName = request.GET.get("foodName")
    nutrients = request.GET.get(foodName+"-nutrients")
<<<<<<< Updated upstream
    nutrients = nutrients.replace('\'','\"')

    nutrients_dict = json.loads(nutrients) 
    context = {
             'foodName': foodName,
             'nutrients': nutrients_dict
            }
    return render(request, 'addFood.html', context)
=======
    mealType = request.POST.get('mealType')
    water = 0
    potassium = 0
    sodium = 0
    protein = 0
    phosphorus = 0
    if nutrients is None:
        pass
    else:
        nutrients = nutrients.replace('\'','\"')
        nutrients_dict = json.loads(nutrients) 

        for nutrient_name, amount_unit in nutrients_dict.items():
            if nutrient_name == "Water":
                water = amount_unit[0]
            elif nutrient_name == "Protein":
                protein = amount_unit[0]
            elif nutrient_name == "Phosphorus, P":
                phosphorus = amount_unit[0]
            elif nutrient_name == "Potassium, K":
                potassium = amount_unit[0]
            elif nutrient_name == "Sodium, Na":
                sodium = amount_unit[0]
    context = {
             'foodName': foodName,
             'nutrients': nutrients_dict,
             'mealType': mealType,
             'water': water,
             'phosphorus': phosphorus,
             'sodium': sodium,
             'potassium': potassium,
             'protein': protein
            }
    return render(request, 'homepages/addFood.html', context)

def addWaterPageView(request):
    water = request.GET.get("water")
    context = {
        'name': water
    }
    return render(request, 'homepages/addWater.html', context)

def storeFoodItemPageView(request):
    # if request.method == 'POST':


    #add date
    record_date = daily_log()
    record_date.date = request.POST.get('date')

    #add meal

    new_meal = meal()
    new_meal.meal_type_id = request.POST.get('mealType')

    #Create a new Substance object from the model (like a new record)
    new_substance = substance()
    
    #Store the data from the form to the new object's attributes (like columns)
    new_substance.name = request.GET.get('foodName')
    
    water = request.GET.get("water")
    if water == '':
        water = 0
    else:
        water = float(water)
    sodium = request.GET.get("sodium")
    if sodium == '':
        sodium = 0
    else:
        sodium = float(sodium)
    protein = request.GET.get("protein")
    if protein == '':
        protein = 0
    else:
        protein = float(protein)
    phosphorus = request.GET.get("phosphorus")
    if phosphorus == '':
        phosphorus = 0
    else:
        phosphorus = float(phosphorus)
    potassium = request.GET.get("potassium")
    if potassium == '':
        potassium = 0
    else:
        potassium = float(potassium)
    
    # protein = float(request.GET.get("protein"))
    # phosphorus = float(request.GET.get("phosphorus"))
    # potassium = float(request.GET.get("potassium"))
    # sodium = float(request.GET.get("sodium"))
    quantity = float(request.GET.get("quantity"))
    foodMeasure = request.GET.get("foodMeasure")
    if foodMeasure == "G":
        conversion = quantity/100
        protein = protein * conversion
        phosphorus = phosphorus * conversion
        potassium = potassium * conversion
        sodium = sodium * conversion
        water = water * conversion
    elif foodMeasure == "MG":
        conversion = quantity / 100000
        protein = protein * conversion
        phosphorus = phosphorus * conversion
        potassium = potassium * conversion
        sodium = sodium * conversion
        water = water * conversion
    elif foodMeasure == "OZ":
        conversion = quantity * 28.35 / 100
        protein = protein * conversion
        phosphorus = phosphorus * conversion
        potassium = potassium * conversion
        sodium = sodium * conversion
        water = water * conversion
    protein = round(protein,3)
    phosphorus = round(phosphorus,3)
    potassium = round(potassium, 3)
    sodium = round(sodium, 3)
    water = round(water,3)

    new_substance.protein = protein
    new_substance.phosphate = phosphorus
    new_substance.k = potassium
    new_substance.na = sodium
    new_substance.water = water

    
    #Save the employee record
    new_substance.save()
        
    #Make a list of all of the employee records and store it to the variable
    # data = substance.objects.all()

    #Assign the list of employee records to the dictionary key "our_emps"
    # context = {
    #     "substances" : data
    # }
    return render(request, 'homepages/dashboard.html') 
>>>>>>> Stashed changes
