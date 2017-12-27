#Calcul time elapsed in CPU for function f (crible Eratosthene) with parameter p
#Example : elapsed_time(cribleEratosthene,10^6)

function elapsed_time(f,p)
	tic();
	f(p);
	return toc();
end