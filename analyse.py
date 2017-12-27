import rpy2.robjects as robjects
import julia 
#import matplotlib.pyplot as plt

def analyse_and_plot():	



def analyse_julia():
	j = julia.Julia()
	j.include("crible.jl")


def analyse_R():
	res = robjects.r('''source("crible.r")''')

analyse_and_plot()