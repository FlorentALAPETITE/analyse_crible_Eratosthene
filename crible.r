#  Crible Erathostene
#  Par Florent Alapetite, Roxane Bellot et Alexandre Boudine

# prend un entier en paramètre
# Par exemple :    cribleEratosthene(120)

# nous
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

# eux

estPremier <- function(entier){
   
    if(entier==1){
        return(0)
        }
    if(entier==2){
        return(2)}
    else{
        valMaxATest=round(sqrt(entier))
        }
   
    for(i in 2:valMaxATest){
        if((entier%%i)==0){
            return (0)
            }
        }
    return (entier)
   
    }

cribleEratosthene_eux <- function(limite){
    entierToLimite<-1:limite
    quiEstPremier=lapply(entierToLimite,estPremier)
    return (quiEstPremier[quiEstPremier>0])

    }

# calcul
calcul <- function(nous, params){
	print(nous)
	inner <- list(length(params))
	j = 1
	while (j <= length(params)){
		start.time <- Sys.time()
		print(params[j])
		if (nous){
			cribleEratosthene(params[j])
		}
		else {
			cribleEratosthene_eux(params[j])
		}
		end.time <- Sys.time()
		inner[j] = end.time - start.time
		print(end.time - start.time)
		j = j + 1
	}
	inner
}

analyse <- function(){
	params = c(100, 1000, 10000, 100000, 1000000, 10000000)
	list(calcul(T, params), calcul(F, params))
}

analyse()
