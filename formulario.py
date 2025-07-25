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
    
    def dato_por_posicion(self):
        dato1=int(input("ingresa el primer dato a ver "))
        dato2=int(input(" ingrese segundo dato a ver "))
        n_umero=[dato1,dato2]
        self.oblista.indeex(n_umero)
    
    def contar_lista(self):
        num=int(input(" Ingrese el primer número a contar: "))
        num1=int(input(" Ingrese el segundo número a contar: "))
        cantidad=[num,num1]
        self.oblista.coun(cantidad)
        
    def ordenar_numero(self):
        self.oblista.orden_lista()
    
    def mayor_menor(self):
        self.oblista.descedente_lista()
    
# se distancia el objecto principal

formu=Calculadora()

continuar= "s"

# se crea un menu para el usuario
while continuar== "s":   
    print("\n==== BIENVENIDO USUARIO ====")
    print("===== MENU DE ARRAYS ====")
    print("1. Pedir dos numeros ")
    print("2. Almacenar los numeros pedidos ")
    print("3. Incluir nuevos numeros a la lista ")
    print("4. Insertar numeros por posicion ")
    print("5. Eliminar numero por posicion ")
    print("6. Eliminar numero por valor ")
    print("7. Buscar dato por posicion ")
    print("8. Contar numeros de la lista ")
    print("9. Ordenar lista de menor a mayor ")
    print("10. Ordenar lista de mayor a menor ")
    print("11. Ver lista actualizada ")
    print("12. Salir ")

#se crea una variable donde se va a guardar la opcion que eleji el usuario
    opc= input(" selecione la opcion del (1-12):")
#opciones para que el usuario dijite
    match opc:
        case "1":
            formu.pedir_numero()
        
        case "2":
            formu.almacenar_numero()
        
        case "3":
            formu.incluir_lista()
        
        case "4":
            formu.insertar_dato()
        
        case "5":
            formu.eliminar_por_posicion()
        
        case "6":
            formu.eliminar_por_valor()
        
        case "7":
            formu.dato_por_posicion()
        
        case "8":
            formu.contar_lista()
        
        case "9":
            formu.ordenar_numero()
        
        case "10":
            formu.mayor_menor()
        
        case "11":
            print(" LISTA ACTUALIZADA:",formu.oblista.lista_numero)
        
        case "12":
         print(" HASTA LUEGO ")
         break
    
        case _:
            print(" OPCION INVALIDA. ")

    continuar = input("\n¿Desea realizar otra operación?(s:para seguir o n:para salir ): ").lower()
    

