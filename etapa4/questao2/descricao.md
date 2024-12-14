<div align="center">
  <h1>QUESTÃO 02</h1>
    <img src="../../assets/explicacao.gif" align="center" style="width: 600px; height: 340px;" />
  </p>
</div>

## 📝 Compreendeu o ponto?

O sistema de controle de Jaime está cada vez mais completo. Contudo, não se pode deixar que a complexidade da implementação do sistema atrapalhe o uso do usuário do programa.

Afinal, ninguém quer ter que decifrar uma lista bidimensional achar a tarefa correta de sua agenda.


## 🛠️ SUA TAREFA

Defina uma função chamada `simpliflicar_lista()`. Ela receberá como argumento uma lista multidimensional - como mostrado abaixo.

    [
      ['entregar relatorio de fisexp', 'quarta', 'instituto de fisica'], 
      ['prova de probabilidade e estatistica', 'terca', 'ICC - Anf. 15'],
      ['revisao para prova de calculo', 'quinta', 'ICC - Anf. 17'],
      ['trabalho de APC', 'segunda', 'Linf'],
    ]

Sua função deve montar e retornar uma nova lista (unidimensional) contendo apenas os nomes das tarefas de cada sublista presente na lista multidimensional recebida.

>**DICA:** Usar `list comprehension` para facilitar a criação da nova lista.

---

## 👀 DEMONSTRAÇÃO

Considerando a lista multidimensional acima como `lista_multi`:

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
simpliflicar_lista(lista_multi)
        </pre></td>
        <!-- Outputs -->
        <td><pre>
['entregar relatorio de fisexp', 'prova de probabilidade e estatistica', 'revisao para prova de calculo', 'trabalho de APC']
        </pre></td>
    </tr>
</tbody>

</table>

---
