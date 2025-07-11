# importamos el archivo lista_dato de la clase lista_numeros
from lista_datos import lista_numeros

# se crea la clase Calculadora 
class Calculadora:
    
# se hace un constructor lleno 
    def __init__(self):
#atributos de el constructor
        self.numero1=""
        self.numero2=""
        self.oblista=lista_numeros()

# se crea el medoto pedir numero
    def pedir_numero(self):
        self.numero1=input(" ingresa el primer numero:")# se  pide el primer numero
        self.numero2=input(" ingresa el segundo numero:")# se pide el segundo numero
    
# se crea el metodo almacenar_numero
    def almacenar_numero(self):
        dato_numero=[self.numero1,self.numero2]# se crea una variable donde vamos aceder a los atributos de la clase padre num1 y num2
        self.oblista.guardar_numero(dato_numero)# aqui se llama el metodo de la clase hija
        
# se crea el metodo incluir lista
    def incluir_lista(self):
        self.numero3=input( "ingresa el tercer numero: ")# se pide un tercer numero
        self.numero4=input("ingrese el cuarto numero: ")# y un cuarto numero
        numeros_nuevos= [self.numero3, self.numero4] # aqui se crea una variable donde se alamacena dicho numeros
        self.oblista.guardar_numero(numeros_nuevos) # aqui se llama el metodo de la clase hija

# se crea el metodo insertar dato
    def insertar_dato(self):
        numero = input("Ingrese el número que desea insertar: ")# se le pide un numero a el usuario  para añadirlo a la lista
        posicion = int(input("En qué posición desea insertarlo: "))# se pide la posicion donde quiere posicionar en la lista 
        self.oblista.insertar_en_posicion(posicion,numero)# se llama al metodo de la clase y se le envia los argumentos

    # se crea el metodo eliminar dato
    def eliminar_dato(self):
        numero = input(" que numeros deseas eliminar ")# se pide el numero a eliminar 
        self.oblista.eliminar_numero(numero)# llama el metodo de la clase y se envia el argumento
        
    def ver_numero(self):
        self.oblista.ver_Numero()


# codigo principal
objformulario = Calculadora()
objformulario.pedir_numero()
objformulario.almacenar_numero()
objformulario.incluir_lista()
objformulario.insertar_dato()
objformulario.eliminar_dato()
objformulario.ver_numero()

