texto = str(input('Digite um texto: '))
op_texto = []
tex_new=[]

for i in range(len(texto)):
    tex_new.append(texto[i])
    if texto[i] == 'a':
        op_texto.append(i)
    elif texto[i] == 'e':
        op_texto.append(i)
    elif texto[i] == 'i':
        op_texto.append(i)
    elif texto[i] == 'o':
        op_texto.append(i)
    elif texto[i] == 'u':
        op_texto.append(i)

for e in range(len(tex_new)):
    for y in op_texto:
        if e == y:
            tex_new.insert(e,tex_new[e].replace(tex_new[e],'*'))
            elemento_removido = tex_new.pop(y+1)
tex_new = " ".join(tex_new)

        
print(tex_new)