from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

def index(request):
    return render(request, "index.html", {})

def showCSV(request):
    # Read Excel file into DataFrame
    df = pd.read_excel('automated_dtr/templates/skibidi.xlsx')
    
    data_list = {}

    for x in range(3, len(df), 2):
        id = df.iloc[x, 2]  # Adjust the column index as needed
        name = df.iloc[x, 10]  # Adjust the column index as needed
        if id not in data_list:
            data_list[id] = []
        data_list[id].append({'name': name})

    return JsonResponse({'value': data_list})

    # Lawrence time
    # skibidi = df.iloc[4, 4]
    # Name
    # skibidi = df.iloc[3, 10]

    # if pd.isna(skibidi):
    #     return JsonResponse({'value': skibidi})
    # else:
    #     time = [skibidi[i:i+5] for i in range(0, len(skibidi), 5)]
    #     return JsonResponse({'value': time})
