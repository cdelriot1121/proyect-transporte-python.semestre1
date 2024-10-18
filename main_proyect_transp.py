'''
PROYECTO TRANSPORTE: Diseño de un algoritmo o codigo, para el control del horario del sistema urbano de la ciudad
de Cartagena
El sistema en el que se aplicara este algoritmo es momentaniamente en transcaribe
'''
'''
=*=*=*=*=*= ESQUEMA =*=*=*=*=*=
En principio vamos a crear un menu, para dos perfiles...
1. Actualizar el horario de buses en linea:
    Aqui se debe mostrar, una opcion de agregar un nuevo bus, eliminar cuando haya finalizado el recorrido, 
    y tambien vaciar el todos los datos.... (Tambien se deben imprimir los buses en lineas, para saber cual eliminar)

    En los datos del bus debe estar: el nombre de la ruta, las estaciones, y la hora que pasara por cada estacion,
    además tambien el tiempo se modificara dependiendo de la intesidad del trafico de la ciudad 
    (con esta opcion que digitara el conductor, se establecera un margen de error con respecto a la hora en que sale el bus,
    El margen del tiempo en minutos debe ser de +5 minutos segun va aumentando las estaciones, es decir
    Tambien debes tener en cuenta cada una de las estaciones, y las rutas que pasan por alli, el nombre de los buses son (t100e, t101, t102, t103, x101, x102):
        1. Portal (pasa: t100e, t101, t102, t103, x101, x102) (0 minutos, el conductor comienza por aqui)
        2. Madre Bernarda (pasa: t100e, t101, t102, t103) (+5m)
        3. Castellana (pasa: t101, t100e, t103) (+5m)
        4. Ejecutivos (pasa: t102, t101, t103) (+3m)
        5. 4 Vientos (pasa: t100e, t101, t103) (+2m)
        6. España (pasa: t101, t102) (+3m)
        7. Centro (pasa: t100e, t101, t102, x101, x102) (+10m)
        8. Bodeguita (pasa: t103, x101) (+5m)

2. Mostrar los buses que estan en linea
    Aqui se imprimiran, todos los buses que se encuentran en linea
    (Aqui se imprimiran, de manera ordenada:
        * Debe mostrar el nombre del bus
        * Las estaciones
        * Y la hora
    tambien debe aver una opcion para salir

3. Cerrar el programa
    Aqui se finaliza el programna en general
'''
from os import system
import time
import datetime
system('cls')

Lista_princ_buses = [ 
    ['T101', {'Portal': 0, 'MadreBernarda': 5, 'Castellana': 10, 'Ejecutivos': 13, '4Vientos': 15, 'España': 18, 'Centro': 28}],
    ['T103', {'Portal': 0, 'MadreBernarda': 5, 'Castellana': 10, 'Ejecutivos': 13, '4Vientos': 15, 'Bodeguita': 33}],
    ['T100e', {'Portal': 0, 'MadreBernarda': 5, 'Castellana': 10, '4Vientos': 15, 'Centro': 28}],
    ['x101', {'Portal': 0, 'Centro': 22, 'Bodeguita': 25}],
    ['x102', {'Portal': 0, 'Centro': 22}]
]
buses_en_linea = []  

try: 
    with open('buses_en_linea.txt', 'r') as archivo:
        for linea in archivo:
            datos_bus = linea.strip().split(',')
            nombre_ruta = datos_bus[0]
            hora_salida = datos_bus[1]
            rutas_y_hora = {}
            for i in range(2, len(datos_bus), 2):
                estacion = datos_bus[i]
                hora = datos_bus[i + 1]
                rutas_y_hora[estacion] = hora
            buses_en_linea.append([nombre_ruta, hora_salida, rutas_y_hora])
except FileNotFoundError:
    pass
while True:  
    print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
    print('=&=&=&= MENU PRINCIPAL =&=&=&=') 
    print('1. Actualizar el sistema de los buses\n2. Ver buses en línea\n3. Cerrar el programa')
    print('')
    opcion_fun = int(input('Ingrese su opción: '))  
    print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
    time.sleep(1)
    system('cls')
    if opcion_fun == 1:  
        print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
        print('1. Agregar bus\n2. Eliminar un bus en línea')
        opcion_1 = int(input('Digite su opción: '))
        print('')
        time.sleep(0.5)
        system('cls')

        if opcion_1 == 1:
            print('Buses principales disponibles:')
            for i, bus in enumerate(Lista_princ_buses):
                print(f"{i + 1}. {bus[0]}")
            opcion_bus = int(input('Ingrese el número de la ruta que va a operar: ')) 
            if opcion_bus >= 1 and opcion_bus <= len(Lista_princ_buses):
                bus_seleccionado = Lista_princ_buses[opcion_bus - 1]
                datos_bus = [] 
                rutas_y_hora = {}
                nombre_ruta = bus_seleccionado[0]
                datos_bus.append(nombre_ruta)
                hora_salida = input('Ingrese la hora de salida del bus (HH:MM): ')
                datos_bus.append(hora_salida)

                increment_temp = 0
                for estacion, tiempo in bus_seleccionado[1].items():
                    hora_estacion = (datetime.datetime.strptime(hora_salida, '%H:%M') +
                                     datetime.timedelta(minutes=tiempo + increment_temp)).strftime('%H:%M')
                    rutas_y_hora[estacion] = hora_estacion
                    increment_temp += tiempo

                datos_bus.append(rutas_y_hora)
                buses_en_linea.append(datos_bus)
                print('El bus ha sido agregado exitosamente.')
                time.sleep(2.5)
                system('cls')
            else:
                system('cls')
                print('¡Opción inválida! Por favor, seleccione una opción válida.')
        elif opcion_1 == 2:
            if len(buses_en_linea) == 0:
                print('No hay buses en línea disponibles.')
                time.sleep(2)
                system('cls')
            else:
                print('Buses en línea disponibles:')
                for i, bus in enumerate(buses_en_linea):
                    print(f"{i + 1}. {bus[0]}")

                opcion_bus = int(input('Ingrese el número del bus que desea eliminar: '))
                if opcion_bus >= 1 and opcion_bus <= len(buses_en_linea):
                    bus_eliminado = buses_en_linea.pop(opcion_bus - 1)
                    system('cls')
                    print(f'El bus {bus_eliminado[0]} ha sido eliminado exitosamente.')
                    time.sleep(2.5)
                    system('cls')
                else:
                    system('cls')
                    print('¡Opción inválida! Por favor, seleccione una opción válida.')
    elif opcion_fun == 2:
        if len(buses_en_linea) == 0:
            print('No hay buses en línea disponibles...')
            time.sleep(3.5)
        else:
            print('=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=')
            print('')
            print('Nombre del Bus   |   Estaciones y Horas')
            print('-' * 40)
            for bus in buses_en_linea:
                nombre_bus = bus[0]
                rutas_y_hora = bus[2]
                print(nombre_bus)
                for estacion, hora in rutas_y_hora.items():
                    print(f'                 |   {estacion}: {hora}')
                print('-' * 40)
            time.sleep(20)
        system('cls')
    elif opcion_fun == 3:
       
        with open('buses_en_linea.txt', 'w') as archivo:
            for bus in buses_en_linea:
                datos_bus = [bus[0], bus[1]]
                for estacion, hora in bus[2].items():
                    datos_bus.append(estacion)
                    datos_bus.append(hora)
                linea = ','.join(datos_bus)
                archivo.write(linea + '\n')
        print('Cerrando el programa...')
        time.sleep(4.5)
        system('cls')
        break