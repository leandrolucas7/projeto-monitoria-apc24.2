<div align="center">
  <h1>PROJETO FINAL</h1>
    <img src="../assets/spider.jpeg" align="center" style="width: 600px; height: 340px;" />
  </p>
</div>

## 📝 Com grandes poderes vêm grandes responsabilidades.

A saga do nosso herói Jaime está chegando ao fim. Após anos de esforço, o estudante está prestes a se formar em sua universidade. Durante esse período, ele aprendeu mais do que podia imaginar e agora parte para sua jornada como programador no mundo real.

Contudo, antes de deixar a universidade, Jaime deseja usar seus superpoderes de programação para retribuir todo o conhecimento adquirido e as experiências vivênciadas durante seu período de universitário.

Para isso, Jaime - que, como todo bom super-herói / programador não foje dos desafios - decidiu enfrentar o maior inimigo de todos os estudantes de universidade: o SIGAA.

Ele irá presentar a universidade com um novíssimo sistema de gestão dinâmico e confiável - QUE NUNCA CAI NO DIA DA MATRÍCULA EXTRAORDINÁRIA!

## 📌 EXPLICAÇÃO PRÉVIA

Durante a execução do programa, você irá receber vários tipos de inputs que guiarão o que o sistema deve fazer.

Entre os tipos de input estão: `informacoes gerais`, `tipo`, `encerramento`, `dados`, `acoes`, `complemento`.

**Explicação dos inputs:**

>**`informacoes gerais`:**
>- String que contém informações a serem extraidas como:
>   - `cargo`: Tipo de cargo que o responsável pela instituição ocupa (Ex: Reitoria, Direção...);   
>   - `responsavel`: Nome da pessoa que ocupa o cargo de chefia. O nome é sempre composto por primeiro nome e sobrenome (Ex: Albus Dumbledore);
>   - `semestre`: Indica qual o semestre atual em curso na instituição. Sempre indicado pela palavra '**primeiro**' ou '**segundo**'; 
>   - `ano`: Representa o ano atual. Sempre composto por quatro dígitos (Ex: 1995, 2024...); 
>   - `local`: Nome da instituição de ensino. Pode conter espaços e não possui quantidade pré-definida de palavras (Ex: Escola de Magia e Bruxaria de Hogwarts, Universidade de Brasilia...).   


>**`tipo`:**
>- Indica qual tipo de informação o sistema começará a receber:
>   - `DADOS`: Após esse input, o sistema receberá dados cadastrais até o input de **encerramento**;
>   - `ACOES`: Após esse input, o sistema receberá informações de **acesso** que podem, ou não, ser seguidas de um input de **complemento** até o input de **encerramento**.
   

>**`encerramento`:**
>- Indica o fim do loop de inputs do **tipo** definido anteriormente:
>   - `fim`: Encerra o loop de inputs de **dados**;
>   - `FIM`: Encerra o loop de inputs de **acoes** / **complementos**.

>**`dados`:**
>- String composta por **matricula**, **nome** e **departamento**. Todos separados por vírgula;
>- Existem 3 tipos de **matricula**, todos seguem o formato:
>   - `PPxxxxxxxS`, no qual:
>     - `PP`: Prefixo de duas letras que indica a posição da pessoa;
>     - `x`: Dígito no intervalo **[0 - 9]**;
>     - `S`: Sufixo no valor de um dígito no intervalo **[0 - 9]**.
>- Exemplos de **matricula**
>   - `co10001234`: Posição de **coordenador** com o sufixo **4**;
>   - `po10007241`: Posição de **professor** com o sufixo **1**;
>   - `al21010135`: Posição de **aluno** com o sufixo **5**;
>- O nome da pessoa é sempre composto por primeiro nome e sobrenome.
>- **IMPORTANTE**
>   - A **matricula** e **nome** recebidos estão cifrados:
>     - **Alunos** tem dados cifrados com uma camada (Cifra de César).
>     - **Coordenadores** e **Professores** tem dados cifrados com duas camadas (Cifra de César -> Cifra de Substituição).
>   - **OBS:** Essas Cifras seguem as condições estabelecidas no [exercício 3 da etapa 2](../etapa2/questao3/descricao.md)

>**`acoes`:**
>- String composta por **matricula** e **acao**. Ambos separados por um espaço em branco;
>- Existem 2 tipos de **acoes**:
>   - `i`:
>     - Imprime, no formato especificado, todas as turmas válidas relacionadas a pessoa que realizou a ação.
>   - `m`:
>     - **Coordenador**: Monta uma turma em seu departamento com base nas informações do **complemento**;
>     - **Professor**, O professor passa a ministrar a turma, exibida no **complemento** caso:
>       1. A turma exista;
>       2. A turma seja do seu departamento;
>       3. A turma ainda NÃO possua professor.
>       4. Não haja conflito de dias com outras turmas ministradas.
>     - **Aluno**, O aluno é matriculado na turma, exibida no **complemento** caso:
>       1. A turma exista;
>       2. A turma seja do seu departamento;
>       3. A turma ainda JÁ possua professor.
>       4. Não haja conflito de dias com outras turmas ministradas.
>     - **OBS:** Ações do tipo **m** são seguidas de **complemento**.
>- **OBS:** Para ser válida, uma turma precisa ter **professor** e, ao menos, **um aluno**.

>**`complemento`:**
>- String que complementa as ações do tipo **m**. Difere entre posições que executam a ação;
>- Tipos de  **acoes**:
>   - `Coordenador`:
>     - Nome da turma seguido pelos dias de aula - separados por vírgula (Ex: Defesa Contra as Artes das Trevas,seg/qua/sex).
>   - `Profesor` e `Aluno`:
>     - Nome da turma (Ex: Defesa Contra as Artes das Trevas).

---


## 📐 ESPECIFICAÇÕES RESUMIDAS

- `Coordenador`:
  - Cria as turmas e associa-as ao seu departamento.
- `Professor`:
  - Ministra turmas existentes em seu departamento mas que ainda não possuem professor. Também não pode haver conflito de horários.
- `Aluno`:
  - Matricula-se em turmas existentes em seu departamento que possuem professor. Também não pode haver conflito de horários.
- Ação de impressão `i`:
  - Imprime apenas as turmas válidas.
    - Possuem **professor** e, ao menos um, **aluno**;
    - Apresenta o total se turmas válidas.
  - Imprime as turmas em ordem alfabética.

---

## 🚨 POSSÍVEIS EXCEÇÕES PARA LIDAR

- **Turma inexistente**
  - Quando algum professor ou aluno tenta se associar a alguma turma que não existe;
  - `mensagem de erro`: Turma inexistente.
- **Turma de departamento diferente**
  - Quando algum professor ou aluno tenta se associar a alguma turma de outro departamento;
  - `mensagem de erro`: Turma de departamento diferente.
- **Turma ja possui professor**
  - Quando algum professor tenta se associar a alguma turma que já possui professor associado;
  - `mensagem de erro`: Turma ja possui professor.
- **Turma nao possui professor**
  - Quando algum aluno tenta se associar a alguma turma que não possui professor;
  - `mensagem de erro`: Turma nao possui professor.
- **Conflito de dias**
  - Quando algum professor ou aluno tentar se associar a alguma turma cujo horario é conflitante com outra que ele já faz parte;
  - `mensagem de erro`: Conflito de dias.

---

## 🖨 FORMATO DE IMPRESSÃO ️

    >>>>>
    NOME DO LOCAL MAIUSCULO
    Departamento Nome
    [Posicao(a): Nome Pessoa]

    #01: TURMA B
    ---> Professor(a): Nome Professor
    ---> Horario: xxx/xxx
    ---> Matriculados: X aluno(s)

    #02: TURMA Z
    ---> Professor(a): Nome Professor
    ---> Horario: xxx
    ---> Matriculados: X aluno(s)

    ==> Y turmas ativa(s).

    "Nome Responsavel - Cargo (ano.semestre)"
    <<<<<

**Exemplo  prático de um coordenador:**
- **Cargo:** Reitoria;
- **Nome do responsável:** Albus Dumbledore;
- **Semestre:** Primeiro;
- **Ano:** 2025;
- **Local:** Escola de Magia e Bruxaria de Hogwarts;
- **Nome do coordenador:** Godric Gryffindor;
- **Departamento:** Grifinoria;
- **Posição:** Coordenador;
- **Turmas:**
  - Defesa Contra as Artes das Trevas:
    - Professor(a): 
    - Horario: seg/qua/sex
    - Alunos: __________
  - Transfiguracao:
    - Professor(a): Minerva McGonagall
    - Horario: seg/qua
    - Alunos: Harry Potter, Hermione Granger, Ron Weasley
  - Trato das Criaturas Magicas:
    - Professor(a): Rubeus Hagrid
    - Horario: qua
    - Alunos: __________
  - Detenção - Floresta Proibida:
    - Professor(a): Rubeus Hagrid
    - Horario: qua
    - Alunos: Harry Potter

**Resultado:**

    >>>>>
    ESCOLA DE MAGIA E BRUXARIA DE HOGWARTS
    Departamento Grifinoria
    [Coordenador(a): Godric Gryffindor]

    #01: DETENCAO - FLORESTA PROIBIDA
    ---> Professor(a): Rubeus Hagrid
    ---> Horario: sex/sab
    ---> Matriculados: 1 aluno(s)

    #02: TRANSFIGURACAO
    ---> Professor(a): Minerva McGonagall
    ---> Horario: seg/qua
    ---> Matriculados: 3 aluno(s)

    ==> 2 turmas ativa(s).

    "Alvo Dumbledore - Reitoria (2025.1)"
    <<<<<


## 🛠️ SUA TAREFA

Você receberá os inputs na ordem que foi especificada acima. Cabe a você identificar os pontos de início e fim dos inputs, bem como o tipo dos inputs - todos seguem as especificações descritas acima.

Você é livre para escolher como associar, armazenar e manipular os dados dos inputs, desde que as ações que usam esses dados gerem o resultado esperado.

> **DICA:** Grande parte nas funcionalidades que você implementou em exercícios anteriores podem ser usadas diretamente ou indiretamente nesse projeto.

<details>
<summary><b>Ver flowchart do programa:</b></summary>
adicionar flowchart
</details>

---

## 👀 DEMONSTRAÇÃO

<table>

<thead>
    <tr>
        <th>Input</th>
        <th>Result</th>
    </tr>
</thead>

<tbody>
    <!-- Primeiro Teste -->
    <tr>
        <!-- Inputs -->
        <td><pre>
O conselho, na figura de Alvo Dumbledore, acolhe os membros academicos para o segundo semestre de 1995 na "EMBH" - Escola de Magia e Bruxaria de Hogwarts
DADOS
th45554325,Phsent Pexqqnishe,Grifinoria
jk78881648,Mqluhdy MwSklysynn,Grifinoria
fq76565685,Mfwwd Utyyjw,Grifinoria
al04012300,Hermione Granger,Grifinoria
fim
ACOES
co10001234 m
Transfiguracao,qui/sex
co10001234 m
Defesa Contra as Artes das Trevas,seg/qua/sex
po10007241 m
Transfiguracao
po10007241 m
Defesa Contra as Artes das Trevas
al04012300 m
Transfiguracao
al21010135 m
Transfiguracao
al21010135 i
FIM
        </pre></td>
        <!-- Outputs -->
        <td><pre>
Conflito de dias.
>>>>>
ESCOLA DE MAGIA E BRUXARIA DE HOGWARTS
Departamento Grifinoria
[Aluno(a): Harry Potter]

#01: TRANSFIGURACAO
---> Professor(a): Minerva McGonagall
---> Horario: qui/sex
---> Matriculados: 2 aluno(s)

==> 1 turmas ativa(s).

"Alvo Dumbledore - Conselho (1995.2)"
<<<<<
        </pre></td>
    </tr>
    <!-- Segundo Teste -->
    <tr>
        <!-- Inputs -->
        <td><pre>
A diretoria, representada por Alvo Dumbledore, recebe os docentes e discentes para o primeiro semestre de 2025 na "EMBH" - Escola de Magia e Bruxaria de Hogwarts
DADOS
th45554325,Phsent Pexqqnishe,Grifinoria
rf33324563,Btitutc Bivampclg,Sonserina
gh54544805,Drarebd Divgr,Sonserina
jk78881648,Mqluhdy MwSklysynn,Grifinoria
fq76565685,Mfwwd Utyyjw,Grifinoria
ep64446724,Hvegs Qepjsc,Sonserina
al04012300,Hermione Granger,Grifinoria
fim
ACOES
co10001234 m
Defesa Contra as Artes das Trevas,seg/qua/sex
co10001234 m
Transfiguracao,ter/qui
co10001234 m
Feiticos,seg/sex
co00019876 m
Pocoes,ter/qui
po10007241 m
Transfiguracao
po10007241 m
Feiticos
po01011754 m
Defesa Contra as Artes das Trevas
po01011754 m
Pocoes
al04012300 m
Transfiguracao
al04012300 m
Feiticos
al21010135 m
Feiticos
al21010135 m
Defesa Contra as Artes das Trevas
al20002384 m
Pocoes
co10001234 i
al20002384 m
Estudo dos Trouxas
al20002384 i
FIM
        </pre></td>
        <!-- Outputs -->
        <td><pre>
Turma de departamento diferente.
Turma não possui professor.
\>>>>>
ESCOLA DE MAGIA E BRUXARIA DE HOGWARTS
Departamento Grifinoria
[Coordenador(a): Godric Gryffindor]

#01: FEITICOS
---> Professor(a): Minerva McGonagall
---> Horario: seg/sex
---> Matriculados: 2 aluno(s)

#02: TRANSFIGURACAO
---> Professor(a): Minerva McGonagall
---> Horario: ter/qui
---> Matriculados: 1 aluno(s)

==> 2 turmas ativa(s).

"Alvo Dumbledore - Diretoria (2025.1)"
<<<<<
Turma inexistente.
\>>>>>
ESCOLA DE MAGIA E BRUXARIA DE HOGWARTS
Departamento Sonserina
[Aluno(a): Draco Malfoy]

#01: POCOES
---> Professor(a): Severus Snape
---> Horario: ter/qui
---> Matriculados: 1 aluno(s)

==> 1 turmas ativa(s).

"Alvo Dumbledore - Diretoria (2025.1)"
<<<<<
        </pre></td>
    </tr>
    <!-- Terceiro Teste -->
    <tr>
        <!-- Inputs -->
        <td><pre>
A reitoria, na presença de Alvo Dumbledore, deseja um ótimo primeiro semestre de 2025 na "EMBH" - Escola de Magia e Bruxaria de Hogwarts.
DADOS
th45554325,Phsent Pexqqnishe,Grifinoria
rf33324563,Btitutc Bivampclg,Sonserina
fg45433394,Datqac Nuodmr,Grifinoria
hi54656136,Pifwuoi Elcqpifj,Sonserina
fg37445554,Omjrqdgw Jgsknudb,Corvinal
jk78881648,Mqluhdy MwSklysynn,Grifinoria
fq76565685,Mfwwd Utyyjw,Grifinoria
it92889028,Kmlzqkw Lqoowzg,Lufa-Lufa
ep64446724,Hvegs Qepjsc,Sonserina
al04012300,Hermione Granger,Grifinoria
bm11113121,Hjooz Xfbtmfz,Grifinoria
do56334153,Ylqfhqw Fudeeh,Sonserina 
fim
ACOES
co10001234 m
Trato das Criaturas Magicas,seg/qua
po09011155 m
Trato das Criaturas Magicas
al04012300 m
Trato das Criaturas Magicas
co00019876 m
Pocoes,seg/qua
co10001234 m
Defesa Contra as Artes das Trevas,qui/sex
po12010533 m
Pocoes
po17009995 m
Defesa Contra as Artes das Trevas
al04012300 m
Defesa Contra as Artes das Trevas
al21010135 m
Trato das Criaturas Magicas
al20002384 m
Pocoes
al00002011 m
Trato das Criaturas Magicas
co10001234 m
Transfiguracao,ter
co10001234 m
Detencao - Floresta Proibida,sex/sab
po10007241 m
Transfiguracao
al04012300 m
Transfiguracao
po10007241 m
Defesa Contra as Artes das Trevas
po09011155 m
Detencao - Floresta Proibida
al21010135 m
Detencao - Floresta Proibida
al21010135 m
Defesa Contra as Artes das Trevas
al00002011 m
Defesa Contra as Artes das Trevas
po10007241 i
al04012300 i
co10001234 i
co00019876 m
Feiticos,seg/ter/qua
co00019876 i
FIM
        </pre></td>
        <!-- Outputs -->
        <td><pre>
Turma de departamento diferente.
Turma não possui professor.
Conflito de dias.
\>>>>>
ESCOLA DE MAGIA E BRUXARIA DE HOGWARTS
Departamento Grifinoria
[Professor(a): Minerva McGonagall]

#01: DEFESA CONTRA AS ARTES DAS TREVAS
---> Professor(a): Minerva McGonagall
---> Horario: qui/sex
---> Matriculados: 1 aluno(s)

#02: TRANSFIGURACAO
---> Professor(a): Minerva McGonagall
---> Horario: ter
---> Matriculados: 1 aluno(s)

==> 2 turmas ativa(s).

"Alvo Dumbledore - Reitoria (2025.1)"
<<<<<
\>>>>>
ESCOLA DE MAGIA E BRUXARIA DE HOGWARTS
Departamento Grifinoria
[Aluno(a): Hermione Granger]

#01: TRANSFIGURACAO
---> Professor(a): Minerva McGonagall
---> Horario: ter
---> Matriculados: 1 aluno(s)

#02: TRATO DAS CRIATURAS MAGICAS
---> Professor(a): Rubeus Hagrid
---> Horario: seg/qua
---> Matriculados: 3 aluno(s)

==> 2 turmas ativa(s).

"Alvo Dumbledore - Reitoria (2025.1)"
<<<<<
\>>>>>
ESCOLA DE MAGIA E BRUXARIA DE HOGWARTS
Departamento Grifinoria
[Coordenador(a): Godric Gryffindor]

#01: DEFESA CONTRA AS ARTES DAS TREVAS
---> Professor(a): Minerva McGonagall
---> Horario: qui/sex
---> Matriculados: 1 aluno(s)

#02: DETENCAO - FLORESTA PROIBIDA
---> Professor(a): Rubeus Hagrid
---> Horario: sex/sab
---> Matriculados: 1 aluno(s)

#03: TRANSFIGURACAO
---> Professor(a): Minerva McGonagall
---> Horario: ter
---> Matriculados: 1 aluno(s)

#04: TRATO DAS CRIATURAS MAGICAS
---> Professor(a): Rubeus Hagrid
---> Horario: seg/qua
---> Matriculados: 3 aluno(s)

==> 4 turmas ativa(s).

"Alvo Dumbledore - Reitoria (2025.1)"
<<<<<
\>>>>>
ESCOLA DE MAGIA E BRUXARIA DE HOGWARTS
Departamento Sonserina
[Coordenador(a): Salazar Slytherin]

#01: POCOES
---> Professor(a): Horacio Slughorn
---> Horario: seg/qua
---> Matriculados: 1 aluno(s)

==> 1 turmas ativa(s).

"Alvo Dumbledore - Reitoria (2025.1)"
<<<<<
        </pre></td>
    </tr>
</tbody>

</table>

---

