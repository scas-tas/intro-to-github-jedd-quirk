def e(m: str, s,c="") -> str:
    for Mi in range(len(m)):c+=(m[Mi],chr((ord(m[Mi].lower())-97+(([s],s)[isinstance(s, str)][0],ord(str(([s],s)[isinstance(s, str)])[Mi%len(str(([s],s)[isinstance(s, str)]))])-97)[isinstance(([s],s)[isinstance(s, str)][0],str)])%26+97-32*m[Mi].isupper()))[m[Mi].isalpha()]
    return c
def d(m: str, s,c="") -> str:
    for Mi in range(len(m)):c+=(m[Mi],chr((ord(m[Mi].lower())-97-(([s],s)[isinstance(s, str)][0],ord(str(([s],s)[isinstance(s, str)])[Mi%len(str(([s],s)[isinstance(s, str)]))])-97)[isinstance(([s],s)[isinstance(s, str)][0],str)])%26+97-32*m[Mi].isupper()))[m[Mi].isalpha()]
    return c
print(d(e("Hello World!",27),27))