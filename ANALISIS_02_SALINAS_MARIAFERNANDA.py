#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:42:27 2020

@author: Fer
"""

#MANDAMOS A LLAMAR A LAS PAQUETERIAS QUE VAMOS A UTILIZAR PARA EL ANALISIS

import numpy as np #es una paqueteria fundamental de python para el analisis de datos y aqui la vamos a mandar a llamar para hacer la utlilizacion de sus estructuras de datos como conectores para transmitir los datos con diferentes algoritmos/propositos
import pandas as pd #paqueteria donde igualmente podemos trabajar con datos estructurados, filtrar,agregar junto con numpy para tener un alto rendimiento

def ordenamiento(lista):#definimos una funcion para el proximo ordenamineto de las listas con las cuales vamos a trabajar y asi cada vez que necesitemos ordentar una mandamos a llamar a la función.
    longitud=len(lista)-1#ocupando los operadores booleanos para ordenarlos mientras estos no esten en orden
    ordenado=False
    while not ordenado: 
        ordenado=True 
        for i in range(0,longitud): 
            if lista[i][1]<lista[i+1][1]: 
                ordenado=False  
                lista[i],lista[i+1]=lista[i+1],lista[i] 




dataframe=pd.read_csv('synergy_logistics_database.csv') #mandamos a llamar al archivo csv

dataframe.dtypes#imprimimos que tipo de datos son con los que vamos a trabajar si es object es str, int numeros enteros y esto lo ocuaparemos si necesitamos cambiar str a int para hacer algunas operaciones  


Exports=dataframe[dataframe['direction'].str.contains('Exports')]#aqui ya le damos valores de la lista con identificador exportar o importar a nuestra variable para haci utilizarlo en las siguientes operaciones 
Imports=dataframe[dataframe['direction'].str.contains('Imports')]

print(Exports['origin'].value_counts())#aqui hacemos el recuento de valores unicos por cada pais que existe 


#consignia 1

#aqui accedemos a los valores de las listas con cada pais que ya nos imprimio y con str.contains se prueba que el pais este contendio en la cadena de datos
Exp_Ori_China=Exports[Exports['origin'].str.contains('China')]
Exp_Ori_Japan=Exports[Exports['origin'].str.contains('Japan')]
Exp_Ori_Netherlands=Exports[Exports['origin'].str.contains('Netherlands')]
Exp_Ori_USA=Exports[Exports['origin'].str.contains('USA')]
Exp_Ori_Germany=Exports[Exports['origin'].str.contains('Germany')]
Exp_Ori_South_Korea=Exports[Exports['origin'].str.contains('South Korea')]
Exp_Ori_Canada=Exports[Exports['origin'].str.contains('Canada')]
Exp_Ori_Mexico=Exports[Exports['origin'].str.contains('Mexico')]
Exp_Ori_Singapore=Exports[Exports['origin'].str.contains('Singapore')]
Exp_Ori_France=Exports[Exports['origin'].str.contains('France')]
Exp_Ori_Australia=Exports[Exports['origin'].str.contains('Australia')]
Exp_Ori_India=Exports[Exports['origin'].str.contains('India')]
Exp_Ori_Brazil=Exports[Exports['origin'].str.contains('Brazil')]
Exp_Ori_Italy=Exports[Exports['origin'].str.contains('Italy')]
Exp_Ori_Spain=Exports[Exports['origin'].str.contains('Spain')]
Exp_Ori_Russia=Exports[Exports['origin'].str.contains('Russia')]
Exp_Ori_Switzerland=Exports[Exports['origin'].str.contains('Switzerland')]
Exp_Ori_Belgium=Exports[Exports['origin'].str.contains('Belgium')]



#HACEMOS UNA ITERACIÓN POR CADA PAIS SUMANDO TODOS LOS VALORES CON CADA PAIS QUE HACE UNA EXPORTACION
china_totales=[]
for i in ['Mexico','Spain','Rusia','South Korea','Argentina','Germany','Japan','USA','Belgium','Brazil']:
    china_totales.append(['china /'+i,Exp_Ori_China[Exp_Ori_China['destination'].str.contains(i)]['total_value'].sum()])
Aus_totales=[]
for i in ['Singapore','Thailand','Philippines','United Kingdom','Brazil','Mexico']:
    Aus_totales.append(['Australia/'+i,Exp_Ori_Australia[Exp_Ori_Australia['destination'].str.contains(i)]['total_value'].sum()])
Bel_totales=[]
for i in ['United Kingdom','Netherlands','France','Germany']:
    Bel_totales.append(['Belgica/'+i,Exp_Ori_Belgium[Exp_Ori_Belgium['destination'].str.contains(i)]['total_value'].sum()])
BRA_totales=[]
for i in ['Netherlands','Mexico','China','Argentina','USA']:
    BRA_totales.append(['Brazil/'+i,Exp_Ori_Brazil[Exp_Ori_Brazil['destination'].str.contains(i)]['total_value'].sum()])
Can_totales=[]
for i in ['United Kingdom','Mexico','USA','China','Japan','Brazil']:
    Can_totales.append(['Canada/'+i,Exp_Ori_Canada[Exp_Ori_Canada['destination'].str.contains(i)]['total_value'].sum()])
Fra_totales=[]
for i in ['United Kingdom','Netherlands','Germany','Belgium','Spain','USA','Canada','China','Italy','Russia','Austria']:
    Fra_totales.append(['Francia/'+i,Exp_Ori_France[Exp_Ori_France['destination'].str.contains(i)]['total_value'].sum()])
GER_totales=[]
for i in ['United Kingdom','France','USA','Mexico','South Korea','Italy','China','Canada','Brazil']:
    GER_totales.append(['Germany/'+i,Exp_Ori_Germany[Exp_Ori_Germany['destination'].str.contains(i)]['total_value'].sum()])
Ind_totales=[]
for i in ['United Arab Emirates','China','USA','Russia','Japan','Germany']:
    Ind_totales.append(['Inida/'+i,Exp_Ori_India[Exp_Ori_India['destination'].str.contains(i)]['total_value'].sum()])
Ita_totales=[]
for i in ['United Kingdom','Netherlands','France','Germany','Spain','Switzerland','USA','Croatia','Singapore','Canada','Ireland','Russia']:
    Ita_totales.append(['Italy/'+i,Exp_Ori_Italy[Exp_Ori_Italy['destination'].str.contains(i)]['total_value'].sum()])
Jap_totales=[]
for i in ['Germany','Brazil','Canada','China','Mexico','USA','Russia','South Korea','Singapore','Switzerland','Spain']:
    Jap_totales.append(['Japan/'+i,Exp_Ori_Japan[Exp_Ori_Japan['destination'].str.contains(i)]['total_value'].sum()])
Mex_totales=[]
for i in ['New Zealand','USA','Singapore','Brazil','Japan','Austria','Canada','Peru']:
    Mex_totales.append(['Mexico/'+i,Exp_Ori_Mexico[Exp_Ori_Mexico['destination'].str.contains(i)]['total_value'].sum()])
Neth_totales=[]
for i in ['France','Germany','Belgium','Argentina','Mexico','Brazil']:
    Neth_totales.append(['Netherlands/'+i,Exp_Ori_Netherlands[Exp_Ori_Netherlands['destination'].str.contains(i)]['total_value'].sum()])
Rus_totales=[]
for i in ['Netherlands','France','Germany','Belorussia','China','Turkey','Japan','India','South Korea']:
    Rus_totales.append(['Rusia/'+i,Exp_Ori_Russia[Exp_Ori_Russia['destination'].str.contains(i)]['total_value'].sum()])
Sin_totales=[]
for i in ['USA','Malaysia','Japan','China']:
    Sin_totales.append(['Singapore/'+i,Exp_Ori_Singapore[Exp_Ori_Singapore['destination'].str.contains(i)]['total_value'].sum()])
SK_totales=[]
for i in ['Vietnam','Japan','Mexico','China','Brazil','USA']:
    SK_totales.append(['South Korea/'+i,Exp_Ori_South_Korea[Exp_Ori_South_Korea['destination'].str.contains(i)]['total_value'].sum()])
SPA_totales=[]
for i in ['France','Germany','Russia','Belgium','Italy','Brazil']:
    SPA_totales.append(['Spain/'+i,Exp_Ori_Spain[Exp_Ori_Spain['destination'].str.contains(i)]['total_value'].sum()])
SWI_totales=[]
for i in ['France','Germany','Russia','Italy']:
    SWI_totales.append(['Switzerland/'+i,Exp_Ori_Switzerland[Exp_Ori_Switzerland['destination'].str.contains(i)]['total_value'].sum()])
USA_totales=[]
for i in ['Netherlands','Belgium','Mexico','United Arab Emirates','Argentina','Canada','Brazil','Singapore','China']:
    USA_totales.append(['USA/'+i,Exp_Ori_USA[Exp_Ori_USA['destination'].str.contains(i)]['total_value'].sum()])
        
#HACEMOS LISTAS DE ORDENAMINETO PARA CADA PAIS CON SU RESPECTIVO DESTINO
primero=[
Aus_totales[0],
Bel_totales[0],
BRA_totales[0],
Can_totales[0],
china_totales[0],
Fra_totales[0],
GER_totales[0],
Ind_totales[0],
Ita_totales[0],
Jap_totales[0],
Mex_totales[0],
Neth_totales[0],
Rus_totales[0],
Sin_totales[0],
SK_totales[0],
SPA_totales[0],
SWI_totales[0],
USA_totales[0]
]
ordenamiento(primero)



segundo=[
Aus_totales[1],
Bel_totales[1],
BRA_totales[1],
Can_totales[1],
china_totales[1],
Fra_totales[1],
GER_totales[1],
Ind_totales[1],
Ita_totales[1],
Jap_totales[1],
Mex_totales[1],
Neth_totales[1],
Rus_totales[1],
Sin_totales[1],
SK_totales[1],
SPA_totales[1],
SWI_totales[1],
USA_totales[1]
]
ordenamiento(segundo)

tercero=[
Aus_totales[2],
Bel_totales[2],
BRA_totales[2],
Can_totales[2],
china_totales[2],
Fra_totales[2],
GER_totales[2],
Ind_totales[2],
Ita_totales[2],
Jap_totales[2],
Mex_totales[2],
Neth_totales[2],
Rus_totales[2],
Sin_totales[2],
SK_totales[2],
SPA_totales[2],
SWI_totales[2],
USA_totales[2]
]
ordenamiento(tercero)




cuarto=[
Aus_totales[3],
Bel_totales[3],
BRA_totales[3],
Can_totales[3],
china_totales[3],
Fra_totales[3],
GER_totales[3],
Ind_totales[3],
Ita_totales[3],
Jap_totales[3],
Mex_totales[3],
Neth_totales[3],
Rus_totales[3],
Sin_totales[3],
SK_totales[3],
SPA_totales[3],
SWI_totales[3],
USA_totales[3]
]
ordenamiento(cuarto)




#YA ORDENADAS LAS LISTAS HACEMOS UNA NUEVA LISTA CREANDO EL TOP 3 POR CADA ORDENAMIENO E IMPRIMIMOS 
top10_exp=[
    primero[0],
    primero[1],
    primero[2],
    primero[3],
    segundo[0],
    segundo[1],
    primero[4],
    segundo[2],
    primero[5],
    tercero[0]
]


ordenamiento(top10_exp)#REORDENAMOS E IMPRIMIMOS
print("La Lista de las 10 rutas mas demandadas por exportación: ",top10_exp)

#IMPORTACIONES
print(Imports['destination'].value_counts())

##aqui accedemos a los valores de las listas con cada pais que ya nos imprimio y con str.contains se prueba que el pais este contendio en la cadena de datos para importaciones
Imp_dest_Thailand=Imports[Imports['destination'].str.contains('Thailand')]
Imp_dest_China=Imports[Imports['destination'].str.contains('China')]
Imp_dest_Mexico=Imports[Imports['destination'].str.contains('Mexico')]
Imp_dest_Japan=Imports[Imports['destination'].str.contains('Japan')]
Imp_dest_Germany=Imports[Imports['destination'].str.contains('Germany')]
Imp_dest_United_Arab_Emirates=Imports[Imports['destination'].str.contains('United Arab Emirates')]
Imp_dest_Canada=Imports[Imports['destination'].str.contains('Canada')]
Imp_dest_USA=Imports[Imports['destination'].str.contains('USA')]
Imp_dest_Poland=Imports[Imports['destination'].str.contains('Poland')]
Imp_dest_India=Imports[Imports['destination'].str.contains('India')]
Imp_dest_Singapore=Imports[Imports['destination'].str.contains('Singapore')]


#HACEMOS UNA ITERACIÓN POR CADA PAIS SUMANDO TODOS LOS VALORES CON CADA PAIS QUE HACE UNA EXPORTACION
Imp_Can_totales=[]
for i in ['USA','Japan','United Kingdom','Mexico']:
    Imp_Can_totales.append(['destino:Canada/'+i,Imp_dest_Canada[Imp_dest_Canada['origin'].str.contains(i)]['total_value'].sum()])
Imp_China_totales=[]
for i in ['USA','Mexico','Germany','Brazil']:
    Imp_China_totales.append(['destino:China/'+i,Imp_dest_China[Imp_dest_China['origin'].str.contains(i)]['total_value'].sum()])
Imp_Germany_totales=[]
for i in ['USA','Mexico','Spain','France','South Korea','Brazil']:
    Imp_Germany_totales.append(['destino:Germany/'+i,Imp_dest_Germany[Imp_dest_Germany['origin'].str.contains(i)]['total_value'].sum()])
Imp_India_totales=[]
for i in ['USA','Japan','Russia','Germany','United Arab Emirates']:
    Imp_India_totales.append(['destino:India/'+i,Imp_dest_India[Imp_dest_India['origin'].str.contains(i)]['total_value'].sum()])
Imp_Jap_totales=[]
for i in ['USA','Mexico','China','Australia','South Korea']:
    Imp_Jap_totales.append(['destino:Japan/'+i,Imp_dest_Japan[Imp_dest_Japan['origin'].str.contains(i)]['total_value'].sum()])
Imp_Mex_totales=[]
for i in ['Japan','Germany','South Korea','Spain','Italy','China']:
    Imp_Mex_totales.append(['destino:Mexico/'+i,Imp_dest_Mexico[Imp_dest_Mexico['origin'].str.contains(i)]['total_value'].sum()])
Imp_Poland_totales=[]
for i in ['France','Italy','Germany']:
    Imp_Poland_totales.append(['destino:Poland/'+i,Imp_dest_Poland[Imp_dest_Poland['origin'].str.contains(i)]['total_value'].sum()])
Imp_singa_totales=[]
for i in ['China','Japan','Malaysia']:
    Imp_singa_totales.append(['destino:Singapore/'+i,Imp_dest_Singapore[Imp_dest_Singapore['origin'].str.contains(i)]['total_value'].sum()])
Imp_Thai_totales=[]
for i in ['USA','Japan','Singapore','China','Malaysia']:
    Imp_Thai_totales.append(['destino:Thailand/'+i,Imp_dest_Thailand[Imp_dest_Thailand['origin'].str.contains(i)]['total_value'].sum()])
Imp_UAE_totales=[]
for i in ['Japan','China','South Korea','Vietnam']:
    Imp_UAE_totales.append(['destino:UAE/'+i,Imp_dest_United_Arab_Emirates[Imp_dest_United_Arab_Emirates['origin'].str.contains(i)]['total_value'].sum()])
Imp_USA_totales=[]
for i in ['China','Japan','Canada','Mexico']:
    Imp_USA_totales.append(['destino:USA/'+i,Imp_dest_USA[Imp_dest_USA['origin'].str.contains(i)]['total_value'].sum()])




#ordenamos
Imp_primeros=[
    Imp_Can_totales[0],
    Imp_China_totales[0],
    Imp_Germany_totales[0],
    Imp_Thai_totales[0],
    Imp_India_totales[0],
    Imp_Poland_totales[0],
    Imp_Mex_totales[0],
    Imp_Jap_totales[0],
    Imp_UAE_totales[0],
    Imp_USA_totales[0],
    Imp_singa_totales[0]
]
ordenamiento(Imp_primeros)



Imp_segundos=[
    Imp_Can_totales[1],
    Imp_China_totales[1],
    Imp_Germany_totales[1],
    Imp_Thai_totales[1],
    Imp_India_totales[1],
    Imp_Poland_totales[1],
    Imp_Mex_totales[1],
    Imp_Jap_totales[1],
    Imp_UAE_totales[1],
    Imp_USA_totales[1],
    Imp_singa_totales[1]
]
ordenamiento(Imp_segundos)



Imp_terceros=[
    Imp_Can_totales[2],
    Imp_China_totales[2],
    Imp_Germany_totales[2],
    Imp_Thai_totales[2],
    Imp_India_totales[2],
    Imp_Poland_totales[2],
    Imp_Mex_totales[2],
    Imp_Jap_totales[2],
    Imp_UAE_totales[2],
    Imp_USA_totales[2],
    Imp_singa_totales[2]
]
ordenamiento(Imp_terceros)





#sacamos ell top de las listas

top10_imp=[
    Imp_primeros[0],
    Imp_primeros[1],
    Imp_segundos[0],
    Imp_terceros[0],
    Imp_primeros[2],
    Imp_primeros[3],
    Imp_primeros[4],
    Imp_segundos[1],
    Imp_primeros[5],
    Imp_segundos[2]
]



ordenamiento(top10_imp)
print("Lista de las 10 rutas más demandadas por IMPORTACIÓN:  ",top10_imp)
      
#consignia3

#aqui sacamos el porcentaje para cada pais 
porcentajes=[
(Exp_Ori_China['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Japan['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Netherlands['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_USA['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Germany['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_South_Korea['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Canada['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Mexico['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Singapore['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_France['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Australia['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_India['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Brazil['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Italy['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Spain['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Russia['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Switzerland['total_value'].sum()/Exports['total_value'].sum())*100,
(Exp_Ori_Belgium['total_value'].sum()/Exports['total_value'].sum())*100
]

#haciendo la suma que fuera hasta el 80% imprimomos los paises con más exportaciones 
nombres=['CHI','JAP','NET','USA','GER','S.K','CAN','MEX','SING','FRA','AUS','IND','BRA','ITA','SPA','RUS','SWI','BEL']    
print(nombres,"con un porcentaje de: ")

print(porcentajes[0]+porcentajes[3]+porcentajes[9]+porcentajes[5]+porcentajes[15]+porcentajes[1]+porcentajes[4]+porcentajes[6])


#analogo al de exportaciones
porc_import=[
    (Imp_dest_Thailand['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_China['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Mexico['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Japan['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Germany['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_United_Arab_Emirates['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Canada['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_USA['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Poland['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_India['total_value'].sum()/Imports['total_value'].sum())*100,
    (Imp_dest_Singapore['total_value'].sum()/Imports['total_value'].sum())*100,
]  

nomimport=['ThA','CHI','MEX','JAP','GER','UAE','CAN','USA','POL','IND','SING']



print(porc_import[0]+porc_import[2]+porc_import[5]+porc_import[3]+porc_import[4]+porc_import[7])

    
      