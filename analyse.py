import rpy2.robjects as robjects
import julia 
import crible
import matplotlib.pyplot as plt

j = julia.Julia()

def analyse_and_plot(listeParams):	
	res_julia = analyse_julia(listeParams)
	res_R = analyse_R(listeParams)
	res_python = crible.analyse(listeParams)

	plt.plot(listeParams,res_julia[0], 'r:o', label = "Julia : nous")
	plt.plot(listeParams,res_julia[1], 'y:o', label = "Julia : eux")

	plt.plot(listeParams,res_R[0], 'g:o', label = "R : nous")
	plt.plot(listeParams,res_R[1], 'k:o', label = "R : eux")

	plt.plot(listeParams,res_python[0], 'b:o', label = "Python : nous")
	plt.plot(listeParams,res_python[1], 'm:o', label = "Python : eux")

	plt.xlabel('Nombre appelé')
	plt.ylabel("Temps d'exécution")

	plt.legend()

	plt.show()


def analyse_julia(listeParams):
	j.include("crible.jl")
	res = j.eval("crible("+str(listeParams)+")")
	return res



def analyse_R(listeParams):
	robjects.r('source("crible.r")')

	listeParams = str(listeParams)[1:-1]
	listeParams = "c(" + listeParams + ")"

	res = robjects.r("analyse("+listeParams+")")
	listeRes = [[],[]]
	for i in range(len(res[0])):
		listeRes[0].append(res[0][i][0])
		listeRes[1].append(res[1][i][0])
	return listeRes



analyse_and_plot([5,10,50,100,500,1000,2000,3000,4000,5000,10000,25000,50000,75000,100000])
