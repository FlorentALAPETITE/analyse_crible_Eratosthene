#  Crible Eratosthene
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






#Crible Eratosthene de Bah Thierno, Daniel Ahmed, Florent Gaillard

function cribleEratosthene2(n)
    # prime : tableau de dimension n initialise a true
    prime = trues(n)
    # on dit que 1 n'est pas premier
    prime[1] = false
    # de 2 a n on parcourt le tableau
    for i in 2:n
     # si i est premier
        if prime[i] == true
            for j in i+1:n
            # alors pour j de i+1 a n si j est un multiple de i, il n'est pas premier
                if j % i == 0
                    prime[j] = false
                end
            end
        end 
    end
    # return les indices dont la valeur est true
    return find(prime)
end


#Calcul time elapsed in CPU for function f (crible Eratosthene) with parameter p
#Example : elapsed_time(cribleEratosthene,10^6)

function elapsed_time(f,p)
	tic();
	f(p);
	return toc();
end


#Calcul time elapsed in CPU for a list of argument, for both of the function
#Example crible([10,20,30])
#Returning an array of 2 elements, being the results of the 1st function and 2nd respectively
#Example [ [0.01 , 0.1, 1.0] , [0.02 , 0.2 , 2.0] ]
#Note : After the 1st execution of a function taking more than 60secondes, next calls won't be done, and result will be 60 

function crible(l)
	res = []
	our = []
	their = []
	do1 = true
	do2 = true
	for i in 1:length(l)
		if do1
			tmp = elapsed_time(cribleEratosthene,l[i])
			if tmp > 60
				do1 = false
				push!(our,60)
			else
				push!(our,tmp)
			end
		else
			push!(our,60)
		end
		if do2
			tmp = elapsed_time(cribleEratosthene2,l[i])
			if tmp > 60
				do2 = false
				push!(their,60)
			else
				push!(their,tmp)
			end
		else
			push!(their,60)
		end
	end
	push!(res,our)
	push!(res,their)
	return res
end


crible([5,10,50,100,500,1000,5000,10000,50000,100000])

