# Función que solicita el número

def obtenerNumero():
    return int(input("Ingrese un número: "));

# Función que calcula los pares.

def mostrarPares(numero):
    for i in range(numero*2, ++2):  #aqui se recorre la primera función desde 0 
        print(i);                   #aqui estará mostrando de 2 en 2 

# Función que calcula los pares sin considerar el valor 0.

def mostrarParesSinCero(numero):
    for i in range(2, (numero*2)+2, ++2):
        print(i);

# Función que suma los valores impares desde 0 hasta n, donde n es el valor ingresado por usuario.

def mostrarSumaImpares(numero):
    resultado = 0;
    for i in range(numero):
        if(i%2 != 0):
            resultado += i;
    print(resultado);

# Función que suma los valores impares desde 0 hasta n, donde n es el valor ingresado por usuario.

def mostrarSumaImparesLimites(inferior, superior):
    resultado = 0;
    for i in range(inferior, superior):
        if(i%2 != 0):
            resultado += i;
    print(resultado);

# Función que calcula el Fibonacci de n elementos.

def fibonacci(elementos):
    if elementos < 2:
        return elementos;
    else:
        return fibonacci(elementos-1) + fibonacci(elementos-2);

# Función que muestra la sucesión de fibonacci n veces.

def mostrarFibonacci(ocurrencias):
    for i in range(ocurrencias+1):
        print(fibonacci(i));       

# Función que ejecuta los programas.

def ejecutarProgramas():
    print("Solo pares, Parte 1:");
    n = obtenerNumero();            #aqui se guarda el numero que ingresó el usuario por parámetro  para luego ser llamado a la funcion del ejercicio 1 
    mostrarPares(n);                #aqui mostraran todos los numeros 
    print("Solo pares, Parte 2:");
    mostrarParesSinCero(n);         #esta vez empezará desde el 2  y no del 0
    print("Suma impares, Parte 1:");
    n2 = obtenerNumero();
    mostrarSumaImpares(n2);         #se pasa el n2 por parametro 
    print("Suma impares, Parte 2:"); #aqui esta la suma de impares parte 2 
    inferior = obtenerNumero();
    superior = obtenerNumero();
    mostrarSumaImparesLimites(inferior, superior);
    print("Secuencia de Fibonacci");
    elementosFibonacci = obtenerNumero();  #elementos de Fibonacci
    mostrarFibonacci(elementosFibonacci);

ejecutarProgramas();
