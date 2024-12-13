<div align="center">
  <h1>QUESTÃO 01</h1>
    <img src="../../assets/bob.gif" align="center" style="width: 600px; height: 340px;" />
  </p>
</div>

## 📝 Uma lista ordenada é uma lista em paz.

Como descobrimos há pouco, Jaime está matriculado em mais disciplinas do que o que consegue dar conta.

Nesse período de aula ele recebeu inúmeras atividades das mais diversas matérias. Mas, devido a falta de tempo, foi jogando todas elas em sua pasta de atividades - de forma aleatória.

Agora ele está perdido em relação a quais atividades precisa fazer primeiro.

Assim, mais uma vez, Jaime vai usar a programação em seu próprio socorro para organizar todos os seus afazeres de acordo com os critérios apropriados.

## 🛠️ SUA TAREFA

Você receberá 3 tipos de input nessa atividade, a `prioridade`, as `atividade`(s) e o `encerramento` - nessa ordem.

Seu papel é receber as `atividades`, que virão em uma sequência de inputs - até o input de `encerramento - e montar / retornar uma lista de acordo com o critério de `prioridade` estabelecido no primeiro input.

**Formato dos inputs:**

- `prioridade` - critério usado para ordenar a lista final:
  - **data**: Ordenar as atividades de acordo com as datas mais próximas;
  - **alfa**: Ordenar as atividades em ordem alfabética;
  - **disciplina**:
    - Primeiro ordenar as atividades de acordo com a ordem alfabética de suas disciplinas de origem;
    - Dentro de cada 'subgrupo' de disciplinas, as atividades devem ser ordenadas de acordo com as datas mais próximas.
- `atividade` - string que segue o modelo abaixo:
  - atividade,materia,data
    - Ex: Lista de Equacoes Diferenciais,Calculo Dois,18
  - Para simplificar, vamos supor que todas as atividades são para o mesmo mês - que ainda vai começar. Assim, só é preciso considerar o dia de entrega.
- `encerramento` - string que indica que não há mais atividades:
  - Conteúdo da string: **fim**.

>**OBS:** É garantido que as o nome das atividades e matérias possui apenas letras, sem acentuação, e espaços em branco.

>**DICA:** Na comparação de strings, se atente na diferença entre caracteres em caixa alta ou baixa. Para esse exercício, eles devem ser considerados iguais.

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
        <td><pre>data
Lista de Transformada de Laplace,Calculo Dois,9
Experimento de Aceleracao,Fisica Exp,27
Experimento de Velocidade,Fisica Exp,20
Competicao de Programacao,APC,14
Prova Final,IAL,30
Atividade de Matrizes,IAL,15
Pratica de Listas,APC,3
Trabalho de EDOs,Calculo Dois,19
fim
        </pre></td>
        <!-- Outputs -->
        <td><pre>
['Pratica de Listas', 'Lista de Transformada de Laplace', 'Competicao de Programacao', 'Atividade de Matrizes', 'Trabalho de EDOs', 'Experimento de Velocidade', 'Experimento de Aceleracao', 'Prova Final']
        </pre></td>
    </tr>
    <!-- Segundo Teste -->
    <tr>
        <!-- Inputs -->
        <td><pre>alfa
Lista de Transformada de Laplace,Calculo Dois,9
Experimento de Aceleracao,Fisica Exp,27
Experimento de Velocidade,Fisica Exp,20
Competicao de Programacao,APC,14
Prova Final,IAL,30
Atividade de Matrizes,IAL,15
Pratica de Listas,APC,3
Trabalho de EDOs,Calculo Dois,19
fim
        </pre></td>
        <!-- Outputs -->
        <td><pre>
['Atividade de Matrizes', 'Competicao de Programacao', 'Experimento de Aceleracao', 'Experimento de Velocidade', 'Lista de Equacoes Diferenciais', 'Pratica de Listas', 'Prova Final', 'Trabalho de EDOs']
        </pre></td>
    </tr>
    <!-- Terceiro Teste -->
    <tr>
        <!-- Inputs -->
        <td><pre>disciplina
Lista de Transformada de Laplace,Calculo Dois,9
Experimento de Aceleracao,Fisica Exp,27
Experimento de Velocidade,Fisica Exp,20
Competicao de Programacao,APC,14
Prova Final,IAL,30
Atividade de Matrizes,IAL,15
Pratica de Listas,APC,3
Trabalho de EDOs,Calculo Dois,19
fim
        </pre></td>
        <!-- Outputs -->
        <td><pre>
['Pratica de Listas', 'Competicao de Programacao', 'Lista de Transformada de Laplace', 'Trabalho de EDOs', 'Experimento de Velocidade', 'Experimento de Aceleracao', 'Atividade de Matrizes', 'Prova Final']
        </pre></td>
    </tr>
</tbody>

</table>

---
