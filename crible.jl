#  Crible Erathostene
#  Par Florent Alapetite, Roxane Bellot et Alexandre Boudine

# prend un entier en paramètre
# Par exemple :    cribleEratosthene(120)


function cribleEratosthene(l)
	arr=collect(2:l)
	res=[]
	while arr[1]^2 < arr[end]
		tmp=shift!(arr)
		res=[res;tmp]
		arr = filter(x->x%tmp!=0,arr)
	end
	return [res;arr]
end 
