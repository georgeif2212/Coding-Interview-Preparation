def decompress(s):
    def helper(i):
        result = ""
        num = 0

        while i < len(s):
            char = s[i]

            if char.isdigit():
                # construir número multi-dígito
                num = num * 10 + int(char)

            elif char == "[":
                # llamada recursiva para obtener lo que va dentro
                sub_str, i = helper(i + 1)
                result += num * sub_str
                num = 0  # reset num

            elif char == "]":
                # cerrar la recursión y regresar
                return result, i

            else:
                # letra normal
                result += char

            i += 1

        return result, i

    final_string, _ = helper(0)
    return final_string


# print(decompress("0[abc]4[ab]c"))
# "3[abc]4[ab]c"
# abcabcabcababababc
# compressionAndDecompression("2[3[a]b]")
# 2[3[a]b]
# aaabaaab


def decompressIterative(s):
    count_stack = []  # pila de multiplicadores
    string_stack = []  # pila de resultados parciales
    curr_str = ""  # resultado actual que se está construyendo
    k = 0  # número que se está formando

    for char in s:
        if char.isdigit():
            k = k * 10 + int(char)

        elif char == "[":
            count_stack.append(k)
            string_stack.append(curr_str)
            k = 0
            curr_str = ""  # ← empezamos una nueva sección

        elif char == "]":
            repeat_count = count_stack.pop()
            prev_str = string_stack.pop()
            curr_str = prev_str + repeat_count * curr_str  # cerramos sección

        else:
            curr_str += char  # letra normal
            print(curr_str)

    return curr_str


print(decompressIterative("3[abc]4[ab]c"))
