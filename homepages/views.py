# from django.http import HttpResponse
from django.shortcuts import render
import pip._vendor.requests as requests
import json

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
    #else:
        #return render(request, 'test.html')
# query = input("Enter your query: ")
# parameters = { # set parameters
#     "api_key": 'EPMl3IkB2Wb9GzdAbcfaaYkCCucSG7JQxbGUoWGK',
#     "query": query,
#     "dataType": ["Foundation"]
# }

# response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search", params = parameters) 
# data = response.json()
# food_dict = {} # food dictionary
# for i in range(len(data["foods"])): # loop through foods
#     food_name = data["foods"][i]['description'] # food name
#     # food_id = data["foods"][i]["fdcId"] # food id
#     food_dict[food_name] = {} # set up dictionary so food id is the key
#     # food_dict[food_id][food_name] = {} # set up dictionary with food name and food id
    
#     food_dict[food_name] = {} # set up dictionary with food name and food id

#     for j in range(len(data["foods"][i]['foodNutrients'])): # loop through nutrients
#         nutrient_name = data["foods"][i]['foodNutrients'][j]['nutrientName'] # nutrient name

#         if nutrient_name == "Potassium, K" or nutrient_name == "Water" or nutrient_name == "Protein" or nutrient_name == "Sodium, Na" or nutrient_name == "Phosphorus, P": # filter nutrients
            
#             if 'value' in data["foods"][i]['foodNutrients'][j].keys(): # if the food has a value
#                 value = data["foods"][i]['foodNutrients'][j]['value'] # the value of nutrients
#                 unit = data["foods"][i]['foodNutrients'][j]['unitName'] # the unit of nutrients
#             else: # there were no nutrient values
#                 value = 0
#                 unit = 0
#             # food_dict[food_id][food_name][nutrient_name] = [value,unit] # store the value, unit, and nutrient name in the food dictionary
#             food_dict[food_name][nutrient_name] = [value,unit] # store the value, unit, and nutrient name in the food dictionary

        
# # print(food_dict)

# # for key in food_dict[328637]:
# #     print(key)

# for i in food_dict:
#     print(i)
#     for key in food_dict[i]:
#         if key == "Water":
#             food_dict[i][key][0] = round(food_dict[i][key][0]/1000,2)
#             food_dict[i][key][1] = 'L'
#         print(key)
#         print(food_dict[i][key])
