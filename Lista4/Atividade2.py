palavras  = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper() , w.lower(), len(w)] for w in palavras]
for i in resultado:
 print(i)

 valores = list(map(lambda w: [w.upper(),w.lower() ,len(w)] , palavras))


for v in valores:
    print(v)
