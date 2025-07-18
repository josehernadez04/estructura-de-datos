# importamos el archivo lista_dato de la clase lista_numeros
from base_datos import lista_numeros

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
        self.numero1=int(input(" ingresa el primer numero:"))# se  pide el primer numero
        self.numero2=int(input(" ingresa el segundo numero:"))# se pide el segundo numero
    
# se crea el metodo almacenar_numero
    def almacenar_numero(self):
        dato_numero=[self.numero1,self.numero2]# se crea una variable donde vamos aceder a los atributos de la clase padre num1 y num2
        self.oblista.guardar_numero(dato_numero)# aqui se llama el metodo de la clase hija
        
# se crea el metodo incluir lista
    def incluir_lista(self):
        numero3=int(input( "ingresa un numero: "))# se pide un tercer numero
        numero4=int(input("ingrese otro numero: "))# y un cuarto numero
        numeros_nuevos= [numero3,numero4] # aqui se crea una variable donde se alamacena dicho numeros
        self.oblista.guardar_numero(numeros_nuevos) # aqui se llama el metodo de la clase hija

# se crea el metodo insertar dato
    def insertar_dato(self):
        valor1 = int(input("Ingrese un numero: "))# se le pide un numero a el usuario  para añadirlo a la lista
        valor2 = int(input("Ingresa otro numero: "))
        agg_numeros= [valor1,valor2]
        posicion = int(input("En qué posición desea insertarlo: "))# se pide la posicion donde quiere posicionar en la lista 
        self.oblista.insertar_en_posicion(posicion,agg_numeros)# se llama al metodo de la clase y se le envia los argumentos

    # se crea el metodo eliminar dato
    def eliminar_por_posicion(self):
        posicion = int(input(" ingrese la posicion del numero que deseas eliminar "))# se pide el numero a eliminar 
        self.oblista.eliminar_numero(posicion)# llama el metodo de la clase y se envia el argumento
    
    def eliminar_por_valor(self):
        numero1 = int(input("ingresa el primer numero a eliminar:"))
        numero2 = int(input(" ingresa el segundo numero a eliminar:"))
        result= [numero1,numero2]
        self.oblista.remove_dato(result)
    
# codigo principal
objformulario = Calculadora()
objformulario.pedir_numero()
objformulario.almacenar_numero()
objformulario.incluir_lista()
objformulario.insertar_dato()
objformulario.eliminar_por_posicion()
objformulario.eliminar_por_valor()

# se crea un menu para el usuario

    

