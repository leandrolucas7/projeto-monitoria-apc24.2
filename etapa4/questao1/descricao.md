<div align="center">
  <h1>QUESTÃO 01</h1>
    <img src="../../assets/ursinho.webp" align="center" style="width: 600px; height: 340px;" />
  </p>
</div>

## 📝 Quem não guarda, perde.

A primeira melhora que Jaime deseja implementar é a possibilidade de guardar mais informações em suas listas.

Até agora, ele só conseguia armazenar o nome das suas atividades. Contudo, qualquer agenda minimamente decente precisa de outras informações complementares.

E esse é o nosso trabalho agora.

## 🛠️ SUA TAREFA

Nesse exercícios, você receberá vários inputs de `info` até o input de `encerramento`. Esses inputs de `info` apresentam informações sobre as tarefas que Jaime precisa agendar.

Cada tarefa pode fazer parte de uma **categoria** (existem 3 no total). Seu papel é criar uma sublista para cada atividade e armazenar a tarefa na lista principal da categoria correspondente.

**Tipos de input**

- `info`: string que contém **categoria**, **nome**, **dia** e **local** da tarefa - nessa ordem e separados por vírgula:
  - **Ex: un,entregar relatorio de fisexp,quarta,instituto de fisica 
- `encerramento`: string que indica o fim dos inputs:
  - **fim**

**Categorias:**

- **Pessoal:** representada por `pe`;
- **Universidade:** representada por `un`;
- **Trabalho:** representada por `tr`.

**Variáveis obrigatórias para correção:**

- Será necessário declarar três listas principais - com os nomes descritos abaixo - para armazenar as listas de tarefas com categorias correspondentes:
  - `lista_pessoal`
  - `lista_universidade`
  - `lista_trabalho`

**Resumindo:**

Para cada input de tarefa, crie uma sublista no formato: `[nome, dia, local]` e adicione a lista geral de categoria correspondente.

O teste irá chamar a impressão das listas gerais - por isso elas precisam ser declaradas com os nomes especificados acima - e o conteúdo delas precisa estar correto.

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
un,entregar relatorio de fisexp,quarta,instituto de fisica
pe,assistir Silicon Valley,domingo,HBO
tr,reuniao sobre o novo projeto,segunda,escritorio
tr,visita ao cliente,terca,fabrica
pe,futebol com amigos,sabado,quadra do bairro
un,prova de probabilidade e estatistica,terca,ICC - Anf. 15
print(lista_pessoal)
print(lista_universidade)
print(lista_trabalho)
        </pre></td>
        <!-- Outputs -->
        <td><pre>
[['assistir Silicon Valley', 'domingo', 'HBO'], ['futebol com amigos', 'sabado', 'quadra do bairro']]
[['entregar relatorio de fisexp', 'quarta', 'instituto de fisica'], ['prova de probabilidade e estatistica', 'terca', 'ICC - Anf. 15']]
[['reuniao sobre o novo projeto', 'segunda', 'escritorio'], ['visita ao cliente', 'terca', 'fabrica']]
        </pre></td>
    </tr>
</tbody>

</table>

---
