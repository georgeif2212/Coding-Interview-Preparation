d = {}                        # diccionario vacío
d["key"] = 42                 # asigna valor 42 a clave "key"
d.get("key", 0)               # devuelve valor o 0 si no existe
for k, v in d.items(): pass   # iterar clave y valor


from collections import Counter
Counter("banana")             # {'b':1, 'a':3, 'n':2}

