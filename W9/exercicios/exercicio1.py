# "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
# "Navegadores antigos tinham uma frase gloriosa: """Navegar é preciso; viver não é preciso""". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."
# "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
# "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."

# ["Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia.", "Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.", "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.", "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."]

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    GrauSimilaridade = 0
    
    for i in range(6):
        #print(GrauSimilaridade, "+", as_a[i] - as_b[i])
        if(as_a[i] > as_b[i]):
            GrauSimilaridade += (as_a[i] - as_b[i])/6
        else:
            GrauSimilaridade += (as_b[i] - as_a[i])/6
        
    return GrauSimilaridade

def calcula_assinatura(texto):
    #Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #tamanho medio de palavra: wal= soma(tamanhoTotalDasPalavras)/numeroDePalavras
    #Relacao Type-Token: ttr = <numero de palavras diferentes> / numeroDePalavras
    #Razão Hapax Legomana: hlr = <numero de palavras usadas uma vez> / numeroDePalavras
    #Tamanho médio de sentença: sal = <soma do numero de caracteres em todas as sentencas> / numeroDeSentencas
    #Complexidade de sentença: sac = <numero de frases> / <numero de sentencas>
    #Tamanho médio de frase: pal = soma(<numero de caracteres em cada frase> / <numero de frases>)
    
    frases = []
    palavras = []
    palavrasLimpas = []
    numeroDeSentencas = 0
    numeroDeFrases = 0
    numeroDePalavras = 0
    tamanhoTotalDasPalavras = 0
    caracteresSentencas = 0
    caracteresFrases = 0

    
    sentencas = separa_sentencas(texto)
    
    for sentenca in sentencas:
        frases.append(separa_frases(sentenca))
        numeroDeSentencas += 1
        caracteresSentencas += len(sentenca)
    
    for sentenca in frases:
        for frase in sentenca:
            palavras.append(separa_palavras(frase))
            numeroDeFrases += 1
            caracteresFrases += len(frase)

    for i in range(len(palavras)):
        for j in range(len(palavras[i])):
            numeroDePalavras += 1
            tamanhoTotalDasPalavras += len(palavras[i][j])
            palavrasLimpas.append(palavras[i][j])
    
    
    
    palavrasUnicas = n_palavras_unicas(palavrasLimpas)
    palavrasDiferentes = n_palavras_diferentes(palavrasLimpas)
    
    wal = tamanhoTotalDasPalavras / numeroDePalavras
    ttr = palavrasDiferentes / numeroDePalavras
    hlr = palavrasUnicas / numeroDePalavras
    sal = caracteresSentencas / numeroDeSentencas
    sac = numeroDeFrases / numeroDeSentencas
    pal = caracteresFrases / numeroDeFrases

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    similaridades = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))
    for assinatura in assinaturas:
        similaridades.append(compara_assinatura(assinatura, ass_cp))
    menorSimilaridadeIndex = 0
    for i in range(len(similaridades)):
        if(similaridades[i] < similaridades[menorSimilaridadeIndex]):
            menorSimilaridadeIndex = i

    #print(menorSimilaridadeIndex+1)
    return (menorSimilaridadeIndex+1)

assinatura_chave = le_assinatura()
textos = le_textos()
print("O autor do texto", avalia_textos(textos, assinatura_chave), "está infectado com COH-PIAH")

