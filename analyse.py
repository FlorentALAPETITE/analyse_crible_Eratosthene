import rpy2.robjects as robjects
import julia 
import crible
import matplotlib.pyplot as plt

j = julia.Julia()

def analyse_and_plot():	
	res_julia = analyse_julia()
	res_R = analyse_R()
	res_python = crible.analyse()

	plt.plot([5,10,50,100,500,1000,5000,10000,50000,100000],res_julia[0], 'r:o', label = "Julia : nous")
	plt.plot([5,10,50,100,500,1000,5000,10000,50000,100000],res_julia[1], 'y:o', label = "Julia : eux")

	plt.plot([5,10,50,100,500,1000,5000,10000,50000,100000],res_R[0], 'g:o', label = "R : nous")
	plt.plot([5,10,50,100,500,1000,5000,10000,50000,100000],res_R[1], 'k:o', label = "R : eux")

	plt.plot([5,10,50,100,500,1000,5000,10000,50000,100000],res_python[0], 'b:o', label = "Python : nous")
	plt.plot([5,10,50,100,500,1000,5000,10000,50000,100000],res_python[1], 'm:o', label = "Python : eux")

	plt.xlabel('Nombre appelé')
	plt.ylabel("Temps d'exécution")

	plt.legend()

	plt.show()

def analyse_julia():
	res = j.include("crible.jl")
	return res



def analyse_R():
	res = robjects.r('''source("crible.r")''')
	listeRes = [[],[]]
	for i in range(len(res[0][0])):
		listeRes[0].append(res[0][0][i][0])
		listeRes[1].append(res[0][1][i][0])
	return listeRes

analyse_and_plot()
