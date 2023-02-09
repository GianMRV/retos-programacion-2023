# Caso 1: un jugador llega a cuatro mientras el otro esta en dos
# Caso 2: los dos jugadores llegan a tres
#   Caso 2.1: Empate
#   Caso 2.2: Ventaja
#   Caso 2.3: Ganador
p1 = 0
p2 = 0
mark = ['Love', 15, 30, 40, 'Ventaja', 'Ha ganado el']
while True:
    jugador = ''
    while jugador != 'P1' and jugador != 'P2':
        jugador = input('Jugador (P1 o P2):\n').capitalize()
    if jugador == 'P1':
        p1 += 1
    else:
        p2 += 1
    if p1 >= 3 and p2 == p1:
        print('Deuce')
    elif p1 > 3 or p2 > 3:
        if p1 > p2 and p1 > 3:
            if p1-2 >= p2:
                print(f'{mark[5]} P1')
                break
            else:
                print(f'{mark[4]} P1')
        else:
            if p2-2 >= p1:
                print(f'{mark[5]} P2')
                break
            else:
                print(f'{mark[4]} P2')
    elif p1 <= 3 or p2 <= 3:
        print(f'{mark[p1]} - {mark[p2]}')