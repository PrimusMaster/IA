from numpy import asarray
from numpy import arange
from numpy import exp
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed
from matplotlib import pyplot

# Funcion objetivo
def objective(x):
	#return	x[0]**(4)+3*x[0]**(3)+2*x[0]**(2)-1 
	return x[0]**(2)-3*x[0]-8

# simulated annealing
def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
	# genera el punto inicial
	best = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
	# se evalua el punto inicial initial
	best_eval = objective(best)
	# Solucion actual
	curr, curr_eval = best, best_eval
	scores = list()
	# Inicio del templado
	for i in range(n_iterations):
		# da un paso y lo evalua
		candidate = curr + randn(len(bounds)) * step_size
		candidate_eval = objective(candidate)
		# checa por una solucion mejor
		if candidate_eval < best_eval:
			# Guarda el nuevo mejor punto, tanto como el mejor candidato como en el conjunto
			# de mejores, se imprimer el progreso 
			best, best_eval = candidate, candidate_eval
			scores.append(best_eval)
			print('>%d f(%s) = %.5f' % (i, best, best_eval))
		# Diferencia entre el candidato y el punto actual a evaluar
		diff = candidate_eval - curr_eval
		# temperatura
		t = temp / float(i + 1)
		# calcula la metropolis de criterio de aceptacion
		metropolis = exp(-diff / t)
		# Comprueba si se mantiene el punto nuevo
		if diff < 0 or rand() < metropolis:
			# se guarda el punto nuevo
			curr, curr_eval = candidate, candidate_eval
	return [best, best_eval, scores]

# Rango de la entrada
r_min = -10.0
r_max = 10.0
bounds = asarray([[r_min, r_max]])
# Numero de iteraciones
n_iterations = 10000
# El maximo del tamaño de los saltos
step_size = 0.2
# temperatura inicial
temp = 15
# Se llama a la funcion del annealing para hacer la busqueda
best, score, scores = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
print('Solucionado!')
print('f(%s) = %f' % (best, score))

# Graficas
figure, (axis1, axis2) = pyplot.subplots(1, 2)

# La funcion
inputs = arange(r_min, r_max, step_size)
# compute targets
results = [objective([x]) for x in inputs]
# crea una line plot de input vs result
axis1.plot(inputs, results)
x_optima = 0.0
# dibuja una linea roja en el punto optimo
axis1.axvline(x=x_optima, ls='--', color='red')

# line plot de los mejores resultados
axis2.plot(scores, '.-')
axis2.set_xlabel('Cantidad de mejoras')
axis2.set_ylabel('f(x)')
pyplot.show()