"""
Este projeto foi realizado no âmbito da UC, Fundamentos da Programação, pelo aluno Afonso Caliço Bernardo
(ist113820).
O projeto consiste num jogo MNK, no estilo do jogo popular "Jogo do Galo", em que o jogador pode alterar a configuração
do jog (colunas, linhas, quantidade de peças seguidas para obter vitória), assim como também pode escolher jogar com
peças brancas ou pretas. O jogador tem ao seu dispor 3 tipos diferentes de estratégias: fácil, normal e dificil, cada
uma com regras específicas.
O jogo quando o jogador ou o computador obterem K peças seguidas.
"""

def eh_tabuleiro(arg):
    """
    Recebe um argumento de qualquer tipo e devolve um booleano:
    True, se o argumento corresponder a um tabuleiro, ou False, caso contrário.
    eh_tabuleiro: universal --> booleano
    """
    elementos = [-1, 0, 1]
    # Verifica se o argumento é um tuplo
    if type(arg) != tuple:
        return False
    # Verifica se o tuplo é constituído apenas por tuplos
    for i in arg:
        if type(i) != tuple:
            return False

    # Verifica se o tabuleiro tem as dimensões corretas
    if len(arg) < 2 or len(arg) > 100:
        return False
    if len(arg[0]) < 2 or len(arg[0]) > 100:
        return False
    # Verifica se nos tuplos apenas estão os elementos -1, 0, 1
    for y in arg:
        for z in y:
            if z not in elementos or not type(z) == int:
                return False
    # Verifica se todos os tuplos "interiores" têm o mesmo tamanho
    for a in arg:
        if len(a) != len(arg[0]):
            return False
    return True



def tabuleiro_contado(tab):
    """
    Recebe um tabuleiro, e devolve um tabuleiro 
    em que os valores nos tuplos são transformados nas posições correspondentes.
    tabuleiro_contado: tabuleiro --> tabuleiro
    """
    valor = 0
    tabuleiro_novo = ()
    for i in range(len(tab)):
        linha = ()
        for x in tab[i]:
            valor += 1  #O valor vai corresponder à posição
            linha = linha + (valor,)
        tabuleiro_novo = tabuleiro_novo + (linha,)
    return tabuleiro_novo


def tabuleiro_lista(tab):
    """
    Recebe um tabuleiro, e devolve o tabuleiro em forma de lista.
    tabuleiro_lista: tabuleiro --> lista
    """
    lista = []
    for i in tab:
        linha = []
        for x in i:
            linha = linha + [x]
        lista.append(linha)
    return lista


def eh_jogador(jog):
    """
    Recebe um inteiro, e devolve um booleano:
    True, se o inteiro corresponder a um jogador, e Falso, caso contrário.
    eh_jogador: inteiro --> booleano
    """
    jogador = [-1, 1]
    if type(jog) == int:
        return jog in jogador
    return False


def eh_posicao(arg):
    """
    Recebe um argumento de qualquer tipo e devolve um booleano:
    True, se o argumento corresponder a uma posição dum tabuleiro, ou False, caso contrário.
    eh_posicao: universal --> booleano
    """
    return (type(arg) == int and 10000 > arg > 0)


def colunas(tab):
    """
    Recebe um tabuleiro e devolve um inteiro correspondente ao número de colunas do tabuleiro.
    colunas: tabuleiro --> inteiro
    """
    return len(tab[0])


def linhas(tab):
    """
    Recebe um tabuleiro e devolve um inteiro correspondente ao número de linhas do tabuleiro.
    linhas: tabuleiro --> inteiro
    """
    return len(tab)


def dist_chebyshev(tab, pos1, pos2):
    """
    Recebe um tabuleiro e duas posições,
    e devolve a distância entre essas posições de acordo com a distância de Chebyshev.
    dist_chebyshev: tabuleiro x posicao x posicao --> inteiro
    """
    m = linhas(tab)
    n = colunas(tab)
    tabuleiro = tabuleiro_contado(tab)
    centro = int((m // 2) * n + n / 2 + 1)
    for i in range(len(tabuleiro)):
        for x in range(len(tabuleiro[i])):
            if tabuleiro[i][x] == pos1:
                x1 = x
                y1 = i
            if tabuleiro[i][x] == pos2:
                x2 = x
                y2 = i
    dist = max(abs(x2 - x1),abs(y2-y1))
    return dist


def obtem_dimensao(tab):
    """
    Recebe um tabuleiro (tuplo) e devolve um tuplo formado pelo número de linhas e de colunas.
    obtem_dimensao: tabuleiro --> tuplo
    """
    tuplomn = (linhas(tab) , colunas(tab))
    return tuplomn


def obtem_valor(tab, pos):
    """
    Recebe um tabuleiro e uma posição do tabuleiro e devolve o valor contido nessa posição.
    obtem_valor: tabuleiro x posicao --> inteiro
    """
    count = 1           
    for i in tab:
        for x in i:
            if count == pos: 
                return x
            # O contador vai incrementando até chegar à posição desejada
            count += 1


def obtem_coluna(tab, pos):
    """
    Recebe um tabuleiro e uma posição do tabuleiro, 
    e devolve um tuplo com todas as posições que formam coluna em que esta contida a posição.
    obtem_coluna: tabuleiro x posicao --> tuplo
    """
    divisor = colunas(tab)      #número de colunas do tabuleiro
    tuplo_coluna = ()
    count = 0
    pos_coluna = pos % divisor  #corresponde à coluna em que está a posição

    #Casos em que a posição não se encontra na última coluna do tabuleiro
    if pos % divisor != 0:
        for i in tab:
            for x in i:
                count += 1
                if count % divisor == pos_coluna:
                    tuplo_coluna = tuplo_coluna + (count,)

    #Casos em que a posição encontra-se na última coluna do tabuleiro                
    if pos % divisor == 0:
        for i in tab:
            for x in i:
                count += 1
                if count % divisor == 0:
                    tuplo_coluna = tuplo_coluna + (count,)
    return tuplo_coluna


def obtem_linha(tab,pos):
    """
    Recebe um tabuleiro e uma posição do tabuleiro, 
    e devolve um tuplo com todas as posições que formam linha em que está contida a posição.
    obtem_linha: tabuleiro x posicao --> tuplo
    """
    tabuleiro = tabuleiro_contado(tab)
    for i in tabuleiro:
        for y in i:
            if y == pos:
                return i


def obtem_diagonais(tab, pos):
    """
    Recebe um tabuleiro e uma posição do tabuleiro,
    e devolve o tuplo fomrado por dois tuplos de posiçções correspondentes à diagonal e antidiagonal.
    obtem_diagonais: tabuleiro x posicao --> tuplo
    """
    tabuleiro = tabuleiro_contado(tab)
    t_diagonal = ()
    t_antidiagonal = ()
    n_linhas = linhas(tab)
    n_colunas = colunas(tab)
    for i in range(len(tabuleiro)):
        for x in range(len(tabuleiro[i])):
            if tabuleiro[i][x] == pos:
                l_pos = i
                c_pos = x
    #Para diagonais
    #Para cima
    m = l_pos
    n = c_pos
    while m >= 0 and n >= 0:
        if tabuleiro[m][n] != pos:
            t_diagonal += (tabuleiro[m][n],)
        m -= 1
        n -= 1
    #Adicionar pos
    t_diagonal += (pos,)
    #Para baixo
    m = l_pos
    n = c_pos
    while m < n_linhas and n < n_colunas:
        if tabuleiro[m][n] != pos:
            t_diagonal += (tabuleiro[m][n],)
        m += 1
        n += 1
    #Para antidiagonal
    #Para cima
    m = l_pos
    n = c_pos
    while m >= 0 and n < n_colunas:
        if tabuleiro[m][n] != pos:
            t_antidiagonal = (tabuleiro[m][n],) + t_antidiagonal
        m -= 1
        n += 1
    #Adicionar pos
    t_antidiagonal = (pos,) + t_antidiagonal
    #Para baixo
    m = l_pos
    n = c_pos
    while m < n_linhas and n >= 0:
        if tabuleiro[m][n] != pos:
            t_antidiagonal = (tabuleiro[m][n],) + t_antidiagonal
        m += 1
        n -= 1

    return (tuple(sorted(t_diagonal)), tuple(sorted(t_antidiagonal, reverse= True)))


def tabuleiro_para_str(tab):
    """
    Recebe um tabuleiro e devolve a cadeia de caracteres que o representa.
    tabuleiro_para_str: tabuleiro --> cad.carateres
    """
    m = linhas(tab)
    n = colunas(tab)
    t_string = ""
    simbolo = ""
    l = 0
    for i in range(2*m - 1): # o número de linhas total do tabuleiro "estético" dá-se através de 2*linhas - 1
        c = 0
        for x in range(4 * n -3): # o número de colunas total do tabuleiro "estético" dá-se por 4*colunas - 3
            # corresponde às linhas do tabuleiro
            if i % 2 == 0:
                #corresponde a uma posição do tabuleiro e por isso lá estarão os elementos do tabuleiro
                if x % 4 == 0:  
                    if tab[l][c] == 1:
                        simbolo = "X"
                    if tab[l][c] == -1:
                        simbolo = "O"
                    if tab[l][c] == 0:
                        simbolo = "+"
                    t_string += f"{simbolo}"
                    c += 1
                if x % 4 != 0:  # não corresponde a uma posição do tabuleiro, então só ajuda na estética
                    t_string += "-"
            # corresponde às linhas que não são do tabuleiro, ajuda na estética
            if i % 2 != 0:
                if x % 4 == 0:
                    t_string += "|"
                if x % 4 != 0:
                    t_string += " "
        # o l só aumenta se o i corresponder a uma linha do tabuleiro
        if i % 2 == 0:
            l += 1
        t_string += "\n"
    t_string = t_string[:-1]
    return t_string


def eh_posicao_valida(tab, pos):
    """
    Recebe um tabuleiro e uma posição e devolve um booleano:
    True, se a posição corresponde a uma posição do tabuleiro, ou False, caso contrário.
    eh_posicao_valida: tabuleiro x posicao --> booleano
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError('eh_posicao_valida: argumentos invalidos')

    num = 1
    for i in tab: 
        for x in i:
            #se a posição for igual ao num 
            #(que aumenta em todas as posições do tabuleiro), quer dizer que a posição é válida
            if num == pos:  
                return True
            else:
                num += 1
    return False


def eh_posicao_livre(tab, pos):
    """
    Recebe um tabuleiro e uma posição do tabuleiro, e devolve um booleano:
    True, se corresponde a uma posição vazia, ou False, caso contrário.
    eh_posicao_livre: tabuleiro x posicao --> booleano
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos):
        raise ValueError('eh_posicao_livre: argumentos invalidos')
    count = 1
    for i in tab:
        for x in i:
            #Quando chega à posição desejada, verifica se esse elemento do tuplo  é igual a 0.
            if count == pos:
                return x == 0
            count += 1


def obtem_posicoes_livres(tab):
    """
    Recebe um tabuleiro e devolve o tuplo com todas as posições livres do tabuleiro.
    obtem_posicoes_livres: tabuleiro --> tuplo
    """
    if eh_tabuleiro(tab) == False:
        raise ValueError('obtem_posicoes_livres: argumento invalido')
    count = 1
    tuplo_posicoes_livres = ()
    for i in range(len(tab)):
        for x in range(len(tab[i])):
            # o tuplo só aumenta se o valor no tabuleiro for igual a 0
            if tab[i][x] == 0:
                tuplo_posicoes_livres = tuplo_posicoes_livres + (count,)
            count += 1
    return tuplo_posicoes_livres


def obtem_posicoes_jogador(tab, jog):
    """
    Recebe um tabuleiro e um inteiro identificando um jogador e,
    devolve o tuplo com todas as posições do tabuleiro ocupadas por pedras do jogador.
    obtem_posicoes_jogador_: tabuleiro x inteiro --> tuplo
    """
    if not eh_tabuleiro(tab) or not eh_jogador(jog):
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')
    count = 1
    tuplo_jogador = ()
    # Obtem todas as posições do jogador -1
    if jog == -1:
        for i in tab:
            for x in i:
                if x == jog:
                    tuplo_jogador = tuplo_jogador + (count,)
                count += 1
    # Obtem todas as posições do jogador 1
    if jog == 1:
        for y in tab:
            for z in y:
                if z == jog:
                    tuplo_jogador = tuplo_jogador + (count,)
                count += 1
    return tuplo_jogador


def obtem_posicoes_adjacentes(tab, pos):
    """
    Recebe um tabuleiro e uma posição do tabuleiro,
    e devolve o tuplo formado pelas posições do tabuleiro adjacentes.
    obtem_posicoes_adjacentes: tabuleiro x posicao --> tuplo
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos):
        raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')
    tabuleiro = tabuleiro_contado(tab)
    tuplo_adjacentes = ()
    for i in tabuleiro:
        for x in i:
            # só é uma posição adjacente se a distância chebyshev for igual a 1
            if dist_chebyshev(tab, x, pos) == 1:
                tuplo_adjacentes += (x,)
    return tuplo_adjacentes


def ordena_posicoes_tabuleiro(tab, tup):
    """
    Recebe um tabuleiro e um tuplo de posições do tabuleiro (pode estar vazio),
    e devolve o tuplo com as posições em ordem ascendente de distância ao centro do tabuleiro.
    As posições que estão à mesma distância do centro são ordenadas de menor a maior.
    ordena_posicoes_tabuleiro: tabuleiro x tuplo --> tuplo
    """
    m = linhas(tab)
    n = colunas(tab)
    if not eh_tabuleiro(tab) or type(tup) != tuple:
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    for elementos in tup:
        if type(elementos) != int or m * n < elementos or elementos <= 0:
            raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    tabuleiro = tabuleiro_contado(tab)
    centro = int((m // 2) * n + n // 2 + 1)
    dist = 0
    tuplo_ordenado, tuplo_final = (), ()
    count = 0
    # forma ordenar todas as posições por distância ao centro (distância chebyshev)
    while count < tabuleiro[-1][-1]:
        for i in tabuleiro:
            for x in i:
                if dist_chebyshev(tab, x, centro) == dist:
                    tuplo_ordenado += (x,)
                    count += 1
        dist += 1
    # só vai adicionar em tuplo_final, os elementos em tup
    for y in tuplo_ordenado:
        if y in tup:
            tuplo_final += (y,)
    return tuplo_final

def marca_posicao(tab, pos, jog):
    """
    Recebe um tabuleiro, uma posição livre do tabuleiro e um inteiro identificando um jogador,
    e devolve um novo tabuleiro com uma nova pedra desse jogador, nessa posição.
    marca_posicao: tabuleiro x posicao x inteiro --> tabuleiro
    """
    if (not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos) or not
        eh_posicao_livre(tab,pos) or not eh_jogador(jog)):
        raise ValueError('marca_posicao: argumentos invalidos')
    tabuleiro = tabuleiro_contado(tab)
    t_lista = tabuleiro_lista(tab)
    t_final = ()
    #altera o valor na lista do tabuleiro
    for i in range(len(tabuleiro)):
        for x in range(len(tabuleiro[i])):
            if tabuleiro[i][x] == pos:
                t_lista[i][x] = jog
    #cria o tuplo com o valor alterado através da lista do tabuleiro
    for y in t_lista:
        t_auxiliar = ()
        for w in y:
            t_auxiliar += (w,)
        t_final += (t_auxiliar,)

    return t_final


def verifica_k_linhas(tab, pos, jog, k):
    """
    Recebe um tabuleiro, uma posição do tabuleiro, um inteiro identificando o jogador
    e um inteiro positivo, k, e devolve um booleano:
    True, se existe pelo menos uma linha (horizonta, vertical ou diagonal)
    que contenha a posição com k ou mais pedras consecutivas do jogador indicado, e Falso, caso contrário.
    verifica_k_linhas: tabuleiro x posicao x inteiro x inteiro --> booleano
    """
    if (not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos) or not eh_jogador(jog) or not
            type(k) == int or not k > 0):
            raise ValueError('verifica_k_linhas: argumentos invalidos')
    if pos not in obtem_posicoes_jogador(tab, jog):
        return False
    if k == 1:
        return True
    n_linhas = linhas(tab)
    n_colunas = colunas(tab)
    l_pos = (pos - 1) // n_colunas
    c_pos = (pos - 1) % n_colunas
    #Em coluna para baixo
    count = 1
    m = l_pos
    n = c_pos
    while m < n_linhas - 1:
        if tab[m][n] == tab[m+1][n]:
            count += 1
            if count == k:
                return True
        else:
            break
        m += 1
    #Em coluna para cima
    m = l_pos
    n = c_pos
    while m > 0:
        if tab[m][n] == tab[m-1][n]:
            count += 1
            if count == k:
                return True
        else:
            break
        m -= 1
    #Em linha para a frente
    count = 1
    m = l_pos
    n = c_pos
    while n < n_colunas - 1:
        if tab[m][n] == tab[m][n+1]:
            count += 1
            if count == k:
                return True
        else:
            break
        n += 1
    #Em linha para trás
    m = l_pos
    n = c_pos
    while n > 0:
        if tab[m][n] == tab[m][n-1]:
            count += 1
            if count == k:
                return True
        else:
            break
        n -= 1
    #Diagonal para baixo
    count = 1
    m = l_pos
    n = c_pos
    while m < (n_linhas - 1) and n < (n_colunas-1):
        if tab[m][n] == tab[m+1][n+1]:
            count += 1
            if count == k:
                return True
        else:
            break
        m += 1
        n += 1
    #Diagonal para cima
    m = l_pos
    n = c_pos
    while m > 0 and n > 0:
        if tab[m][n] == tab[m-1][n-1]:
            count += 1
            if count == k:
                return True
        else:
            break
        m -= 1
        n -= 1
    #Antidiagonal para cima
    count = 1
    m = l_pos
    n = c_pos
    while m > 0 and n < (n_colunas - 1):
        if tab[m][n] == tab[m-1][n+1]:
            count += 1
            if count == k:
                return True
        else:
            break
        m -= 1
        n += 1
    #Antidiagonal para baixo
    m = l_pos
    n = c_pos
    while m < (n_linhas - 1) and n > 0:
        if tab[m][n] == tab[m+1][n-1]:
            count += 1
            if count == k:
                return True
        else:
            break
        m += 1
        n -= 1
    return False


def eh_fim_jogo(tab, k):
    """
    Recebe um tabuleiro e um inteiro positivo, k, e devolve um booleano:
    True, se o jogo terminou, ou False, caso contrário.
    eh_fim_jogo: tabuleiro x inteiro --> booleano
    """
    tabuleiro = tabuleiro_contado(tab)
    if not eh_tabuleiro(tab) or not type(k) == int or not k > 0:
        raise ValueError('eh_fim_jogo: argumentos invalidos')
    if obtem_posicoes_livres(tab) == ():
        return True
    #Para o jogador 1
    for i in tabuleiro:
        for x in i:
            if verifica_k_linhas(tab, x, 1, k) == True:
                return True
    #Para o jogador -1
    for h in tabuleiro:
        for j in h:
            if verifica_k_linhas(tab, j, -1, k) == True:
                return True
    return False



def escolhe_posicao_manual(tab):
    """
    Recebe um tabuleiro e devolve uma posição introduzida manualmente pelo jogador.
    escolhe_posicao_manual: tabuleiro --> posicao
    """
    if not eh_tabuleiro(tab):
        raise ValueError('escolhe_posicao_manual: argumento invalido')
    n = input("Turno do jogador. Escolha uma posicao livre: ")
    while not (n.isdigit() and int(n) in obtem_posicoes_livres(tab)):
        n = input("Turno do jogador. Escolha uma posicao livre: ")
    return int(n)


def estrategia_facil(tab,jog):
    """
    Recebe um tabuleiro e um inteiro identificando o jogador, e devolve a posição que segue as seguintes regras:
    Se existir pelo menos uma posição livre e adjacente a uma pedra própria, jogar numa dessas posições.
    Se não, jogar numa posição livre.
    Se houver várias posições que seguem o mesmo critério, deve escolher a posição mais próxima do centro.
    estrategia_facil: tabuleiro x inteiro --> posicao
    """
    posicoes_vazias = obtem_posicoes_livres(tab)
    tabuleiro = tabuleiro_contado(tab)
    todas_posicoes_adjacentes = ()
    possibilidades = ()
    m = linhas(tab)
    n = colunas(tab)
    centro = int((m // 2) * n + n // 2 + 1)
    # Todas as posições adjacentes às posições do jogador escolhido
    for h in range(len(tab)):
        for j in range(len(tab[h])):
            if tab[h][j] == jog:
                todas_posicoes_adjacentes = todas_posicoes_adjacentes + tuple(obtem_posicoes_adjacentes(tab, tabuleiro[h][j]),)
    # Todas as posições vazias e que são adjacentes a uma posição do jogador escolhido
    for i in range(len(tabuleiro)):
        for x in range(len(tabuleiro[i])):
            if tabuleiro[i][x] in posicoes_vazias and tabuleiro[i][x] in todas_posicoes_adjacentes:
                possibilidades = possibilidades + (tabuleiro[i][x],)
    # Caso não haja nenhuma posição vazia e adjacente a outra peça do jogador, escolhe-se a posição mais perto do centro
    if possibilidades == ():
        contador = 0
        while True:
            for c in posicoes_vazias:
                if dist_chebyshev(tab, c, centro) == contador:
                    return c
            contador += 1

    #Casos em que há uma ou mais posições vazias e adjacentes a outra peça do jogador
    if possibilidades != ():
        contador = 0
        while True:
            for k in possibilidades:
                if dist_chebyshev(tab, k, centro) == contador:
                    return k
            contador += 1

def estrategia_normal(tab, jog, k):
    """
    Recebe um tabuleiro, um inteiro identificando o jogador e um inteiro positivo, k, e
    devolve a posição que segue as seguintes regras:
    Determina-se o maior valode de L <= k tal que o próprio ou o adversário podem conseguir colocar L peças consecutivas.
    estrategia_normal: tabuleiro x inteiro x inteiro --> posicao
    """
    posicoes_vazias = obtem_posicoes_livres(tab)
    m = linhas(tab)
    n = colunas(tab)
    centro = int((m // 2) * n + n // 2 + 1)
    tabuleiro = tabuleiro_contado(tab)
    num, d = 0, 100
    p_consecutivos, a_consecutivos = 0, 0
    p_jogada, a_jogada = 0, 0
    tabuleiro_original = tab
    #Para obter linha
    for pos in posicoes_vazias:
        tab = marca_posicao(tabuleiro_original, pos, jog)
        for i in range(1, k+1):
            if verifica_k_linhas(tab, pos, jog, i):
                if i > p_consecutivos:
                    p_consecutivos = i
                    d = dist_chebyshev(tab, centro, pos)
                    p_jogada = pos
                if i == p_consecutivos and dist_chebyshev(tab, centro, pos) < d:
                    p_consecutivos = i
                    d = dist_chebyshev(tab, centro, pos)
                    p_jogada = pos
    #Para impossibilitar adversário
    for pos in posicoes_vazias:
        tab = marca_posicao(tabuleiro_original, pos, -jog)
        for x in range(1, k+1):
            if verifica_k_linhas(tab, pos, -jog, x):
                if x > a_consecutivos:
                    a_consecutivos = x
                    d = dist_chebyshev(tab, centro, pos)
                    a_jogada = pos
                if x == a_consecutivos and dist_chebyshev(tab, centro, pos) < d:
                    a_consecutivos = x
                    d = dist_chebyshev(tab, centro, pos)
                    a_jogada = pos
    if a_consecutivos > p_consecutivos:
        return a_jogada
    else:
        return p_jogada


def simulacao_normal(tab, k, jog):
    """
    Recebe um tabuleiro, um inteiro positivo, k, e um inteiro a identificar o jogador, e devolve
    uma posição, depois de uma simulação inteira de um jogo na estratégia normal.
    simulacao_normal: tabuleiro x inteiro x inteiro --> posicao
    """
    posicoes_vazias_ordenadas = ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab))
    empate = ()
    for pos in posicoes_vazias_ordenadas:
        tab = marca_posicao(tab, pos, -jog)
        if verifica_k_linhas(tab, pos, -jog, k):
            return pos
        if obtem_posicoes_livres(tab) == ():
            empate = (pos,) + empate
        while eh_fim_jogo(tab, k):
            #Turno do jog
            posicao = escolhe_posicao_auto(tab, jog, k, 'normal')
            tab = marca_posicao(tab, posicao, jog)
            if verifica_k_linhas(tab, posicao, jog, k):
                break
            if obtem_posicoes_livres(tab) == ():
                empate = (pos,) + empate
                break
            #Turno do -jog
            posicao = escolhe_posicao_auto(tab, -jog, k, 'normal')
            tab = marca_posicao(tab, posicao, -jog)
            if verifica_k_linhas(tab, posicao, -jog, k):
                return pos
            if obtem_posicoes_livres(tab) == ():
                empate = (pos,) + empate
                break
    if empate != ():
        return empate[0]


def estrategia_dificil(tab, jog, k):
    """
    Recebe um tabuleiro, um inteiro identificando o jogador, um inteiro positivo, k, e
    devolve uma posição que segue as seguintes regras:
    Se existir pelo menos uma posição que permita ganhar o jogo, jogar numa dessas posições.
    Se não, e se existir pelo menos uma posição que impossibilite o adversário de ganhar, jogar numa dessas posições
    Se não, simular um jogo normal até ao fim e verificar a posição que permita obter um melhor resultado
    estrategia_dificil: tabuleiro x inteiro x inteiro --> posicao
    """
    posicoes_vazias = obtem_posicoes_livres(tab)
    m = linhas(tab)
    n = colunas(tab)
    tab_original = tab
    adv_possibilidades, sim_normal = (), ()
    d = 100
    adv_jogada = 0
    centro = int((m // 2) * n + n // 2 + 1)

    # Simulação normal
    tab = tab_original
    if simulacao_normal(tab, k, jog) != None:
        return simulacao_normal(tab, k, jog)

    # Se não houver nenhum destes casos, jogar numa posição livre mais próximo do centro
    tab = tab_original
    d, jogada = 100, 0
    for pos in posicoes_vazias:
        if dist_chebyshev(tab, centro, pos) < d:
            d = dist_chebyshev(tab, centro, pos)
            jogada = pos
    return jogada
    

def escolhe_posicao_auto(tab, jog, k, lvl):
    """
    Recebe um tabuleiro, um inteiro correspondente ao jogador, um inteiro positivo, k,
    e a cadeia de caracteres correspondente à estratégia,
    e devolve a posição escolhida automaticamente de acordo com a estratégia usada.
    escolhe_posicao_auto: tabuleiro x inteiro x inteiro x cad. carateres --> posicao
    """
    estrategias = ['facil', 'normal', 'dificil']
    if (not eh_tabuleiro(tab) or not eh_jogador(jog) or not type(k) == int or not k > 0 or
            eh_fim_jogo(tab, k) == True or lvl not in estrategias):
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')
    if lvl == 'facil': #escolhe a posição de acordo com a estratégia fácil
        return estrategia_facil(tab,jog)
    if lvl == 'normal': #escolhe a posição de acordo com a estratégia normal
        return estrategia_normal(tab,jog,k)
    if lvl == 'dificil': #escolhe a posição de acordo com a estratégia dificil
        return estrategia_dificil(tab,jog,k)
        

def jogo_mnk(cfg, jog, lvl):
    """
    É a função principal que permite jogar o jogo completo. 
    A função recebe um tuplo de três valores inteiros correspondentes aos valores de configuração do jogo m,n,k,
    um inteiro identificando as pedras do jogador humano e uma cadeia de caracteres identificando a estratégia do jogo usada pelo computador.
    jogo_mnk: tuplo x inteiro x cad.caracteres --> inteiro
    """
    estrategias = ['facil', 'normal', 'dificil']
    if (not 2 <= cfg[0] <= 100 or not 2 <= cfg[1] <= 100 or not type(cfg) == tuple or not
    eh_jogador(jog) or not lvl in estrategias):
        raise ValueError('jogo_mnk: argumentos invalidos')
    k = cfg[-1]
    m = cfg[0]
    n = cfg[1]
    if jog == 1:
        simbolo = 'X'
    if jog == -1:
        simbolo = 'O'
    tabuleiro = ()
    for i in range(m):
        linha = ()
        for x in range(n):
            linha = linha + (0,)
        tabuleiro += (linha,)
    print('Bem-vindo ao JOGO MNK.')
    print(f"O jogador joga com '{simbolo}'.")
    print(tabuleiro_para_str(tabuleiro))
    if jog == 1: # se jog for igual a 1, começa
        while not eh_fim_jogo(tabuleiro, k):
            jogada = escolhe_posicao_manual(tabuleiro)
            tabuleiro = marca_posicao(tabuleiro, jogada, jog)
            print(tabuleiro_para_str(tabuleiro))
            if verifica_k_linhas(tabuleiro, jogada, jog, k):
                print('VITORIA')
                return 1
            if obtem_posicoes_livres(tabuleiro) == ():
                print('EMPATE')
                return 0

            print(f'Turno do computador ({lvl}):')
            jogada = escolhe_posicao_auto(tabuleiro, -1, k, lvl)
            tabuleiro = marca_posicao(tabuleiro, jogada, -1)
            print(tabuleiro_para_str(tabuleiro))
            if verifica_k_linhas(tabuleiro, jogada, -jog, k):
                print('DERROTA')
                return -1
            if obtem_posicoes_livres(tabuleiro) == ():
                print('EMPATE')
                return 0
    if jog == -1: #se jog for igual a -1, o computador começa
        while not eh_fim_jogo(tabuleiro, k):
            print(f'Turno do computador ({lvl}):')
            jogada = escolhe_posicao_auto(tabuleiro, 1, k, lvl)
            tabuleiro = marca_posicao(tabuleiro, jogada, 1)
            print(tabuleiro_para_str(tabuleiro))
            if obtem_posicoes_livres(tabuleiro) == ():
                print('EMPATE')
                return 0
            if eh_fim_jogo(tabuleiro, k):
                print('DERROTA')
                return 1
            jogada = escolhe_posicao_manual(tabuleiro)
            tabuleiro = marca_posicao(tabuleiro, jogada, jog)
            print(tabuleiro_para_str(tabuleiro))
            if obtem_posicoes_livres(tabuleiro) == ():
                print('EMPATE')
                return 0
            if eh_fim_jogo(tabuleiro, k):
                print('VITORIA')
                return -1
