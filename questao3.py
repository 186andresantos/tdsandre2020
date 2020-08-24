def duracao_do_evento(hora, minuto, segundo):
    return (hora//3600) + (minuto//60) + segundo

def main():
    
    h = int(input(segundos//3600))
    m = int(input((segundos%3600)//60))
    s = int(input((segundos%3600)%60))

    r = duracao_do_evento(h,m,s)
    print( r )

if __name__ == '__main__':
    main()
