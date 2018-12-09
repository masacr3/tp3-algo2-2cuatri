def uphead(arreglo,pos,cmp):
    if pos == 0 : return

    padre = (pos - 1) // 2

    # padre > hijo
    
    if cmp (arreglo[padre], arreglo[pos]) > 0:

        #swap
        arreglo[padre],arreglo[pos] = arreglo[pos], arreglo[padre]
        uphead(arreglo,padre,cmp)

def heap_encolar(arreglo,dato,cmp):
    arreglo.append(dato)
    uphead(arreglo,len(arreglo)-1,cmp)

def downheap(arreglo, n, padre, cmp):
    if padre >= n : return

    min = padre
    izq = (2 * padre) + 1
    der = (2 * padre) + 2

    if izq < n and cmp(arreglo[izq], arreglo[min]) < 0 : min = izq

    if der < n and cmp(arreglo[der], arreglo[min]) < 0 : min = der

    if min != padre:
        #swap
        arreglo[padre],arreglo[min] = arreglo[min], arreglo[padre]
        downheap(arreglo, n , min, cmp)

def heap_desencolar(arreglo,cmp):
    if not arreglo: return

    #swap
    arreglo[0],arreglo[len(arreglo)-1] = arreglo[len(arreglo)-1], arreglo[0]

    dato = arreglo.pop()

    downheap(arreglo, len(arreglo), 0, cmp)

    return dato
