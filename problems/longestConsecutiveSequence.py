def longestConsecutive(nums):
    num_set = set(nums)  # Paso 1: convertir a set para acceso rápido
    max_length = 0  # Aquí guardamos la secuencia más larga encontrada

    for num in num_set:  # Paso 2: recorrer todos los números del set

        if num - 1 not in num_set:  # Solo empezamos si es el comienzo de una secuencia

            current = num  # current es el número actual que estamos evaluando
            current_streak = 1  # Empezamos una nueva secuencia, lleva al menos 1 número

            while current + 1 in num_set:  # Mientras el siguiente número esté en el set
                current += 1  # Avanzamos al siguiente número
                current_streak += 1  # Aumentamos el contador de la secuencia

            # Si encontramos una secuencia más larga que la anterior, la actualizamos
            max_length = max(max_length, current_streak)

    return max_length  # Al final devolvemos la longitud más larga


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
