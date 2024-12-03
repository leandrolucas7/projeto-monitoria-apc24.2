def main():
    ### COLETAR INFORMAÇÕES GERAIS ###
    info = input()
    cargo = get_cargo(info)
    responsavel = get_responsavel(info)
    semestre = get_semestre(info)
    ano = get_ano(info)
    local = get_local(info)

    ### LISTAS PARA ARMAZENAMENTO ###
    info = [cargo, responsavel, semestre, ano, local]
    coordenadores = []
    professores = []
    alunos = []
    turmas = []

    ### COLETAR DADOS PESSOAIS ###
    CATEGORIAS = ["COORDENADORES", "PROFESSORES", "ALUNOS"]
    for _ in range(len(CATEGORIAS)):
        tipo = input()
        # Os inputs da categoria encerram com a palavra 'fim'
        dados = input()
        while dados != "fim":
            dados = dados.split(",")
            # Decifrar dados privados (Matrícula e Nome)
            # Coordenadores e professores tem uma camada extra de segurança (Cifra de Substituição)
            if tipo == CATEGORIAS[0] or tipo == CATEGORIAS[1]:
                dados[0] = criptografia_substituicao(dados[0])
                dados[1] = criptografia_substituicao(dados[1])
            # Criptografia Geral (Cifra de César). O último dígito da matrícula é o fator de rotação 
            # O último dígito da matrícula deve ser mantido
            rotacao = int(dados[0][-1])
            dados[0] = criptografia_cesar(dados[0], -rotacao)
            dados[0] = dados[0][:-1] + str(rotacao)
            dados[1] = criptografia_cesar(dados[1], -rotacao)

            # Adidionar sub-lista para turmas e horários
            dados.append([])
            dados.append([])
            # Adidionar listas com informações pessoais as 'super' listas correspondentes
            if tipo == CATEGORIAS[0]:
                # Remover sub-lista de horários do coordenador
                dados.pop()
                coordenadores.append(dados)
            elif tipo == CATEGORIAS[1]:
                professores.append(dados)
            elif tipo == CATEGORIAS[2]:
                alunos.append(dados)
            dados = input()

    ### INICIAR SISTEMA DE AÇÕES ###
    # Tipos de inputs:
        # Encerramento: "FIM"
        # Validação: POSIÇÃO AÇÃO MATRÍCULA
    # Posições válidas: "C" (Coordenador) "P" (Professor), "A" (Aluno)
    posicoes_validas = ["C", "P", "A"]
    acoes_validas = ["m", "i"]
    validacao = input()
    while validacao != "FIM":
        posicao, acao, matricula = validacao.split()
        # Verificar válidade da posição e ação
        if not posicao in posicoes_validas:
            imprimir_erro("Posicao", posicao)
        elif not acao in acoes_validas:
            imprimir_erro("Acao", acao)
        # Passar execução para as funções de controle
        elif posicao == "C":
            #controlador_coordenador(acao, matricula, coordenadores, turmas, info)
            controlador("Coordenador", acao, matricula, coordenadores, turmas, info)
        elif posicao == "P":
            #controlador_professor(acao, matricula, professores, turmas, info)
            controlador("Professor", acao, matricula, professores, turmas, info)
        elif posicao == "A":
            #controlador_aluno(acao, matricula, alunos, turmas, info)
            controlador("Aluno", acao, matricula, alunos, turmas, info)
        validacao = input()


# FUNÇÕES DE BUSCA / INSERÇÃO --------------------------------------------------------- #

# O cargo será sempre a segunda palavra do input inicial
# Sempre haverá uma vírgula após o cargo
def get_cargo(s:str)->str:
    palavras = s.split()[1]
    return palavras[:-1]


# O responsável sempre estará imediatamente atrás da segunda vírgula do input inicial
# O nome do responsável sempre possuirá duas palavras
def get_responsavel(s:str)->str:
    trecho = s.split(",")[1]
    nomes = trecho.split()[-2:]
    return " ".join(nomes)


# A primeira ocorrência da palavra 'primeiro' ou 'segundo' (não necessariamente todo minúsculo) anterior a sigla representa o semestre
# Tratar o primeiro semestre como 0 e o segundo como 1
def get_semestre(s:str)->int:
    i = get_posicao_sigla(s)
    primeiro = s.lower()[:-i].rfind("primeiro")
    segundo = s.lower()[:-i].rfind("segundo")
    return 1 if segundo > primeiro else 0


# A primeira ocorrência de números anterior a sigla é garantida de ser um ano com 4 digitos
def get_ano(s:str)->int:
    i = get_posicao_sigla(s)
    while not s[i].isdigit():
        i -= 1
    ano = int(s[i-3:i+1])
    return ano


# Garantido que após a sigla haverá um '-'. As palavras após o '-' serão o local
# Poderá haver um '-' dentro do nome do local
# O último caractere do local é alfanumérico
def get_local(s:str)->str:
    i = get_posicao_sigla(s)
    while s[i] != "-":
        i += 1
    local = s[i+1:].strip()
    return local if local[-1].isalnum() else local[:-1]


# É garantido que a última ocorrência de uma sigla (de no mínimo 2 letras) em caixa alta e entre aspas duplas é a sigla
def get_posicao_sigla(s:str)->int:
    while True:
        ultima_aspas = s.rfind('"')
        contagem = 0
        while s[ultima_aspas - contagem - 1].isupper():    
            contagem += 1
        if contagem >= 2 and s[ultima_aspas - contagem - 1]:
            return ultima_aspas - contagem - 1


def busca_2d(elemento:str, l:list, sub_posicao:int)->list:
    for sub_lista in l:
        if elemento == sub_lista[sub_posicao]:
            return sub_lista
    return []


def insercao_binaria(item:str, itens:list)->int:
    baixo = 0 
    alto = len(itens)
    while baixo < alto:
        meio = (baixo + alto) // 2 
        if item.lower() > itens[meio].lower():
            baixo = meio + 1
        else:
            alto = meio
    return baixo


def busca_binaria(item:str, itens:list, baixo:int, alto)->int:
    if baixo > alto:
        return -1

    meio = (baixo + alto) // 2 
    if item.lower() == itens[meio].lower():
        return meio
    elif item.lower() > itens[meio].lower():
        busca_binaria(item, itens, meio+1, alto)
    else:
        busca_binaria(item, itens, baixo, meio-1)

# ------------------------------------------------------------------------------------- #


# FUNÇÕES DE CONTROLE ----------------------------------------------------------------- #

def controlador(posicao:str, acao:str, matricula:str, pessoas:list, turmas:list, info:list)->None:
    # Verificar existência da pessoa com base na posição/matrícula recebida
    pessoa = busca_2d(matricula, pessoas, 0)
    if not pessoa:
        imprimir_erro("Matrícula", matricula)
        return

    # Executar ações com base no chamador correto
    if acao == "i":
        imprimir_turmas(pessoa, posicao, info)
    elif acao == "m":
        if posicao.lower()  == "coordenador":
            turma = montar_turma(pessoa)
            nomes_das_turmas = [item[0] for item in turmas]
            turmas.insert(insercao_binaria(turma[0], nomes_das_turmas), turma)
        elif posicao.lower() == "professor":
            turma = ministrar_turma(pessoa, turmas)
        elif posicao.lower() == "aluno":
            turma = matricular_turma(pessoa, turmas)



def controlador_coordenador(acao:str, matricula:str, coordenadores:list, turmas:list, info:list)->None:
    # Verificar existência do coordenador
    coordenador = busca_2d(matricula, coordenadores, 0)
    if not coordenador:
        imprimir_erro("Matricula", matricula)
        return
    # Executar ação
    if acao == "i":
        imprimir_turmas(coordenador, "Coordenador", info)
    elif acao == "m":
        turma = montar_turma(coordenador)
        nomes_das_turmas = [item[0] for item in turmas]
        turmas.insert(insercao_binaria(turma[0], nomes_das_turmas), turma)


def controlador_professor(acao:str, matricula:str, professores:list, turmas:list, info:list)->None:
    professor = busca_2d(matricula, professores, 0)
    if not professor:
        imprimir_erro("Matricula", matricula)
        return
    if acao == "i":
        imprimir_turmas(professor, "Professor", info)
    elif acao == "m":
        turma = ministrar_turma(professor, turmas)


def controlador_aluno(acao:str, matricula:str, alunos:list, turmas:list, info:list)->None:
    aluno = busca_2d(matricula, alunos, 0)
    if not aluno:
        imprimir_erro("Matricula", matricula)
        return
    if acao == "i":
        imprimir_turmas(aluno, "Aluno", info)
    elif acao == "m":
        turma = matricular_turma(aluno, turmas)

# ------------------------------------------------------------------------------------- #


# FUNÇÕES DE AÇÕES -------------------------------------------------------------------- #
def imprimir_turmas(pessoa:list, posicao:str, info:list)->None:
    imprimir_cabecalho(info[4], pessoa[2], pessoa[1], posicao)
    contador = 0
    for turma in pessoa[3]:
        if validar_turma(turma):
            contador += 1
            print()
            print(f"{contador}- {turma[0].upper()}")
            print(f"--> Professor(a): {turma[3]}")
            print(f"--> Horario: {'/'.join(turma[5])}")
            print(f"--> Matriculados: {len(turma[4])} aluno(s)")
    print()
    print(f"==> {contador} turmas ativa(s).")
    print()
    imprimir_rodape(info[1], info[0], info[3], info[2])


def montar_turma(coordenador:list)->list:
    nome, dias, requisito = input().split(",")
    dias = dias.split("/") # Ex: ['seg', 'qua']...
    # Nome, Departamento, Coordenador, Professor, Alunos, Dias, Requisitos
    turma = [nome, coordenador[2], coordenador[1], None, [], dias, requisito]
    # Inserir turma de forma ordenada na lista de turmas do coordenador
    turmas = coordenador[3]
    nomes_das_turmas = [item[0] for item in turmas]
    turmas.insert(insercao_binaria(nome, nomes_das_turmas), turma)
    return turma

def ministrar_turma(professor:list, turmas:list)->list:
    nome_da_turma = input()
    # Verificar existência da turma
    nomes_das_turmas = [item[0] for item in turmas]
    indice_turma = busca_binaria(nome_da_turma, nomes_das_turmas, 0, len(nomes_das_turmas))
    if indice_turma == -1:
        print("turma não existe") # Consertar mensagem de erro
        return []
    
    turma = turmas[indice_turma]
    # Verificar se departamentos são iguais
    if professor[2].lower() != turma[1].lower():
        print("professor não está no departamento da turma") # Consertar mensagem de erro
        return []
    # Verificar se turma já tem professor
    if turma[3]:
        print("turma já tem professor") # Consertar mensagem de erro
        return []
    # Verificar dias da turma
    if not dias_compativeis(professor[4], turma[5]):
        print("Conflito de datas") # Consertar mensagem de erro
        return []
    
    # Operação válida
    turma[3] = professor[1]
    professor[4] += turma[5]
    professor[3].append(turma)
    return turma


def matricular_turma(aluno:list, turmas:list)->list:
    nome_da_turma = input()
    # Verificar existência da turma
    nomes_das_turmas = [item[0] for item in turmas]
    indice_turma = busca_binaria(nome_da_turma, nomes_das_turmas, 0, len(nomes_das_turmas))
    if indice_turma == -1:
        print("turma não existe") # Consertar mensagem de erro
        return []
    
    turma = turmas[indice_turma]
    # Verificar se departamentos são iguais
    if aluno[2].lower() != turma[1].lower():
        print("aluno não está no departamento da turma") # Consertar mensagem de erro
        return []
    # Verificar se turma já tem professor
    if not turma[3]:
        print("turma não tem professor") # Consertar mensagem de erro
        return []
    # Verificar dias da turma
    if not dias_compativeis(aluno[4], turma[5]):
        print("Conflito de datas") # Consertar mensagem de erro
        return []
    
    # Operação válida
    turma[4].append(aluno[1])
    aluno[4] += turma[5]
    aluno[3].append(turma)
    return turma
# ------------------------------------------------------------------------------------- #


# FUNÇÕES DE VALIDAÇÃO ---------------------------------------------------------------- #

def criptografia_cesar(s:str, rotacao:int)->str:
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    resultado = ""
    for c in s:
        if c.isalpha():
            maiusclulo = c.isupper()
            i = alfabeto.index(c.lower())
            i = (i + rotacao) % len(alfabeto)
            resultado += alfabeto[i] if not maiusclulo else alfabeto[i].upper()
        elif c.isdigit():
            i = digitos.index(c)
            i = (i + rotacao) % len(digitos)
            resultado += digitos[i]
        else:
            resultado += c
    return resultado


def criptografia_substituicao(s:str)->str:
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    resultado = ""
    for c in s:
        if c.isalpha():
            maiusclulo = c.isupper()
            i = alfabeto.index(c.lower())
            i = len(alfabeto) - i - 1 
            resultado += alfabeto[i] if not maiusclulo else alfabeto[i].upper()
        elif c.isdigit():
            i = digitos.index(c)
            i = len(digitos) - i - 1 
            resultado += digitos[i]
        else:
            resultado += c
    return resultado


def validar_turma(turma:list)->bool:
    # Existe professor e aluno na turma
    return turma[3] and len(turma[4]) > 0


def dias_compativeis(reservado:list, novo:list)->bool:
    for dia in novo:
        if dia in reservado:
            return False
    return True

# ------------------------------------------------------------------------------------- #


# FUNÇÕES DE IMPRESSÃO --------------------------------------------------------------------- #

def imprimir_erro(tipo:str, arg:str)->None:
    print(f"{tipo} '{arg}' invalido(a).")


def imprimir_cabecalho(local:str, departamento:str, nome:str, posicao:str)->None:
    print(">>>>>")
    print(local.upper())
    print(f"Departamento {departamento}")
    print(f"[{posicao.capitalize()}(a): {nome}]")


def imprimir_rodape(nome:str, cargo:str, ano:str, semestre:str)->None:
    print(f'"{nome.title()} - {cargo.capitalize()} ({ano}.{semestre})"')
    print("<<<<<")
# ------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()
