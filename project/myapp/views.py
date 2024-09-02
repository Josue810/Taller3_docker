import requests
import json
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

FLASK_API_BASE_URL = 'http://localhost:5000'

def home(request):
    try:
        response = requests.get(f'{FLASK_API_BASE_URL}/users')
        response.raise_for_status()  # Verifica que la solicitud fue exitosa
        users = response.json()     # Convierte la respuesta en un objeto JSON
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        users = []  # Manejo de errores: Usa una lista vacía o maneja el error de otra manera
    except ValueError as e:
        print(f"JSON decoding failed: {e}")
        users = []  # Manejo de errores: Usa una lista vacía o maneja el error de otra manera

    return render(request, 'index.html', {'data': users})

def add_user(request):
    if request.method == 'POST':
        data = {
            'username': request.POST.get('username'),
            'name': request.POST.get('name'),
            'password': request.POST.get('password')
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f"{FLASK_API_BASE_URL}/user", json=data, headers=headers)
        response.raise_for_status()  # Verifica que la solicitud fue exitosa
    return redirect('home')

def delete_user(request, id):
    response = requests.delete(f"{FLASK_API_BASE_URL}/user/{id}")
    response.raise_for_status()  # Verifica que la solicitud fue exitosa
    return redirect('home')

def edit_user(request, id):
    if request.method == 'POST':  # Cambiar a 'POST' ya que el navegador no envía PUT directamente
        data = {
            'username': request.POST.get('username'),
            'name': request.POST.get('name'),
            'password': request.POST.get('password')
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(f"{FLASK_API_BASE_URL}/user/{id}", json=data, headers=headers)
        response.raise_for_status()  # Verifica que la solicitud fue exitosa
        return redirect('home')
    
    elif request.method == 'GET':
        response = requests.get(f"{FLASK_API_BASE_URL}/user/{id}")
        response.raise_for_status()  # Verifica que la solicitud fue exitosa
        user = response.json()
        return render(request, 'edit.html', {'data': user})
    
    else:
        return HttpResponseBadRequest("Invalid method")