def main():
    ### CONSTANTES ###
    POSICOES = ["Coordenador", "Professor", "Aluno"]
    ACOES = ["m", "i"]

    ### COLETAR INFORMAÇÕES GERAIS ###
    info = input()
    cargo = get_cargo(info)
    responsavel = get_responsavel(info)
    semestre = get_semestre(info)
    ano = get_ano(info)
    local = get_local(info)

    ### LISTAS PARA ARMAZENAMENTO ###
    info = [cargo, responsavel, semestre, ano, local]
    # coordenador: ["matricula", "nome", "departamento", "posição", [turma]]
    coordenadores = []
    # professor: ["matricula", "nome", "departamento", "posição", [turma], ["seg", "qua"]]
    professores = []
    # aluno: ["matricula", "nome", "departamento", "posição", [turma], ["seg", "qui"]]
    alunos = []
    # turma: ["nome", "departamento", coordenador, professor, [aluno, aluno, ...], ["seg", "sex"]]
    turmas = []

    ### COLETAR / DECIFRAR DADOS PESSOAIS ###
    # Tipos de inputs:
        # Indicador da sequência de próximos inputs: "DADOS"
        # Comando: MATRÍCULA NOME DEPARTAMENTO
        # Encerramento: "FIM"
    input()
    # Primeira linha de dados válidos
    dados = input()
    while dados != "fim":
        dados = dados.split(",") 
        # Decifrar dados privados (Matrícula e Nome) - É garantido que os dados iniciais são válidos
        dados = decifrar_dados(dados)
        posicao = get_posicao(dados[0])
        # Adidionar posição e sub-listas para turmas e dias
        dados.append(posicao)
        dados.append([])
        dados.append([])
        # Adidionar listas com informações pessoais as 'super' listas correspondentes
        if posicao == POSICOES[0]:
            # Remover sub-lista de horários do coordenador
            dados.pop()
            coordenadores.append(dados)
        elif posicao == POSICOES[1]:
            professores.append(dados)
        elif posicao == POSICOES[2]:
            alunos.append(dados)
        dados = input()

    ### INICIAR SISTEMA DE AÇÕES ###
    # Tipos de inputs:
        # Indicador da sequência de próximos inputs: "ACOES"
        # Comando: MATRÍCULA AÇÃO
        # Encerramento: "FIM"
    input()
    # Primeira linha de comandos válidos
    comando = input()
    while comando != "FIM":
        matricula, acao = comando.split()
        posicao = get_posicao(matricula)
        # Verificar válidade da posição e ação
        if not acao in ACOES:
            argumento_invalido("Acao", acao)
        # Passar execução para as funções de controle
        elif posicao == POSICOES[0]:
            controlador( acao, matricula, coordenadores, turmas, info)
        elif posicao == POSICOES[1]:
            controlador( acao, matricula, professores, turmas, info)
        elif posicao == POSICOES[2]:
            controlador( acao, matricula, alunos, turmas, info)
        comando = input()


# FUNÇÃO DE CONTROLE ----------------------------------------------------------------- #

def controlador(acao:str, matricula:str, pessoas:list, turmas:list, info:list)->None:
    # Verificar existência da pessoa com base na posição/matrícula recebida
    pessoa = buscar_sublista(matricula, pessoas)
    if not pessoa:
        argumento_invalido("Matricula", matricula)
        return
    # Executar ações com base no chamador correto
    posicoes = ["coordenador", "professor", "aluno"]
    if acao == "i":
        imprimir_turmas(pessoa, info)
    elif acao == "m":
        turma = []
        if pessoa[3].lower()  == posicoes[0]:
            turma = montar_turma(pessoa)
            nomes_das_turmas = [item[0] for item in turmas]
            turmas.insert(insercao_binaria(turma[0], nomes_das_turmas), turma)
        elif pessoa[3].lower() == posicoes[1]:
            turma = ministrar_turma(pessoa, turmas)
        elif pessoa[3].lower() == "aluno":
            turma = matricular_turma(pessoa, turmas)
        # Inserir turma de forma ordenada na lista de turmas da pessoa atual
        if turma:
            # Considerar apenas as turmas da pessoa em questão
            nomes_das_turmas = [item[0] for item in pessoa[4]]
            pessoa[4].insert(insercao_binaria(turma[0], nomes_das_turmas), turma)

# ------------------------------------------------------------------------------------- #


# FUNÇÕES DE AÇÕES -------------------------------------------------------------------- #
def imprimir_turmas(pessoa:list, info:list)->None:
    imprimir_cabecalho(info[4], pessoa[2], pessoa[1], pessoa[3])
    contador = 0
    for turma in pessoa[4]:
        if turma_valida(turma):
            contador += 1
            print()
            print(f"#{contador:02}: {turma[0].upper()}")
            print(f"---> Professor(a): {turma[3][1]}")
            print(f"---> Horario: {'/'.join(turma[5])}")
            print(f"---> Matriculados: {len(turma[4])} aluno(s)")
    print()
    print(f"==> {contador} turmas ativa(s).")
    print()
    imprimir_rodape(info[1], info[0], info[3], info[2])


def montar_turma(coordenador:list)->list:
    nome, dias = input().split(",")
    turma = [nome, coordenador[2], coordenador, None, [], dias.split("/")]
    return turma


def ministrar_turma(professor:list, turmas:list)->list:
    nome_da_turma = input()
    # Verificar existência da turma
    turma = get_turma(nome_da_turma, turmas)
    if not turma:
        return []
    # Verificar se a turma está disponível para o professor
    if not turma_compativel(professor, turma, tem_professor=False):
        return []
    # Adicionar professor na turma e ocupar dias do professor
    turma[3] = professor
    professor[5] += turma[5]
    return turma


def matricular_turma(aluno:list, turmas:list)->list:
    nome_da_turma = input()
    # Verificar existência da turma
    turma = get_turma(nome_da_turma, turmas)
    if not turma:
        return []
    # Verificar se a turma está disponível para o aluno
    if not turma_compativel(aluno, turma):
        return []
    # Adicionar aluno na turma e ocupar dias do aluno
    turma[4].append(aluno)
    aluno[5] += turma[5]
    return turma

# ------------------------------------------------------------------------------------- #


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
    primeiro = s.lower()[:i].rfind("primeiro")
    segundo = s.lower()[:i].rfind("segundo")
    return 2 if segundo > primeiro else 1


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


# É garantido que a sigla do local é alfanumérica e está cercada pelas últimas aspas duplas
def get_posicao_sigla(s:str)->int:
    while True:
        ultima_aspas = s.rfind('"')
        contagem = 0
        while s[ultima_aspas - contagem - 1].isalnum():    
            contagem += 1
        if contagem >= 2 and s[ultima_aspas - contagem - 1]:
            return ultima_aspas - contagem - 1


def buscar_sublista(elemento:str, l:list, sub_posicao:int=0)->list:
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
        return busca_binaria(item, itens, meio+1, alto)
    else:
        return busca_binaria(item, itens, baixo, meio-1)


def get_turma(nome_da_turma:str, turmas:list)->list:
    nomes_das_turmas = [item[0] for item in turmas]
    indice_turma = busca_binaria(nome_da_turma, nomes_das_turmas, 0, len(nomes_das_turmas))
    if indice_turma == -1:
        print("Turma inexistente.")
        return []
    return turmas[indice_turma]


def get_posicao(matricula:str)->str:
    sigla = matricula[:2]
    if sigla == "co":
        return "Coordenador"
    elif sigla == "po":
        return "Professor"
    elif sigla == "al":
        return "Aluno"
    return ""

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


def decifrar_dados(dados:list)->list:
    # Função interna para facilitar lógica / evitar repetição desnecessária
    def aplicar_cesar(matricula:str, nome:str)->list:
        rotacao = int(matricula[-1])
        matricula_decifrada = criptografia_cesar(matricula, -rotacao)
        matricula_decifrada = matricula_decifrada[:-1] + str(rotacao)
        nome_decifrado = criptografia_cesar(nome, -rotacao)
        return [matricula_decifrada, nome_decifrado, dados[2]]

    # Supor que é aluno: Apenas Cifra de César
    dados_decifrados = aplicar_cesar(dados[0], dados[1])
    if get_posicao(dados_decifrados[0]) == "Aluno":
        return dados_decifrados
    # Como é garantido que os dados inicias são válidos , é certo que será coordenador ou professor
    dados_decifrados = [criptografia_substituicao(dados[0]), criptografia_substituicao(dados[1]), dados[2]]
    dados_decifrados = aplicar_cesar(dados_decifrados[0], dados_decifrados[1])
    return dados_decifrados
    

def turma_valida(turma:list)->bool:
    # Existe professor e aluno na turma
    return turma[3] and len(turma[4]) > 0


def turma_compativel(pessoa:list, turma:list, tem_professor=True)->bool:
    # Verificar se departamentos são iguais
    if pessoa[2].lower() != turma[1].lower():
        print("Turma de departamento diferente.") 
        return False
    # Verificar se turma já tem professor
    if turma[3] and not tem_professor:
        print("Turma já possui professor.")
        return False
    elif not turma[3] and tem_professor:
        print("Turma não possui professor.")
        return False
    # Verificar conflito de dias
    for dia in turma[5]:
        if dia in pessoa[5]:
            print("Conflito de dias.")
            return False
    return True

# ------------------------------------------------------------------------------------- #


# FUNÇÕES DE IMPRESSÃO --------------------------------------------------------------------- #

def argumento_invalido(tipo:str, arg:str)->None:
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
