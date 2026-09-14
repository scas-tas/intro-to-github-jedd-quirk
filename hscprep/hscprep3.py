def rot13(m):
    M=""
    for i in m:
        if i.isalpha():
            M+="nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(i)]
        else:
            M+=i
    return M
print(rot13("Hello, World!"))