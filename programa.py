def fatorial(n: int) -> int:
    if n < 0:
        raise ValueError("O número não pode ser negativo.")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
