#Se importan las librerias
import random
import time
from func1 import npi , clear, animacion

#Se declaran las frases para usar con la funcion animacion
aa = False
uvida = True
vidas = 3
vidas2 = 0
name = 'Usuario'
uw = 0
cw = 0
min=0
max=50
frase1 = '------------------------- THE SECRET NUMBER-------------------------'
frase2 = 'c a r g a n d o ...'
frase3 = 'R E V O   E M A G                                                                     '
frase5 = '! E T S A N A G                                                                       '

#Se declara la variable opc antes de entrar al while para poder iterar el menu
opc = 5
while opc != 0:
        #Se carga el menu y las opciones
        clear()
        animacion(frase1, 0.01, 1)

        print(f'                                               {name}= {uw}   Computer= {cw}' )
        print("\n")
        time.sleep(0.3)
        print('Selecciona una opcion: \n')
        time.sleep(0.3)
        print('1. Jugar')
        time.sleep(0.3)
        print('2. Configuracion')
        time.sleep(0.3)
        print('0. Salir\n')
        time.sleep(0.3)
        
        #Pide una opcion del menu
        
        opc = int(input(""))
        
        opc2 = 5
        #Entra al menu de configuracion(2)
        if opc == 2:
                while opc2 != 0:
                        clear()
                        print(f'                                               {name}= {uw}   Computer= {cw}')
                        print("\n")
                        time.sleep(0.3)
                        print('Selecciona una opcion: \n')
                        time.sleep(0.3)
                        print('1. Ingresar nombre')
                        time.sleep(0.3)
                        print('2. Definir rango')
                        time.sleep(0.3)
                        print('3. Vidas')
                        time.sleep(0.3)
                        if aa:
                                print('4. Desactivar ayuda')
                                time.sleep(0.3)
                        else:
                                print('4. Activar ayuda')
                                time.sleep(0.3)
                        print('0. Regresar\n')
                        time.sleep(0.3)
                        opc2 = int(input(""))
                        if opc2 == 1:
                                clear()
                                print(f'                                               {name}= {uw}   Computer= {cw}')
                                name = input('Escribe tu nombre: ')
                        if opc2 == 2:
                                clear()
                                min= -1
                                max= 5
                                #Pide al usuario el numero minimo y maximo, para generar el numero secreto
                                while 0 > min or 10 < min:
                                        clear()
                                        print(f'                                               {name}= {uw}   Computer= {cw}')
                                        min = int(input('elige el numero minimo(0/10): '))
                                        if min < 0 or min > 10:
                                                print('el valor es incorrecto')
                                while 10 > max or 50 < max: 
                                        clear() 
                                        print(f'                                               {name}= {uw}   Computer= {cw}')      
                                        max = int(input('elige el numero maximo(10/50): '))
                                        if max < 10 or max > 50:
                                                print('el valor es incorrecto')
                                                time.sleep(1)
                        if opc2 == 3:
                                vidas2 = int(input('Selecciona la cantidad de vidas: ')) 
                        if opc2 == 4:
                                clear()
                                if aa:
                                        print('* ayuda desactivada *')
                                        aa = False
                                else:
                                        print('* ayuda activada *')
                                        aa = True
                                time.sleep(0.8)



        if opc == 1:

                #Se genera el numero secreto                
                clear() 
                animacion(frase2, 0.05, 3)               
                print("generando numero secreto..")
                time.sleep(2)                
                info = [] #se crea la lista vacia donde va la info de num secreto
                uvida = False
                if vidas2 != 0:
                        vidas = vidas2
                else:
                        vidas = 3
                        
                num_secreto = random.randint (min,max)
                npi(num_secreto, info)
                clear()

                #Comienza el juego
                while vidas != 0:
                        clear()
                        print(f"Vidas : {vidas}                                {name}= {uw}   Computer= {cw}")
                        print('\n')
                        if vidas == 3 and aa:
                                print('(ayuda)'.center(44, '='))
                                print(f'* el numero secreto comienza con la letra {info[1]} \n')
                        elif vidas == 2 and aa:
                                print('(ayuda)'.center(44, '='))
                                print(f'* el numero secreto termina con la letra {info[2]} \n')
                        elif vidas == 1 and aa:
                                print('(ayuda)'.center(44, '='))
                                print(f'* el numero secreto es un numero {info[0]} \n')
                                uvida = True



                        #Pide al usuario un numero                       
                        num_usuario = int (input("ingresa un numero :" ))
                        
                        #Si el usuario adivina el numero secreto
                        if num_usuario == num_secreto:
                            for i in range(55):# animacion si ganaste
                                    frase6 = frase5[i::-1]
                                    clear()
                                    print(frase6)
                                    time.sleep(0.007)

                            print('\n' * 8)                                   
                            time.sleep(1)
                            print(f'El numero secreto es: {num_secreto}')
                            time.sleep(2)
                            vidas = 0
                            uw += 1 


                                
                        #Si el usuario ingresa un numero mayor al numero secreto
                        elif num_usuario > num_secreto:
                                if uvida == False:
                                        print("Fallaste! prueba un numero mas chico")
                                vidas = vidas - 1
                                time.sleep(2)
                                #Game over
                                if vidas == 0:
                                        for i in range(55):
                                                frase4 = frase3[i::-1]
                                                clear()
                                                print(frase4)
                                                time.sleep(0.008)
                                        print('\n' * 8)
                                        time.sleep(1)
                                        print(f'El numero secreto es: {num_secreto}')
                                        time.sleep(2)
                                
                        #Si el usuario ingresa un numero menor al numero secreto        
                        elif num_usuario < num_secreto:
                                if uvida == False:
                                        print("Fallaste! prueba un numero mas grande")
                                vidas = vidas - 1
                                time.sleep(2)
                                #Game over
                                if vidas == 0:
                                        for i in range(55):
                                                frase4 = frase3[i::-1]
                                                clear()
                                                print(frase4)
                                                time.sleep(0.008)
                                        print('\n' * 8)
                                        time.sleep(1)
                                        #Muestra cual era el numero secreto
                                        print(f'El numero secreto es: {num_secreto}')
                                        time.sleep(2)
                                        cw += 1
    
                        
        #Si el usuario ingresa una opcion incorrecta del menu
        elif opc != 1 and opc!=0 and opc!=2:
                print("\nvalor incorrecto!")
                time.sleep(1)

frasee = (f'''
               
                     THE SECRET NUMBER

            Universidad Tecnologica de la Rioja

. Tecnicatura en programacion 
. laboratorio de computacion
. desarrollado en python
. programado por
                  . Arol Alonso
                  . Emmanuel Brizuela Parisi
                  . Jimena Cerezo


02.07.21
''')
animacion(frasee, 0.007, 1)
time.sleep(1)
clear() 
        
        
              

                                

                

                
                
        
        
 
        
        
        

        

