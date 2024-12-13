<div align="center">
  <h1>QUESTÃO 03</h1>
    <img src="../../assets/londres.gif" align="center" style="width: 600px; height: 340px;" />
  </p>
</div>

## 📝 Pontualidade britânica.

Ufa! Jaime agora está com todas as suas atividades agendadas e sua vida de estudos mais tranquila - na medida do possível para qualquer estudante.

Visando melhorar otimizar ainda mais a sua organização, Jaime agora quer organizar sua agenda dinamicamente - ou seja, à medida que novos compromissos vão surgindo.


## 🛠️ SUA TAREFA

Nesse exercício, você receberá uma sequência de inputs de `atividades`, que continuam até o input de `encerramento`.

Entre os inputs de `atividades`, os testes irão chamar a função, `imprimir_lista(minha_lisa)`. Você não precisa se preocupar com essa função (ela é definida pelo testador), apenas com o argumento `minha_lista`.

Para ter êxito na questão, você vai precisar declarar uma variável, que armazena uma lista, chamada `minha_lista`. Nela você, organizará os inputs de `atividades` alfabeticamente - no momento que eles são recebidos. Ou seja a lista já é montada em ordem alfabética.

Entre alguns inputs, a função do testador `imprimir_lista()` irá ser invocada com o argumento `minha_lista`- por isso a sua lista precisa ter esse nome.

Esses testes intermediários vão validar se sua lista está sempre ordenada.

Os inputs se encerram com o `encerramento` que é uma string com valor **fim**.

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
Exercicio de derivadas
Ensaio para apresentacao
imprimir_lista(minha_lista)
atividade de esperanca e variancia
LISTA DE ORDENACAO
exercicio de COMbinatoria
imprimir_lista(minha_lista)
Trabalho de APC
imprimir_lista(minha_lista)
Prova de Calculo
fim
        </pre></td>
        <!-- Outputs -->
        <td><pre>
['Ensaio para apresentacao', 'Exercicio de derivadas']
['atividade de esperanca e variancia', 'Ensaio para apresentacao', 'exercicio de COMbinatoria', 'Exercicio de derivadas', 'LISTA DE ORDENACAO']
['atividade de esperanca e variancia', 'Ensaio para apresentacao', 'exercicio de COMbinatoria', 'Exercicio de derivadas', 'LISTA DE ORDENACAO', 'Trabalho de APC']
        </pre></td>
    </tr>
</tbody>

</table>

---
