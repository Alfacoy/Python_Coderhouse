# Actividad 1
nombre_equipo = input('¿Cúal es el nombre del equipo?\n')
partidos_ganados = int(input('¿Cúantos partidos ganaron?\n')) 
partidos_empatados = int(input('¿Cúantos partidos empataron?\n')) 
partidos_perdidos = int(input('¿Cúantos partidos perdieron?\n')) 
promedio =  ((partidos_ganados * 3) + partidos_empatados) / (partidos_ganados + partidos_empatados + partidos_perdidos)
print('\nActividad 1')
print('> El promedio final para ' + nombre_equipo + ' es de: ' + str(round(promedio,2)))

# Actividad 2
cadena_1  = "versátil"
cadena_2  = "Python"
cadena_3  = "es un lenguaje"
cadena_4  = "de programación"
res = cadena_2 + ' ' + cadena_3 + ' ' + cadena_4 + ' ' + cadena_1
print('\nActividad 2')
print('> ' + res)


# Actividad 3
cadena = "acitametaM ,5.8 ,otipeP ordeP"
cadena_reverse = cadena[::-1]
nombre_alumno = cadena_reverse[0:12:1]
nota = cadena_reverse[14:17:1]
materia = cadena_reverse[19:29:1]
cadena_formateada = nombre_alumno+ ' ha sacado un ' + nota + ' en ' + materia + '.'
print('\nActividad 3')
print('> ' +cadena_formateada + '\n')