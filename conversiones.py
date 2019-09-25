#se declara la variable str Con una secuencia de dijitos 
numero="1234"
#se muestra el tipo de variable a la que pertenece.La salida type()no es un str es un dato type 
print (type(numero))
#se declara unstrin con sustitucion (en donde iranlos valoes propocionados utilizando format 
salida= "El numero utilizado es {}"
#se genera el resultado.La meta sustitucion hara que en donde esta {}se coloque el valor del numero 
print (salida.format(numero))
