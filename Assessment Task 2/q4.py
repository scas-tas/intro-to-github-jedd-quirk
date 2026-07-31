def e(m: str, s: int) -> str:
    c=""
    for M in m.lower():c+=chr((ord(M)-97+s)%26+97)
    return c
def d(m: str, s: int) -> str:
    c=""
    for M in m.lower():c+=chr((ord(M)-97-s)%26+97)
    return c
print(d(e("abcdefg",26),27))