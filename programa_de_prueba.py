#cajero automatico con codigo muy ¿¿basico??#

cuentaBancanria= 35000
opcionRetorno= "Si"
print("Bienvenidos al sistema del banco nacion. Por favor, introducta que operacion va a realizar")
print("Extraccion: 1")
print("Deposito: 2")
print("Extraccion en dolares: 3")

#operaciones bancarias
extraccion= 1
deposito= 2
extraccionDolares= 3


asignacionOperacion= int(input("Coloque el numero correspondiente: "))
    
def extraccionDinero():
 montoExtraccion=int(input("Ingrese el monto a retirar "))
 if montoExtraccion > cuentaBancanria:
  print("Fondos insuficientes")
 else:
  restaExtraccion= cuentaBancanria - montoExtraccion
  print("La operacion ha sido exitosa")  
  print("Resumen de su cuenta: ",restaExtraccion)
  opcionRetorno = input("Desea realizar otra operacion? Si/No: ")
  if opcionRetorno is "si":
      print(asignacionOperacion)
                                                                                                                                                          
        
def depositoCuenta():
 print("Cargando datos de la tarjeta......")
 sumaDeposito =int(input("Ingrese el monto a depositar en su cuenta: "))
 procesoDeposito=cuentaBancanria + sumaDeposito
 print("Deposito exitoso")
 print("Resumen de su cuenta: ",procesoDeposito)
 opcionRetorno = input("Desea realizar otra operacion? Si/No: ")
    
    
def extraccionDlrs():
 montodolares= int(input("Ingrese el monto en dolares: "))
 muldolares= montodolares * 350
 if muldolares > cuentaBancanria:
  print('Fondos insuficientes')
 else:
  restadls= muldolares - cuentaBancanria
  print("La operacion ha sido exitosa")
  print("Resumen de su cuenta", restadls)
  opcionRetorno = input("Desea realizar otra operacion? Si/No: ")


   

if asignacionOperacion is extraccion:
     extraccionDinero()

elif asignacionOperacion is deposito:
    depositoCuenta()

elif asignacionOperacion is extraccionDolares:
     extraccionDlrs()   

