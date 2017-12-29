# Get rpy2 package for python3 to execute R

* $ pip3 install rpy2==2.3.0


# Get PyJulia to call Julia (ver. >= 0.5) from Python

* In julia interpreter : Pkg.add("PyCall")

* $ git clone https://github.com/JuliaPy/pyjulia
* $ cd pyjulia
* $ pip3 install -e .

# Get matplotlib

* $ sudo apt-get install python3-tk
* $ sudo pip3 install matplotlib


# Lancer analyse 

* python3 analyse.py


# Modifier les paramètres de l'analyse 

* Dans le fichier analyse.py : modifier l'appel final à **analyse_and_plot()** avec une liste différente. 
