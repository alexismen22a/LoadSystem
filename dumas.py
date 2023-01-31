import pandas as pd
import os
import csv

flag2 = False
d = ""
rangefechas = ""
def dumas():

    print ("Bienvenido a Sistema de facil contavilidad de Alexis")
    

    flag = "1"

    while flag == "1":
        data_gather()
        print("Desea ingresar otro viaje? Si = 1, No = 2")
        flag = input()
        os.system('clear')
    else:
        calculate_total()
        print("Gracias por usar el sistema de facil contavilidad de Alexis")
        print("Hasta la proxima")
        exit()

    


def data_gather():
    global flag2
    global d
    global rangefechas
    Template =  ["CUSTOMER","DATE","BOL#","ORIGIN","ORIGIN TICKET#","ORIGIN" "WEIGHT","DESTINATION","DESTINATION TICKET#"," DESTINATION WEIGHT","BUSHEL / TONS","FREIGH RATE", "TOTAL"]
  
    if flag2 == False:
        print("Por favor ingresar nombre del chofer")
        d = input()
        print("Por favor ingrese el rango de fechas de los viajes")
        rangefechas = input()
        flag2 = True
        #Create a csv file and write the data to it
        with open(d+rangefechas+'.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(Template)
            csvFile.close()


    


    customerdata = "Gavilon"
    date = ""
    bol = "DDG"
    origin = "ETTER"
    origin_ticket = ""
    origin_weight = ""
    destination = ""
    destination_ticket = ""
    destination_weight = ""
    bushel_tons = ""
    freight_rate = ""
    
    total = ""

   
    os.system('clear')
    print ("Por favor ingrese los datos solicitados")
    print ("Fecha de la carga")
    date = input()
    os.system('clear')
    print("Es DDG? Si = 1, No = 2")
    ddg_is = input()
    os.system('clear')
    if ddg_is == "1":
        bol = "DDG"
    else:
        print("Por favor ingresar el alimento")
        bol = input()
    os.system('clear')
    print ("Numero de ticket de origen")
    origin_ticket = input()
    os.system('clear')
    print ("Peso de la carga en origen")
    origin_weight = input()
    os.system('clear')
    print ("Lugar de destino")
    destination = input()
    os.system('clear')
    print ("Numero de ticket de destino")
    destination_ticket = input()
    os.system('clear')
    print ("Peso de la carga en destino")
    destination_weight = input()
    os.system('clear')
    print ("Tiene Bushel / tons escrito?")
    print ("Si = 1, No = 2")
    ithas = input()
    os.system('clear')
    if ithas == "1":
        print ("Bushel o Tons")
        bushel_tons = input()
    os.system('clear')
    print ("Tarifa de flete")
    freight_rate = input()
    os.system('clear')
    total = float(origin_weight) * float(freight_rate)
    print ("Total: " ,total)

    with open(d+rangefechas+'.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([customerdata,date,bol,origin,origin_ticket,origin_weight,destination,destination_ticket,destination_weight,bushel_tons,freight_rate,total])
            csvFile.close()

def calculate_total():
    with open(d+rangefechas+'.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        total = 0
        for row in reader:
            if row[11] != "TOTAL":
                total = total + float(row[11])
        print("Suma de todas las cargas: ", total)
        csvFile.close()
    
    with open (d+rangefechas+'.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writerrow2 = ["","","","","","","","","","","",""]
        writer.writerow(writerrow2)
        writer.writerow(["","","","","","","","","","","","Suma de todas las cargas: ",total])

dumas()