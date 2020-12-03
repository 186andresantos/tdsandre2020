def data(dia, mês, ano):
    t = dia, mês, ano
    return t

dd = int(input( " Dia: "))
mm = int(input( " Mês: "))
aa = int(input( " Ano: "))
t = data(dd, mm, aa)

print(f' A data formatada é {t}')
