from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.http import Http404
import simplejson as json
import numpy as np
import time
from sympy import sympify
from scipy.integrate import odeint


global entrada
entrada = sympify('0')

global tiempo_inicio
tiempo_inicio = 0

global inicial
inicial = 0

global tiempo_anterior
tiempo_anterior = 0

global tiempo_actual
tiempo_actual = 0


### MODELOS ###
def model(y,t,k):
    dydt = -k * y
    return dydt


### VIEWS ###

def index(request):
	return render(request, "index.html")

def actualizarDatos(request):

	global entrada
	global tiempo_inicio
	global inicial
	global tiempo_anterior
	global tiempo_actual

	tiempo_anterior = tiempo_actual
	tiempo_actual = time.time() - tiempo_inicio

	respuesta = {}
	respuesta['tiempo'] = tiempo_actual
	respuesta['angulo'] = np.round( float(entrada.subs({'t': tiempo_actual}) ) , 2)

	sol_eq_1 = odeint(model,inicial,[tiempo_anterior,tiempo_actual],args=(0.1,))[1]
	inicial = sol_eq_1

	respuesta['voltaje'] = np.round( float( sol_eq_1 ) , 2)

	return HttpResponse(json.dumps(respuesta))

def entrada_req(request):

	global entrada
	global tiempo_inicio
	global inicial
	global tiempo_actual

	inicial = 10

	entrada = sympify(request.POST['campo_entrada'])

	tiempo_inicio = time.time()
	tiempo_actual = 0

	return HttpResponse("")
