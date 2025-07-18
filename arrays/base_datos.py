# se crea la clase "lista_numeros"
class lista_numeros:

# se inicializa con unico atributo 
    def __init__(self):
# esta es lista donde se guardan todos los numeros 
        self.lista_numero=[]

 # se crea un  metodo llamado guardar numero con el (append)
    def guardar_numero(self, dato_numero): #se le agrega un parametro
        self.lista_numero.append(dato_numero)
        print("Se agrego sublista:", self.lista_numero)
    
# se crea el metodo nueva lista 
    def nueva_lista(self,numeros_nuevos):# aca se agregan un parametro
        self.lista_numero.extend(numeros_nuevos)# se le agregan esos dos numeros a la lista 
        print("Se agrego nueva sublista:",self.lista_numero)# y aqui no las muestra actualizada ya agg los dos numeros
         
# se crea el metodo donde vamos a insertar un numero con una posicion especifica 
    def insertar_en_posicion(self, posicion,agg_numeros):# se le agrega dos parametros  
        self.lista_numero.insert(posicion,agg_numeros)# en la lista se van a insertar estos dos argumentos 
        print(f"se agrego los numeros: {agg_numeros}, en la posicion:{posicion}")# y por ultimo se muestra la lista actualizada
        print("lista actualizada",self.lista_numero)
# se crea el metodo para borrar un numero de la lista
    def eliminar_numero(self,posicion):
        while True:
            try: # vamos a utilizar un try para fallos de un error
                if 0 <= posicion < len(self.lista_numero):
                    eliminado = self.lista_numero.pop(posicion)
                    print (f" se elimino los numero: {eliminado}, en la posicion: {posicion}")
                    break
                else:
                    print(" la posicion no existe en lista.")# aca en llegado caso no estar el numero muentra este dicho mensaje 

            except ValueError:
                 print(" Error: Ingresa un número válido.")# al recibir dicho argumento y no se encuenre en la array va a decir dicho mensaje
        
# metodo remove
    def remove_dato(self,result):
        while True:
            try:
                if result in self.lista_numero:
                    self.lista_numero.remove(result)
                    print(f"los numeros {result} fue eliminado.")
                    break
                else:
                    print(f"los numeros {result} no se encuentra en la lista.")
            except ValueError:
                    print("Error: Ingresa un número válido.")
                    

    