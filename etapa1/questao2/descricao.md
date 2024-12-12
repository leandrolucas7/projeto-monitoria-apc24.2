<div align="center">
  <h1>QUESTÃO 02</h1>
    <img src="../../assets/neymar.jpg" align="center" style="width: 600px; height: 340px;" />
  </p>
</div>

## 📝 Onde não há normas, a ordem se perde.

Agora que já consegue extrair as informações importantes do texto, Jaime está pronto para montar o seu resumo.  
Contudo, ele sabe que para um resumo ser bom é preciso que esteja organizado.  
Para isso, ele definiu algumas normas que seu resumo deve seguir.

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

Você receberá 2 strings, uma contendo as informações gerais sobre o tópico em questão e outra com os avanços provenientes desse tópico.  
É seu trabalho extrair as informações necessárias dessas strings e montar o resumo nos moldes definidos por Jaime.

>**DICA:** Altere as funções construídas anteriormente para retornar o valor extraído, ao invés de imprimi-los, e use o valor de retorno para chegar o template.

>**OBS:** Não é necessário formatar os avancos importantes, é suficiente extrair o trecho em que eles são citados e replicar no template.
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
A imprensa, criada por Johannes Gutenberg, trouxe inúmeras mudanças para nossa sociedade. Ele inventou esse instrumento em 1440 na "RFA" - Republica Federal da Alemanha.
Alguns avanços são, disseminação do conhecimento,  alfabetização em massa, revolução científica, surgimento dos jornais.
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
</tbody>

</table>

---
