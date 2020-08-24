def compras(a, b,c, d):
    return a, b, c, d

def main():
    compra= float(input())
    vista= compra-(compra*9/100)
    cinco_vezes= compra
    dez_vezes= compra+(compra*17/100)
    print(f'{vista:.2f}')
    print(f'{cinco_vezes:.2f}')
    print(f'{dez_vezes:.2f}')

if __name__=='__main__':
    main()
