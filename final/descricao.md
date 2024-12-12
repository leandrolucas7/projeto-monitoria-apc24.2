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


## 🚨 POSSÍVEIS EXCEÇÕES PARA LIDAR

Casos particulares

---

## 🛠️ SUA TAREFA

tarefa...

>**Dica:** Adicionar dicas.

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
        <td><pre>comeco
vhdefg3
cewvut6
seapc10
cecjv68
fim
        </pre></td>
        <!-- Outputs -->
        <td><pre>seabcd3
usabcd3
seapc10
usunb21
        </pre></td>
    </tr>
</tbody>

</table>

---