// Caso 1: un jugador llega a cuatro mientras el otro esta en dos
// Caso 2: los dos jugadores llegan a tres
//   Caso 2.1: Empate
//   Caso 2.2: Ventaja
//   Caso 2.3: Ganador
let p1 = 0
let p2 = 0
const mark = ['Love', 15, 30, 40]
const play = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'] // Ingresar la secuencia de puntos que desee aqui
let i = 0
while (i < play.length){
    let jugador = play[i]
    if (jugador == 'P1')
        p1 += 1
    else
        p2 += 1
    if (p1 >= 3 && p2 == p1)
        console.log('Deuce')
    else if (p1 > 3 || p2 > 3){
        if (p1 > p2 && p1 > 3){
            if (p1-2 >= p2){
                console.log('Ha ganado el P1')
                break
            }
            else
                console.log('Ventaja P1')
        }
        else{
            if (p2-2 >= p1){
                console.log('Ha ganado el P2')
                break
            }
            else
                console.log('Ventaja P2')
        }
    }
    else if (p1 <= 3 || p2 <= 3)
        console.log(mark[p1] + ' - ' + mark[p2])
    i++
}