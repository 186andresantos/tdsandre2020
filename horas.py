def dia( horas, minutos, segundos):
    m = (horas * 60) + (minuto * 60) + segundos
    return m

h = int(input( "Horas: "))
m = int(input( "Minutos: "))
s = int(input( "Segundos: "))
m = dia(h, m, s)

print(f'dia: {m} ')
