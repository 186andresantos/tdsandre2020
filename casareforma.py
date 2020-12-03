def casa(largura, altura, comprimento):
    area = largura, altura, comprimento
    return area

area_piso = largura * comprimento
volume_sala = largura * comprimento * altura
area_paredes = ( 2 * altura * largura ) + ( 2 * altura * comprimento )
a = casa(area_piso, volume_sala, area_paredes)
print(f' a área total da casa é, {a}' )