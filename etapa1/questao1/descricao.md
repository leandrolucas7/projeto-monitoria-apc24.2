<div align="center">
  <h1>QUESTÃO 01</h1>
    <img src="../../assets/velozes.jpg" align="center" style="width: 600px; height: 340px;" />
  </p>
  <p>
    “ADICIONAR FRASE!!!!!!!!!!!"
  </p>
</div>

## 📝 Na dúvida, resuma.

Como bom programador, assim que abriu o livro, Jaime buscou padrões que o ajudassem na sua tarefa de criar um resumo sobre as invenções ou descobertas. Após folhear algumas páginas ele encontrou algo que podia ajudá-lo a extrair as informações importantes para o seu resumo.  
Ele percebeu que, para toda nova invenção/descoberta que o livro citava, os dois primeiros parágrafos seguiam o seguinte formato.

**Primeiro parágrafo:**

> A <span style="color: red">imprensa</span>, criada por <span style="color: green">Johannes Gutenberg</span>, trouxe inúmeras mudanças para nossa sociedade. Ele <span style="color: blue">inventou</span> esse instrumento em <span style="color: orange">1440</span> na <span style="color: fuchsia">"RFA"</span> - <span style="color: teal">Republica Federal da Alemanha</span>.

> A <span style="color: red">gravidade</span>, foi descrita por <span style="color: green">Isaac Newton</span>, sua "teoria da gravidade" trouxe grandes avanços para a astronomia. Newton <span style="color: blue">descobriu</span> esse fenômeno em <span style="color: orange">1687</span> no <span style="color: fuchsia">"RUGI"</span> - <span style="color: teal">Reino Unido da Gra-Bretanha e Irlanda do Norte</span>.

- <span style="color: red">Tópico</span>: segunda palavra e imediatamente antes de uma vírgula;
- <span style="color: green">Pessoa</span>: nome e sobrenome imediatamente antes da segunda vírgula do parágrafo;
- <span style="color: blue">Categoria</span>: a palavra "inventou" ou "descobriu" mais próxima e anterior a abreviação do local;
- <span style="color: orange">Ano</span>: A primeira aparição de 4 dígitos em sequência mais próxima e anterior a abreviação do local;
- <span style="color: fuchsia">Abreviação</span>: A última aparição de qualquer palavra entre aspas duplas;
- <span style="color: teal">Invenção / Descoberta</span>: Após a abreviação e o hífen e sempre alfanumérico.

**Segundo parágrafo:**

> Alguns avanços são, disseminação do conhecimento,  alfabetização em massa, revolução científica, surgimento dos jornais.

> Os desenvolvimentos observados são, previsão de órbitas planetárias, cálculo de trajetórias de projéteis.

- Consequências das invenções / descobertas separadas por `,`;
- No primeiro caso são 4 consequências, equanto no segundo são 2.


## 🛠️ SUA TAREFA

Defina as funções listadas abaixo. Todas vão receber variações do primeiro parágrafo exemplificado acima e devem imprimir a informação que extrairam do texto que receberam.

- `get_topico()`: imprime o tópico;
- `get_pessoa()`: imprime a pessoa;
- `get_categoria()`: imprime "Invencao" ou "Descoberta" caso a categoria encontrada seja "inventou" ou "descobriu";
- `get_ano()`: imprime o ano;
- `get_local()`: imprime o local;

>As impressões devem ser capitalizadas. Caso haja mais de uma palavra, ambas devem ser capitalizadas.

>**Os nomes da funções devem ser iguais aos descritos acima. Todas vão receber uma `string` como argumento.**

---

## 👀 DEMONSTRAÇÃO

**Considerando os exemplos de primeiro parágrafo acima, assuma - para os testes abaixo - que conteúdo da variável `texto` corresponde ao primeiro e segundo exemplo, respectivamente.**
<table class="coderunnerexamples">

<thead>
    <tr>
        <th>Input</th>
        <th>Result</th>
    </tr>
</thead>

<tbody>
    <!– Primeiro Teste –>
    <tr>
        <!– Inputs –>
        <td><pre>get_topico(texto)
get_pessoa(texto)
get_categoria(texto)
get_ano(texto)
get_local(texto)
        </pre></td>
        <!– Outputs –>
        <td><pre>Imprensa
Johannes Gutenberg
Invencao
1440
Republica Federal da Alemanha
        </pre></td>
    </tr>
    <!––>
    <!– Segundo Teste –>
    <tr>
        <!– Inputs –>
        <td><pre>get_topico(texto)
get_pessoa(texto)
get_categoria(texto)
get_ano(texto)
get_local(texto)
        </pre></td>
        <!– Outputs –>
        <td><pre>Gravidade
Isaac Newton
Descoberta
1687
Reino Unido da Gra-Bretanha e Irlanda do Norte
        </pre></td>
    </tr>
</tbody>

</table>

---
