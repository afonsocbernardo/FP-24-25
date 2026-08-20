"""
Este projeto foi realizado no âmbito da UC, Fundamentos da Programação, pelo aluno Afonso Caliço Bernardo
(ist113820).
O projeto consiste numa adaptação do jogo comercial Orbito, um caso particular do jogo m,n,k. Neste projeto, o jogador poderá
alterar o número de órbitas, assim como pode escolher jogar com as pedras pretas ou brancas. No fim de cada turno, todas as
peças rodam uma posição em sentido anti-horário nas suas órbitas. O jogador tem ao seu dispor 3 tipos diferentes de modo de jogo:
facil (contra o computador de acordo com a estratégia fácil), normal (contra o computador de acordo com a estratégia fácil) e
2jogadores (contra outro jogador humano).
O jogo acaba quando pelo menos um dos jogadores obter uma linha (vertical, horizontal, diagonal) completa com as suas peças.
"""

"""2.1.1    #TAD posicao:
-Construtores:
cria_posicao: str x inteiro --> posicao

-Seletores:
obtem_pos_col: posicao --> st
obtem_pos_lin: posicao --> int

-Reconhecedores:
eh_posicao: universal --> booleano

-Teste:
posicoes_iguais: universal x universal --> booleano

-Transformadores:
posicao_para_str: posicao --> str
str_para_posicao: str --> posicao
"""
def cria_posicao(col, lin):
    """
    Recebe um caracter e um inteiro correspondentes à coluna e à linha
    e devolve a posição correspondente.
    cria_posicao: str x inteiro --> posicao
    """
    if not type(col) == str or not type(lin) == int or not \
            "a" <= col <= "j" or not 0 < lin <= 10 or not len(col) == 1:
        raise ValueError('cria_posicao: argumentos invalidos')
    return (col, lin)


def obtem_pos_col(p):
    """
    Recebe uma posição e devolve a coluna da posição.
    obtem_pos_col: posicao --> str
    """
    return p[0]


def obtem_pos_lin(p):
    """
    Recebe uma posição e devolve a linha da posição.
    obtem_pos_lin: posicao --> int
    """
    return int(p[1])


def eh_posicao(arg):
    """
    Recebe um argumento e devolve um booleano:
    True, se o argumento for um TAD posicao, ou False, caso contrário.
    eh_posicao: universal --> booleano
    """
    if type(arg) != tuple or len(arg) != 2 or type(arg[0]) != str or type(arg[1]) != int \
            or len(arg[0]) != 1 or not 1 <= arg[1] <= 10 or not 'a' <= arg[0] <= 'j':
        return False
    return True


def posicoes_iguais(p1, p2):
    """
    Recebe dois argumentos e devolve um booleano:
    True, se os dois argumentos forem posições e forem posições iguais, ou False, caso contrário.
    posicoes_iguais: universal x universal --> booleano
    """
    #A posição é igual se as colunas e as linhas forem iguais
    return obtem_pos_col(p1) == obtem_pos_col(p2) and obtem_pos_lin(p1) == obtem_pos_lin(p2)


def posicao_para_str(p):
    """
    Recebe um tuplo que representa a posição e devolve a cadeia de caracteres.
    posicao_para_str: posicao --> str
    """
    return str(p[0]) + str(p[1])


def str_para_posicao(s):
    """
    Recebe uma cadeia de caracteres e devolve um tuplo que representa a posição.
    str_para_posicao: str --> posicao
    """
    return (s[0], int(s[1:]))

"""
Funções de alto nível TAD posicao
"""

def eh_posicao_valida(p, n):
    """
    Recebe uma posição e um n que determina o número de orbitas do tabuleiro e devolve um booleano:
    True, se é uma posição válida do tabuleiro, ou False, caso contrário.
    eh_posicao_valida: posicao x inteiro --> booleano
    """
    return (ord("a") <= ord(obtem_pos_col(p)) <= ord("a") + 2 * n - 1 and \
            1 <= obtem_pos_lin(p) <= 2 * n)


def obtem_posicoes_adjacentes(p, n, d):
    """
    Recebe uma posição, um inteiro positivo n, correspondente às orbitas, e um booleano:
    Se o booleano for True, devolve um tuplo com as posições adjacentes.
    Se o booleano for False, devolve um tuplo com as posições adjacentes ortogonais.
    obtem_posicoes_adjacentes: posicao x inteiro x booleano --> tuplo
    """
    coluna = obtem_pos_col(p)
    linha = obtem_pos_lin(p)
    #Para as adjacentes
    if d:
        adjacentes = ()
        #Cria um tuplo que tem todas as "posições" adjacentes a p (até aquelas que não são posições válidas)
        todas_adjacentes = (coluna + str(linha - 1), chr(ord(coluna) + 1) + str(linha - 1), chr(ord(coluna) + 1) + str(linha), \
        chr(ord(coluna) + 1) + str(linha + 1), coluna + str(linha + 1),
        chr(ord(coluna) - 1) + str(linha + 1), chr(ord(coluna) - 1) + str(linha), \
        chr(ord(coluna) - 1) + str(linha - 1))
        #Das "posições criadas, verifica apenas as que são válidas para o tabuleiro"
        for pos in todas_adjacentes:
            if eh_posicao_valida(pos, n):
                adjacentes = adjacentes + (pos,)
        return adjacentes
    #Para as adjacentes ortogonais
    if not d:
        adjacentes = ()
        todas_adjacentes = (coluna + str(linha - 1), chr(ord(coluna) + 1) + str(linha), \
                            coluna + str(linha + 1), chr(ord(coluna) - 1) + str(linha))
        for pos in todas_adjacentes:
            if eh_posicao_valida(pos, n):
                adjacentes = adjacentes + (pos,)
        return adjacentes


def ordena_posicoes(t, n):
    """
    Recebe um tuplo e um inteiro e devolve um tuplo de posições com as mesmas posições de t ordenadas
    de acordo com a ordem de leitura do tabuleiro de Orbito-n.
    ordena_posicoes: tuplo x inteiro --> tuplo
    """
    #Critério 1: As posições estão ordenadas da menor distância ao centro para a maior
    abcissa_centro = n + 0.5
    ordenada_centro = n + 0.5
    def dist(p):
        linha = obtem_pos_lin(p)
        coluna = ord(obtem_pos_col(p)) - 96
        d = max(abs(abcissa_centro - coluna), abs(ordenada_centro - linha))
        return d
    #Critério 2: Em caso de empate, as posições ficam ordenadas por linha (crescente)
    #Critério 3: Em caso de empate, as posições ficam ordenadas por ordem alfabética
    def ordena(p):
        return (dist(p), obtem_pos_lin(p), obtem_pos_col(p))
    return tuple(sorted(t, key=ordena))


"""2.1.2    #TAD pedra:
-Construtores:
cria_pedra_branca: {} --> pedra
cria_pedra_preta: {} --> pedra
cria_pedra_neutra: {} --> pedra

-Reconhecedor:
eh_pedra: universal --> booleano
eh_pedra_branca: pedra --> booleano
eh_pedra_preta: pedra --> booleano

-Teste:
pedras_iguais: universal x universal --> booleano

-Transformador:
pedra_para_str: pedra --> string
"""

def cria_pedra_branca():
    """
    Devolve a pedra pertencente ao jogador branco.
    cria_pedra_branca: {} --> pedra
    """
    return "O"


def cria_pedra_preta():
    """
    Devolve a pedra pertencente ao jogador preto.
    cria_pedra_preta: {} --> pedra
    """
    return "X"


def cria_pedra_neutra():
    """
    Devolve uma pedra neutra.
    cria_pedra_neutra: {} --> pedra
    """
    return " "


def eh_pedra(arg):
    """
    Recebe um argumento universal e devolve um booleano:
    True, se o argumento for um TAD pedra, ou False, caso contrário.
    eh_pedra: universal --> booleano
    """
    elementos = [' ', 'X', 'O'] 
    return arg in elementos


def eh_pedra_branca(p):
    """
    Recebe uma pedra e devolve um booleano:
    True, caso a pedra p for do jogador branco, ou False, caso contrário.
    eh_pedra_branca: pedra --> booleano
    """
    return p == cria_pedra_branca()


def eh_pedra_preta(p):
    """
    Recebe uma pedra e devolve um booleano:
    True, caso a pedra p for do jogador preto, ou False, caso contrário.
    eh_pedra_preta: pedra --> booleano
    """
    return p == cria_pedra_preta()


def pedras_iguais(p1, p2):
    """
    Recebe dois argumentos universais e devolve um booleano:
    True, caso os argumentos forem pedras e iguais, ou False, caso contrário.
    pedras_iguais: universal x universal --> booleano
    """
    return p1 == p2


def pedra_para_str(p):
    """
    Recebe uma pedra e devolve a cadeia de caracteres que representa o jogador dono da pedra.
    pedra_para_str: pedra --> string
    """
    return p

"""
Funções de alto nível TAD pedra
"""
def eh_pedra_jogador(p):
    """
    Recebe uma pedra e devolve um booleano:
    True, caso a pedra seja de um jogador, ou False, caso contrário.
    eh_pedra_jogador: pedra --> booleano
    """
    return eh_pedra_branca(p) or eh_pedra_preta(p)


def pedra_para_int(p):
    """
    Recebe uma pedra e devolve um inteiro (1, -1, 0), dependendo se
    a pedra for do jogador preto, branco, ou neutra, respetivamente.
    pedra_para_int: pedra --> int
    """
    if eh_pedra_branca(p):
        return -1
    if eh_pedra_preta(p):
        return 1
    else:
        return 0


"""2.1.3    #TAD tabuleiro:
-Construtores:
cria_tabuleiro_vazio: int --> tabuleiro
cria_tabuleiro: int x tuplo x tuplo --> tabuleiro
cria_copia_tabuleiro: tabuleiro --> tabuleiro

-Seletores:
obtem_numero_orbitas: tabuleiro --> int
obtem_pedra: tabuleiro x posicao --> pedra
obtem_linha_horizontal: tabuleiro x posicao --> tuplo
obtem_linha_vertical: tabuleiro x posicao --> tuplo
obtem_linhas_diagonais: tabuleiro x posicao --> tuplo x tuplo
obtem_posicoes_pedra: tabuleiro x pedra --> tuplo

-Modificadores:
coloca_pedra: tabuleiro x posicao x pedra --> tabuleiro
remove_pedra: tabuleiro x posicao --> tabuleiro

-Reconhecedor:
eh_tabuleiro: universal --> booleano

-Teste:
tabuleiro_iguais: universal x universal --> booleano

-Transformador:
tabuleiro_para_str: tabuleiro --> str
"""

def cria_tabuleiro_vazio(n):
    """
    Recebe um inteiro correspondente ao número de órbitas, e devolve um tabuleiro sem posições ocupadas.
    cria_tabuleiro_vazio: int --> tabuleiro
    """
    if not 2 <= n <= 5:
        raise ValueError("cria_tabuleiro_vazio: argumento invalido")
    tabuleiro = []
    #O tabuleiro é uma lista de listas
    for x in range(1, 2 * n + 1):
        tabuleiro.append([])
    for i in tabuleiro:
        for x in range(1, 2 * n + 1):
            i.append(cria_pedra_neutra()) #dentro das listas estão posições vazias
    return tabuleiro


def cria_tabuleiro(n, tp, tb):
    """
    Recebe um inteiro e dois tuplos de posições (um ocupado por pedras pretas o outro com brancas) e devolve um tabuleiro
    com as posições dos tuplos ocupadas pelas respetivas pedras.
    cria_tabuleiro: int x tuplo x tuplo --> tabuleiro
    """
    if not 2 <= n <= 5 or not type(n) == int or not type(tp) == tuple or not type(tb) == tuple:
        raise ValueError("cria_tabuleiro: argumentos invalidos")
    tabuleiro = cria_tabuleiro_vazio(n)
    pos_tp, pos_tb = [], []
    for i in tp:
        if not eh_posicao_valida(i, n): #as posições no tuplo têm de ser válidas
            raise ValueError("cria_tabuleiro: argumentos invalidos")
        if i in pos_tp: #não pode haver posições repetidas no tuplo
            raise ValueError("cria_tabuleiro: argumentos invalidos")
        if i in tb: #não pode haver posições no tuplo da outra pedra
            raise ValueError("cria_tabuleiro: argumentos invalidos")
        pos_tp.append(i)
        linha = obtem_pos_lin(i) - 1
        coluna = ord(obtem_pos_col(i)) - 97
        #Se a posição passou a todas as verificações, adiciona-se ao tabuleiro.
        tabuleiro[linha][coluna] = cria_pedra_preta()

    for i in tb:
        if not eh_posicao_valida(i, n): #as posições no tuplo têm de ser válidas
            raise ValueError("cria_tabuleiro: argumentos invalidos")
        if i in pos_tb: #não pode haver posições repetidas no tuplo
            raise ValueError("cria_tabuleiro: argumentos invalidos")
        pos_tb.append(i)
        linha = obtem_pos_lin(i) - 1
        coluna = ord(obtem_pos_col(i)) - 97
        #Se a posição passou a todas as verificações, adiciona-se ao tabuleiro.
        tabuleiro[linha][coluna] = cria_pedra_branca()

    return tabuleiro


def cria_copia_tabuleiro(t):
    """
    Recebe um tabuleiro e devolve uma cópia do tabuleiro.
    cria_copia_tabuleiro: tabuleiro --> tabuleiro
    """
    copia_tabuleiro = []
    for i in t:
        copia_tabuleiro.append(i.copy())
    return copia_tabuleiro


def obtem_numero_orbitas(t):
    """
    Recebe um tabuleiro e devolve uma cópia do tabuleiro.
    obtem_numero_orbitas: tabuleiro --> int
    """
    return int(len(t) / 2)


def obtem_pedra(t, p):
    """
    Recebe um tabuleiro e uma posição e devolve a pedra da posição.
    obtem_pedra: tabuleiro x posicao --> pedra
    """
    return t[obtem_pos_lin(p) - 1][ord(obtem_pos_col(p)) - 97]


def obtem_linha_horizontal(t, p):
    """
    Recebe um tabuleiro e uma posição e devolve um tuplo formado por tuplos de dois elementos correspondentes à posição e
    o valor de todas as posições da linha horizontal que passa pela posição p, ordenadas de cima para baixo.
    obtem_linha_horizontal: tabuleiro x posicao --> tuplo
    """
    tuplo = ()
    for i in range(1, 2 * obtem_numero_orbitas(t) + 1):
        posicao = cria_posicao(chr(96 + i), obtem_pos_lin(p))
        tuplo += ((posicao_para_str(posicao), obtem_pedra(t, posicao)),)
    return tuplo


def obtem_linha_vertical(t, p):
    """
    Recebe um tabuleiro e uma posição e devolve um tuplo formado por tuplos de dois elementos correspondentes à posição e
    o valor de todas as posições da linha vertical que passa pela posição p, ordenadas de cima para baixo.
    obtem_linha_vertical: tabuleiro x posicao --> tuplo
    """
    tuplo = ()
    for i in range(1, 2 * obtem_numero_orbitas(t) + 1):
        posicao = cria_posicao(obtem_pos_col(p), i)
        tuplo += ((posicao, obtem_pedra(t, posicao)),)
    return tuplo



def obtem_linhas_diagonais(t, p):
    """
    Recebe um tabuleiro e uma posição e devolve dois tuplos formados cada um deles por tuplos de dois elementos
    correspondentes à posição e o valor de todas as posições que formam a diagonal e antidiagonal que passam pela posição.
    obtem_linhas_diagonais: tabuleiro x posicao --> tuplo x tuplo
    """
    tuplo_diagonal, tuplo_antidiagonal = (), ()
    for i in range(len(t)):
        for x in range(len(t[i])):
            if cria_posicao(chr(ord('a')+i), x + 1) == p:
                l_pos, c_pos = i, x
    #Para diagonal
    #Para cima
    m, n = l_pos, c_pos
    orbitas = obtem_numero_orbitas(t)
    while m >= 0 and n >= 0:
        if cria_posicao(chr(ord('a')+m), n + 1) != p:
            pos = cria_posicao(chr(ord('a')+ m), n + 1)
            tuplo_diagonal += ((pos, obtem_pedra(t, pos)),)
        m -= 1
        n -= 1
    #Adicionar p
    tuplo_diagonal += ((p, obtem_pedra(t, p)),)
    #Para baixo
    m, n = l_pos, c_pos
    while m < 2 * orbitas and n < 2 * orbitas:
        if cria_posicao(chr(ord('a') + m), n + 1) != p:
            pos = cria_posicao(chr(ord('a')+ m), n + 1)
            tuplo_diagonal += ((pos, obtem_pedra(t, pos)),)
        m += 1
        n += 1
    #Para antidiagonal
    #Para cima
    m, n = l_pos, c_pos
    while m >= 0 and n < 2 * orbitas:
        if cria_posicao(chr(ord('a') + m), n + 1) != p:
            pos = cria_posicao(chr(ord('a')+ m), n + 1)
            tuplo_antidiagonal += ((pos, obtem_pedra(t, pos)),)
        m -= 1
        n += 1
    #Adicionar p
    tuplo_antidiagonal += ((p, obtem_pedra(t, p)),)
    #Para baixo
    m, n = l_pos, c_pos
    while m < 2 * orbitas and n >= 0:
        if cria_posicao(chr(ord('a') + m), n + 1) != p:
            pos = cria_posicao(chr(ord('a')+ m), n + 1)
            tuplo_antidiagonal += ((pos, obtem_pedra(t, pos)),)
        m += 1
        n -= 1
    return tuple(sorted(tuplo_diagonal)), tuple(sorted(tuplo_antidiagonal))


def obtem_posicoes_pedra(t, j):
    """
    Recebe uma lista correspondente a um tabuleiro e uma string correspondente a uma pedra
    e devolve um tuplo formado por todas as posições do tabuleiro ocupadas por pedras j.
    obtem_posicoes_pedra: tabuleiro x pedra --> tuplo
    """
    tuplo = ()
    for i in range(len(t)):
        for x in range(len(t[i])):
            if t[i][x] == pedra_para_str(j):
                #Adiciona ao tuplo as posições que possuem a pedra j
                tuplo += (cria_posicao(chr(ord('a') + x), i+1),)
    return ordena_posicoes(tuplo, obtem_numero_orbitas(t))


def coloca_pedra(t, p, j):
    """
    Recebe um tabuleiro e uma posição e devolve o próprio tabuleiro, que foi modificado
    destrutivamente cololcando a pedra j na posição p.
    coloca_pedra: tabuleiro x posicao x pedra --> tabuleiro
    """
    t[obtem_pos_lin(p)-1][ord(obtem_pos_col(p))-97] = pedra_para_str(j)
    return t


def remove_pedra(t, p):
    """
    Recebe um tabuleiro e uma posição e devolve o próprio tabuleiro, que foi modificado
    destrutivamente removendo a pedra da posição p
    remove_pedra: tabuleiro x posicao --> tabuleiro
    """
    t[obtem_pos_lin(p) - 1][ord(obtem_pos_col(p)) - 97] = cria_pedra_neutra()


def eh_tabuleiro(arg):
    """
    Recebe um argumento de qualquer tipo e devolve um booleano:
    True, se o argumento for um TAD tabuleiro, ou False, caso contrário.
    eh_tabuleiro: universal --> booleano
    """
    pedras = [cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra()]
    if not type(arg) == list or not arg != [] or not len(arg) == len(arg[0]) or not type(arg[0]) == list:
        return False
    for i in arg:
        for x in i:
            if not type(x) == str:
                return False
            if x not in pedras:
                return False
    return True


def tabuleiros_iguais(t1, t2):
    """
    Recebe dois argumentos e devolve um booleano:
    True, se os dois argumentos forem tabuleiros e iguais, ou False, caso contrário.
    tabuleiro_iguais: universal x universal --> booleano
    """
    if not eh_tabuleiro(t1) or not eh_tabuleiro(t2):
        return False
    if not t1 == t2:
        return False
    return True


def tabuleiro_para_str(t):
    """
    Recebe um tabuleiro e devolve a cadeia de caracteres que representa o tabuleiro.
    tabuleiro_para_str: tabuleiro --> str
    """
    n = obtem_numero_orbitas(t)
    count, l, contador_lateral, t_string = 0, 0, 1, ""
    #Para o tabuleiro "estético", o número de linhas dá-se por 4*orbitas
    for linha in range(4 * n):
        c, i = 0, 1
        #Para o tabuleiro "estético", o número de colunas dá-se por 8*orbitas + 2
        for coluna in range(8 * n + 2):
            #Esta é a linha onde fica os índices das colunas
            if linha == 0:
                if coluna % 4 != 0 or coluna == 0:
                    t_string += ' '
                if coluna % 4 == 0 and coluna != 0:
                    letra = chr(ord('a') + count)
                    t_string += str(letra)
                    count += 1
            #Estas são as linhas onde ficam as pedras
            if linha % 2 != 0 and linha != 0:
                if coluna == 1 and linha != 19:
                    t_string += "0"
                if coluna == 2:
                    t_string += str(contador_lateral)
                    contador_lateral += 1
                #As pedras colocam-se nestas colunas
                if coluna % 4 == 0 and coluna != 0:
                    if t[l][c] == cria_pedra_neutra():
                        simbolo = pedra_para_str(cria_pedra_neutra())
                    if t[l][c] == cria_pedra_branca():
                        simbolo = pedra_para_str(cria_pedra_branca())
                    if t[l][c] == cria_pedra_preta():
                        simbolo = pedra_para_str(cria_pedra_preta())
                    t_string += f"[{simbolo}]"
                    c += 1
                if coluna == 4 * i + 2:
                    t_string += '-'
                    i += 1
                if coluna == 2:
                    t_string += ' '
            #Estas são as linhas onde ficam os espaçamentos
            if linha % 2 == 0 and linha != 0:
                if coluna % 4 == 0 and coluna != 0:
                    t_string += "|"
                else:
                    t_string += " "
        if linha % 2 != 0: #só incrementa o l quando for uma linha para colocar as posições
            l += 1 
        else: #tira espaçamentos
            t_string = t_string[:-1]
        t_string += "\n"
    t_string = t_string[:-1]
    return t_string

"""
Funções de alto nível TAD tabuleiro
"""
def move_pedra(t, p1, p2):
    """
    Recebe um tabuleiro e duas posições e devolve o próprio tabuleiro que foi
    modificado destrutivamente movendo uma pedra de p1 para p2.
    move_pedra: tabuleiro x posicao x posicao --> tabuleiro
    """
    coloca_pedra(t, p2, obtem_pedra(t, p1))
    remove_pedra(t, p1)
    return t


def obtem_orbita(t, p):
    """
    Recebe um tabuleiro e uma posicao e devolve um tuplo com todas as posições dessa órbita.
    obtem_orbita: tabuleiro x posicao --> tuplo
    """
    n = obtem_numero_orbitas(t)
    tuplo = ()
    abcissa_centro = n + 0.5
    ordenada_centro = n + 0.5
    linha = obtem_pos_lin(p)
    coluna = ord(obtem_pos_col(p)) - 96
    d = max(abs(abcissa_centro - linha), abs(ordenada_centro - coluna))
    for i in range(len(t) + 1):
        for x in range(len(t[0]) + 1):
            if max(abs(abcissa_centro - x), abs(ordenada_centro - i)) == d:
                tuplo += (posicao_para_str(cria_posicao(chr(96 + x), i)),)
    return tuplo


def obtem_posicao_seguinte(t, p, s):
    """
    Recebe um tabuleiro, uma posicao e um booleano e devolve a posicao da mesma órbita que p que se encontra a seguir no tabuleiro:
    Em sentido horário, se o booleano for True, em sentido anti-horário, caso o booleano for False.
    obtem_posicao_seguinte: tabuleiro x posicao x booleano --> posicao
    """
    n = obtem_numero_orbitas(t)
    posicoes_orbita = obtem_orbita(t, p)
    tuplo_comum = ()
    posicoes_ortogonais = obtem_posicoes_adjacentes(p, n, False)
    linha = obtem_pos_lin(cria_posicao(posicoes_orbita[0][0], int(posicoes_orbita[0][1:])))
    coluna = obtem_pos_col(cria_posicao(posicoes_orbita[0][0], int(posicoes_orbita[0][1:])))
    for i in posicoes_ortogonais: #percorre todas as posições adjacentes
        if i in posicoes_orbita: #verifica se a posição está na órbita
            tuplo_comum += (i,)
    if s: #Sentido horário
        if obtem_pos_lin(p) == linha or obtem_pos_col(p) == coluna:
            return tuplo_comum[0]
        else:
            return tuplo_comum[-1]
    else: #Sentido antihorário
        if obtem_pos_lin(p) == linha or obtem_pos_col(p) == coluna:
            return tuplo_comum[-1]
        else:
            return tuplo_comum[0]


def roda_tabuleiro(t):
    """
    Recebe um tabuleiro e devolve o próprio tabuleiro modificado em que todas
    as pedras de uma posição foram rodadas em sentido anti-horário.
    roda_tabuleiro: tabuleiro --> tabuleiro
    """
    copia = cria_copia_tabuleiro(t)
    c = 0
    #Percorre todas as posições por orbitas
    for i in range(obtem_numero_orbitas(t)):
        for x in obtem_orbita(t, cria_posicao(chr(ord('a') + c), 1 + c)):
            pedra_seguinte = obtem_pedra(copia, obtem_posicao_seguinte(copia, x, True))
            coloca_pedra(t, x, pedra_seguinte)
        c += 1
    return t


def tabuleiro_posicoes(t):
    """
    Recebe um tabuleiro e devolve um tabuleiro com as posições.
    tabuleiro_posicoes: tabuleiro --> tabuleiro
    """
    tabuleiro_novo = []
    linha_pos = 0
    for i in range(len(t)):
        linha = []
        linha_pos += 1
        coluna_pos = 0
        for x in t[i]:
            linha = linha + [posicao_para_str(cria_posicao(chr(ord('a')+coluna_pos), linha_pos))]
            coluna_pos += 1
        tabuleiro_novo.append(linha)
    return tabuleiro_novo


def verifica_linha_pedras(t, p, j, k):
    """
    Recebe um tabuleiro, uma posição, uma pedra e um inteiro e devolve um booleano:
    True, se existe pelo menos uma linha (vertical, horizontal ou diagonal) que contenha a posição p com k 
    ou mais pedras consecutivas do jogador com pedras j, ou False, caso contrário.
    verifica_linha_pedras: tabuleiro x posicao x pedra x int --> booleano
    """
    if not obtem_pedra(t, p) == j:
        return False
    if k == 1:
        return True
    n = obtem_numero_orbitas(t)
    n_linhas_coluna = 2 * n
    tab = tabuleiro_posicoes(t)
    l_pos, c_pos = 0, 0
    for i in range(len(tab)):
        for x in range(len(t[i])):
            if posicao_para_str(p) == tab[i][x]:
                l_pos = i
                c_pos = x
    #Em coluna para baixo
    count = 1
    m = l_pos
    n = c_pos
    while m < n_linhas_coluna - 1:
        if t[m][n] == t[m+1][n]:
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
        if t[m][n] == t[m-1][n]:
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
    while n < n_linhas_coluna - 1:
        if t[m][n] == t[m][n+1]:
            count += 1
            if count == k:
                return True
        else:
            break
        n+= 1
    #Em linha para trás
    m = l_pos
    n = c_pos
    while n > 0:
        if t[m][n] == tab[m][n-1]:
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
    while m < (n_linhas_coluna - 1) and n < (n_linhas_coluna - 1):
        if t[m][n] == t[m+1][n+1]:
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
        if t[m][n] == t[m-1][n-1]:
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
    while m > 0 and n < (n_linhas_coluna - 1):
        if t[m][n] == t[m-1][n+1]:
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
    while m < (n_linhas_coluna - 1) and n > 0:
        if t[m][n] == t[m+1][n-1]:
            count += 1
            if count == k:
                return True
        else:
            break
        m += 1
        n -= 1
    return False

"""
Funções adicionais
"""
 

def eh_vencedor(t, j):
    """
    Recebe um tabuleiro e uma pedra de jogador, e devolve um booleano:
    True, se existe uma linha completa do tabuleiro de pedras do jogador, ou False, caso contrário.
    eh_vencedor: tabuleiro x pedra --> booleano
    """
    pos = 0
    n = obtem_numero_orbitas(t)
    #Para as linhas
    for i in range(2 * n):
        pos = cria_posicao('a', i + 1)
        if verifica_linha_pedras(t, pos, j, 2 * n):
            return True
    #Para as colunas
    for i in range(2* n):
        pos = cria_posicao(chr(ord('a') + i), 1)
        if verifica_linha_pedras(t, pos, j, 2 * n):
            return True
    return False


def eh_fim_jogo(t):
    """
    Recebe um tabuleiro e devolve um booleano:
    True, se o jogo terminou, ou False, caso contrário.
    eh_fim_jogo: tabuleiro --> booleano
    """
    tab = tabuleiro_posicoes(t)
    #Caso um dos jogadores seja vencedor, o jogo acabou
    if eh_vencedor(t, cria_pedra_preta()) or eh_vencedor(t, cria_pedra_branca()):
        return True
    for i in tab:
        for x in i:
            #Se não houver vencedor e houver pelo menos 1 posição com pedra neutra, o jogo não acabou
            if obtem_pedra(t, cria_posicao(x[0], int(x[1:]))) == cria_pedra_neutra():
                return False
    return True


def escolhe_movimento_manual(t):
    """
    Recebe um tabuleiro e permite escolher uma posição livre do tabuleiro (devolve uma string da posição).
    escolhe_movimento_manual: tabuleiro --> posicao
    """
    # Enquanto o jogador não escolher uma posição vazia, vai estar sempre a repetir o input.
    pos = 0
    orbita = obtem_numero_orbitas(t)
    while pos == 0 or eh_pedra_jogador(obtem_pedra(t, pos)):
        n = input('Escolha uma posicao livre:')
        if n[1:].isdigit() and 1 <= int(n[1:]) <= 10 and 'a' <= n[0] <= 'j':
            pos = cria_posicao(n[0], int(n[1:]))
            if not eh_posicao_valida(pos, orbita):
                pos = 0
    return pos


def estrategia_facil(t, j):
    """
    Recebe um tabuleiro e uma pedra identificando o jogador e devolve a melhor posição de acordo 
    com as regras estabelecidas na estratégia fácil.
    estrategia_facil: tabuleiro x pedra --> posicao
    """
    tab, t_adjacentes, t_adjcentes_ind, t_adjacentes_vazias  = tabuleiro_posicoes(t), (), (), ()
    n = obtem_numero_orbitas(t)
    #Todas as posições adjacentes às posições
    for i in tab:
        for x in i:
            if obtem_pedra(t, cria_posicao(x[0], int(x[1:]))) == j:
                t_adjacentes = t_adjacentes + (obtem_posicoes_adjacentes(x, n, True),)
    for i in t_adjacentes:
        for x in i:
            if x in t_adjcentes_ind:
                pass
            else:
                t_adjcentes_ind += (x,)
    #Todas as posições adjacentes que são vazias
    for pos in t_adjcentes_ind:
        if obtem_pedra(t, pos) == cria_pedra_neutra():
            t_adjacentes_vazias += (pos,)
    t_adjacentes_vazias = ordena_posicoes(t_adjacentes_vazias, n)
    if len(t_adjacentes_vazias) != 0:
        return t_adjacentes_vazias[0]
    #Se não houver posições adjacentes vazias
    for i in tab:
        for pos in i:
            t_adjacentes_vazias += (pos,)
    return ordena_posicoes(t_adjacentes_vazias, n)[0]


def escolhe_movimento_auto(t, j,lvl):
    """
    Recebe um tabuleiro, uma pedra e a cadeia de caracteres correspondente à estratégia,
    e devolve a posição escolhida automaticamente de acordo com as regras da respetiva estratégia.
    escolhe_movimento_auto: tabuleiro x pedra x str --> posicao
    """
    if lvl == 'facil':
        #escolhe a posição de acordo com a estratégia fácil
        return estrategia_facil(t, j)
    if lvl == 'normal':
        #escolhe a posição de acordo com a estratégia normal (não foi feito).
        pass


def orbito(n, modo, jog):
    """
    É a função principal que permite jogar um jogo completo de Orbito-n.
    Recebe um inteiro correspondente ao número de órbitas, uma cadeia de caracteres que representa o modo de jogo,
    e a representação externa de uma pedra,
    e devolve um inteiro identificando o jogador vencedor (1 para preto ou -1 para branco) ou 0 em caso de empate.
    orbito: int x str x str --> int
    """
    modos = ['facil', 'normal', '2jogadores']
    jogs = [pedra_para_str(cria_pedra_branca()), pedra_para_str(cria_pedra_preta())]
    if not 2 <= n <= 5 or not modo in modos or not jog in jogs:
        raise ValueError('orbito: argumentos invalidos')
    k = 2 * n
    t = cria_tabuleiro_vazio(n)
    print(f'Bem-vindo ao ORBITO-{n}.') #mensagem inicial
    if modo == '2jogadores':
        print('Jogo para dois jogadores.')
        print(tabuleiro_para_str(t))
        while True:
            #Turno do jogador 'X'
            print("Turno do jogador 'X'.")
            jogada = escolhe_movimento_manual(t)
            coloca_pedra(t, jogada, cria_pedra_preta())
            roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
            #Verifica se ambos os jogadores ganharam (e deu empate)
            if eh_vencedor(t, cria_pedra_preta()) and eh_vencedor(t, cria_pedra_branca()):
                print('EMPATE')
                return 0
            #Verifica se o jogador preto ganhou
            if eh_vencedor(t, cria_pedra_preta()):
                print("VITORIA DO JOGADOR 'X'")
                return 1
            #Verifica se o jogador branco ganhou
            if eh_vencedor(t, cria_pedra_branca()):
                print("VITORIA DO JOGADOR 'O'")
                return -1
            #Verifica se o jogo já acabou e não houve vencedor
            if eh_fim_jogo(t) and not eh_vencedor(t, cria_pedra_preta()) and not eh_vencedor(t, cria_pedra_branca()):
                print('EMPATE')
                return 0
            #Turno do jogador 'O'
            print("Turno do jogador 'O'.")
            jogada = escolhe_movimento_manual(t)
            coloca_pedra(t, jogada, cria_pedra_branca())
            roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
            # Verifica se ambos os jogadores ganharam (e deu empate)
            if eh_vencedor(t, cria_pedra_preta()) and eh_vencedor(t, cria_pedra_branca()):
                print('EMPATE')
                return 0
            #Verifica se o jogador preto ganhou
            if eh_vencedor(t, cria_pedra_preta()):
                print("VITORIA DO JOGADOR 'X'")
                return 1
            #Verifica se o jogador branco ganhou
            if eh_vencedor(t, cria_pedra_branca()):
                print("VITORIA DO JOGADOR 'O'")
                return -1
            #Verifica se o jogo já acabou e não houve vencedor
            if eh_fim_jogo(t) and not eh_vencedor(t, cria_pedra_preta()) and not eh_vencedor(t, cria_pedra_branca()):
                print('EMPATE')
                return 0
    if modo == 'facil' or modo == 'normal':
        if jog == 'X':
            print(f'Jogo contra o computador ({modo}).')
            print(f'O jogador joga com {pedra_para_str(jog)}.')
            print(tabuleiro_para_str(t))
            while True:
                #Turno do jogador
                print('Turno do jogador.')
                jogada = escolhe_movimento_manual(t)
                coloca_pedra(t, jogada, cria_pedra_preta())
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
                # Verifica se ambos os jogadores ganharam (e deu empate)
                if eh_vencedor(t, cria_pedra_preta()) and eh_vencedor(t, cria_pedra_branca()):
                    print('EMPATE')
                    return 0
                #Verifica se o jogador ganhou
                if eh_vencedor(t, cria_pedra_preta()):
                    print("VITORIA")
                    return 1
                #Verifica se o computador ganhou
                if eh_vencedor(t, cria_pedra_branca()):
                    print("DERROTA")
                    return -1
                # Verifica se o jogo já acabou e não houve vencedor
                if eh_fim_jogo(t) and not eh_vencedor(t, cria_pedra_preta()) and not eh_vencedor(t, cria_pedra_branca()):
                    print('EMPATE')
                    return 0
                #Turno computador
                print(f'Turno do computador ({modo}):')
                jogada = escolhe_movimento_auto(t, cria_pedra_branca(), modo)
                coloca_pedra(t, jogada, cria_pedra_branca())
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
                # Verifica se ambos os jogadores ganharam (e deu empate)
                if eh_vencedor(t, cria_pedra_preta()) and eh_vencedor(t, cria_pedra_branca()):
                    print('EMPATE')
                    return 0
                # Verifica se o jogador ganhou
                if eh_vencedor(t, cria_pedra_preta()):
                    print("VITORIA")
                    return 1
                # Verifica se o computador ganhou
                if eh_vencedor(t, cria_pedra_branca()):
                    print("DERROTA")
                    return -1
                # Verifica se o jogo já acabou e não houve vencedor
                if eh_fim_jogo(t) and not eh_vencedor(t, cria_pedra_preta()) and not eh_vencedor(t,cria_pedra_branca()):
                    print('EMPATE')
                    return 0
        if jog == 'O':
            print(f'Jogo contra o computador ({modo}).')
            print(f"O jogador joga com '{pedra_para_str(jog)}'.")
            print(tabuleiro_para_str(t))
            while True:
                #Turno computador
                print(f'Turno do computador ({modo}):')
                jogada = escolhe_movimento_auto(t, cria_pedra_preta(), modo)
                coloca_pedra(t, jogada, cria_pedra_preta())
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
                # Verifica se ambos os jogadores ganharam (e deu empate)
                if eh_vencedor(t, cria_pedra_preta()) and eh_vencedor(t, cria_pedra_branca()):
                    print('EMPATE')
                    return 0
                # Verifica se o computador ganhou
                if eh_vencedor(t, cria_pedra_preta()):
                    print("DERROTA")
                    return 1
                # Verifica se o jogador ganhou
                if eh_vencedor(t, cria_pedra_branca()):
                    print("VITORIA")
                    return -1
                # Verifica se o jogo já acabou e não houve vencedor
                if eh_fim_jogo(t) and not eh_vencedor(t, cria_pedra_preta()) and not eh_vencedor(t, cria_pedra_branca()):
                    print('EMPATE')
                    return 0
                #Turno jogador
                print('Turno do jogador.')
                jogada = escolhe_movimento_manual(t)
                coloca_pedra(t, jogada, cria_pedra_branca())
                roda_tabuleiro(t)
                print(tabuleiro_para_str(t))
                # Verifica se ambos os jogadores ganharam (e deu empate)
                if eh_vencedor(t, cria_pedra_preta()) and eh_vencedor(t, cria_pedra_branca()):
                    print('EMPATE')
                    return 0
                #Verifica se o computador ganhou
                if eh_vencedor(t, cria_pedra_preta()):
                    print("DERROTA")
                    return 1
                #Verifica se o jogador ganhou
                if eh_vencedor(t, cria_pedra_branca()):
                    print("VITORIA")
                    return -1
                # Verifica se o jogo já acabou e não houve vencedor
                if eh_fim_jogo(t) and not eh_vencedor(t, cria_pedra_preta()) and not eh_vencedor(t, cria_pedra_branca()):
                    print('EMPATE')
                    return 0
