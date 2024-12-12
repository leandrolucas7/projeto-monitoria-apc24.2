<div align="center">
  <h1>QUESTÃO 03</h1>
    <img src="../../assets/dividir.png" align="center" style="width: 600px; height: 340px;" />
  </p>
</div>

## 📝 Dividir para conquistar.

Após outra análise do seu programa de resumos, Jaime observou que, já que todos os resumos seguem esse template, é possível dividir o trabalho entre funções diferentes. Para isso, ele criou 3 funções bases - `imprimir_cabecalho()`, `imprimir_info()`, `imprimir_rodape()`.  
Cada função é responsável pela impressão dos respectivos trechos do template.  
Além disso, ele criou a função `imprimir_resumo()` que chama as demais funções e imprime o resumo inteiro.  

**Template:**

    >>>>>
    TOPICO
    Categoria
    [Pessoa]

    => X avancos importantes:
    --> avanço 1, avanço 2, ..., avanço x.

    "Local - Ano"
    <<<<<

## 🛠️ SUA TAREFA

Implemente as 4 funções do trabalho de Jaime, levando em consideração quantos argumentos elas recebem, seus tipos e sua ordem - todos descritos abaixo:

>**imprimir_cabecalho**(topico, categoria, pessoa)

>**imprimir_info**(frase)

>**imprimir_rodape**(local, ano)

>**imprimir_resumo**(topico, categoria, pessoa, local, ano, frase)

>**OBS:** O argumento `frase` é uma string no padrão do segundo parágrafo definido nos exemplos anteriores.

>**OBS:** Os espaços que separam os trechos do resumo devem fazer parte da função `imprimir_info()`.

---

## 👀 DEMONSTRAÇÃO

**Para os testes abaixo, vamos considerar as variáveis abaixo e seus respectivos valores:**

- **topico**: imprensa
- **categoria**: invencao
- **pessoa**: johannes gutenberg
- **local**: Republica Federal da Alemanha
- **ano**: 1440
- **frase**: Alguns avanços são, disseminação do conhecimento,  alfabetização em massa, revolução científica, surgimento dos jornais.


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
        <td><pre>imprimir_resumo(topico, categoria, pessoa, local, ano, frase)
        </pre></td>
        <!-- Outputs -->
        <td><pre>>>>>>
IMPRENSA
Invencao

[Johannes Gutenberg]

=> 4 avancos importantes:
--> disseminação do conhecimento,  alfabetização em massa, revolução científica, surgimento dos jornais.

#Republica Federal da Alemanha - 1440
<<<<<
        </pre></td>
    </tr>
    <!-- Segundo Teste -->
    <tr>
        <!-- Inputs -->
        <td><pre>imprimir_cabecalho(topico, categoria, pessoa)
        </pre></td>
        <!-- Outputs -->
        <td><pre>>>>>>
IMPRENSA
Invencao
[Johannes Gutenberg]
        </pre></td>
    </tr>
    <!-- Terceiro Teste -->
    <tr>
        <!-- Inputs -->
        <td><pre>imprimir_info(info)
        </pre></td>
        <!-- Outputs -->
        <td><pre>

=> 4 avancos importantes:
--> disseminação do conhecimento,  alfabetização em massa, revolução científica, surgimento dos jornais.
        </pre></td>
    </tr>
    <!-- Quarto Teste -->
    <tr>
        <!-- Inputs -->
        <td><pre>imprimir_rodape(local, ano)
        </pre></td>
        <!-- Outputs -->
        <td><pre>#Republica Federal da Alemanha - 1440
<<<<<
        </pre></td>
    </tr>
</tbody>

</table>

---
