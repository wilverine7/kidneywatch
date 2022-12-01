# from django.http import HttpResponse
from django.shortcuts import render, redirect
import pip._vendor.requests as requests
import json
import ast
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from .forms import CreateUserForm
from .models import comorbidity_type, person, daily_log, meal_type, substance
# Create your views here.

def indexPageView(request):
    return render(request, 'homepages/index.html')

def infoPageView(request):
    return render(request, 'homepages/info.html')

def dashboardPageView(request):
    return render(request, 'homepages/dashboard.html')

def testPageView(request):
    return render(request, 'homepages/test.html')

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
        return render(request, 'homepages/type.html', context)
    else:
        return render(request, 'homepages/type.html')

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
            return render(request, 'homepages/test.html', context)
        else:
            return render(request, 'homepages/test.html')
def loginAuthentication(request):
    if request.method =='POST':
        username= request.POST.get('loginUsername')
        password= request.POST.get('loginPassword')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
            
def loginPageView(request):
    

    return render(request, 'homepages/login.html')

def registrationPageView(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Welcome to Kidney Watch " + user+ "!")

            return redirect('registration2')

    context = {'form': form}
    return render(request, 'homepages/register.html', context)


def registrationPageView2(request):

    
    return render(request, 'homepages/registration2.html')

def createUserPageView(request):
    if request.method == 'POST':

        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        birthDate = request.POST.get("birthDate")
        gender = request.POST.get("gender")
        feet = request.POST.get("feet")
        inches = request.POST.get("inches")
        comorbidityType = request.POST.get("comorbidityType")
        weight = request.POST.get("weight")
            
        comorbidityType = int(comorbidityType)
        height = ((int(feet)*12) + int(inches))

        new_person = person()
        new_person.email = User.email
        new_person.personname = User.username
        new_person.password = User.password
        new_person.first_name = firstName
        new_person.last_name = lastName
        new_person.birth_date = birthDate
        new_person.height = height
        new_person.comorbidity_type_id = comorbidityType
        new_person.gender = gender
        new_person.weight = weight
        new_person.save()


    return render(request, 'dashboard/index.html')
    
def addFoodPageView(request):
    foodName = request.GET.get("foodName") # from test.html
    nutrients = request.GET.get(foodName+"-nutrients") # from test.html
    mealType = request.POST.get('mealType') # from addFood.html
    water = 0
    potassium = 0
    sodium = 0
    protein = 0
    phosphorus = 0
    if nutrients is None: # if we didn't get any nutrients
        pass
    else:
        nutrients = nutrients.replace('\'','\"') # reset nutrients in dictionary string
        nutrients_dict = json.loads(nutrients)  # load nutrients string into dictionary

        for nutrient_name, amount_unit in nutrients_dict.items(): # go through each nutrient and the amount for the food we selected
            if nutrient_name == "Water":
                water = amount_unit[0] # set to the first value of the list. The list is [x, mg]
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

    

    #add date
    record_date = daily_log()
    
    record_date.date = date.today()

    meal_type = request.GET.get('mealType')

    if meal_type =="B":
        record_date.meal_type_id = 1
    elif meal_type =="L":
        record_date.meal_type_id = 2
    elif meal_type =="D":
        record_date.meal_type_id = 3
    elif meal_type =="S":
        record_date.meal_type_id = 4
    else:
        record_date.meal_type_id = 5

        
    record_date.person_id = 9
    record_date.substance_id = 21
    #add meal

    # new_meal = meal()
    # new_meal.meal_type_id = request.POST.get('mealType')

    #Create a new Substance object from the model (like a new record)
    
    record_date.save()

    # this is michael's attempt to join our data
    
    import psycopg2
    
    conn = psycopg2.connect(
        database="kidneywatch3", user='postgres',
    password='manger', host='localhost', port='5432'
    )
    
    conn.autocommit = True
    cursor = conn.cursor()
    
    sql = '''SELECT * from homepages_daily_log dl
    INNER JOIN homepages_substance s on s.id = dl.substance_id
    INNER JOIN homepages_person p on p.id = dl.person_id
    INNER JOIN homepages_meal_type mt on mt.id = dl.meal_type_id
    INNER JOIN homepages_comorbidity_type ct on ct.id = p.comorbidity_type_id'''
    # sql = 'bop'
    cursor.execute(sql)
    
    results = cursor.fetchall()
    # print(sql)
    # conn.commit()
    # conn.close()
    # Make a list of all of the employee records and store it to the variable
    data = substance.objects.all()

    #Assign the list of employee records to the dictionary key "our_emps"
    # context = {
    #     "substances" : data
    # }
    substanceName = []
    substanceK = []
    nutrientlist = ['K', 'Na', 'Protein', 'Phosphate', 'Water']
    substanceKTotal = 0
    substanceNaTotal = 0
    substanceProteinTotal = 0
    substancePhosTotal = 0
    substanceWaterTotal = 0
    filter = daily_log.objects.filter(person_id = 9).select_related()
    for list in substance.objects.all():
        substanceName.append(list.name)
        substanceK.append(list.k)
        substanceKTotal += list.k
        substanceNaTotal += list.na
        substanceProteinTotal += list.protein
        substancePhosTotal += list.phosphate
        substanceWaterTotal += list.water
    substancePercentageK = 100*(substanceKTotal/3500)
    substancePercentageNa = 100*(substanceNaTotal/2300)
    substancePercentageProtein = 100*(substanceProteinTotal/(.8*50))
    substancePercentageWater = 100*(substanceWaterTotal/3.7)
    substancePercentagePhos = 100*(substancePhosTotal/3000)
    # substanceProteinTotal = substanceProteinTotal * 1000
    # substanceWaterTotal = 1000000
    # for list in substanceK:
    #     substanceKTotal = int(substanceK[list]) + int(substanceKTotal)
    result_type = type(results)
    totalList = [substancePercentageK, substancePercentageNa, substancePercentageProtein, substancePercentagePhos, substancePercentageWater]
    context = {
        'substanceName' : substanceName,
        'substanceK' : substanceK,
        'substanceKTotal' : substanceKTotal,
        'nutrientlist' : nutrientlist,
        'totalList' : totalList,
        'results' : result_type,
        'sql' : sql,
        'filter' : filter
    }
    return render(request, 'dashboard/index.html', context)
