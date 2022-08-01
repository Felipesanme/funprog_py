# Delivery

def alm_ped() -> dict:
    n = 0
    cliente = ""
    orden = ()
    orden_cliente = {}

    n = int(input())  # número de órdenes

    for _ in range(n):
        cliente = input()
        orden = set(tuple(map(str, input().split())))
        orden_cliente[cliente] = orden
        print(orden_cliente[cliente])

    print(orden_cliente.items())
alm_ped()
