for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #cuando print no tiene argumento es un salto de linea 
    print ()
    #dentro de un for se coloca otro for 
    for j in range(1,11):
     #i =número base de tabla y j=el elemento
     salida="{} x {} ={}"
     print (salida.format(i,j,i*j))
    else:
    #al cumplirse esto se ejecuta el codigo que es unsalto de linea 
    print()
