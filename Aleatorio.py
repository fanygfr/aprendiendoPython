#python contiene muchas librerias preparadas para poder ser utilizadas a estas librerias se les da el nombre de modules 
#para utilizar in modulo en  un programa primero se denbe importar usando la instruccion import 
import random

#se define una variable Float y se le da un valor 
numero1= float(10.5)

#en este lenguaje, una funcion es unconjunto de intruccciones que procesan alguna tarea en especifico como como una unidad de ejecucion 
#se declara con def el codigo colocandolo a la derecha de la definicon que forma parte de la funcion 
def mifuncion():
    #se convierte a float el numero aleatrrio generado por random.randrage()(solo esta disponible si se importa el valor random )
    numero2=float(random.randrange(1,10))
    #se utiliza meta sustituciones para gnerar los resultados 
    mensaje= "la suma de {} y {} es {}"
    print (mensaje.format(numero1,numero2,numero1+numero2))  
#se esjecuta la funcion que se definio en el codigo
mifuncion()

