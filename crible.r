#  Crible Erathostene
#  Par Florent Alapetite, Roxane Bellot et Alexandre Boudine

# prend un entier en paramètre
# Par exemple :    cribleEratosthene(120)


cribleEratosthene <- function(n){
	if (n < 2) return(NULL)
	res <- rep(T, n)
	res[1] <- F
	prime = 2
	milieu = n / 2
	while(prime < milieu){
		res[seq(prime * 2, n, prime)] <- F
		prime <- min(which(res[prime + 1:n]) + prime)
	}
	which(res)
}