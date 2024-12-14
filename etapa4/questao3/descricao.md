<div align="center">
  <h1>QUESTÃO 03</h1>
    <img src="../../assets/luke.gif" align="center" style="width: 600px; height: 340px;" />
  </p>
</div>

## 📝 A ordenação contra-ataca.

Agora que Jaime já consegue montar listas multidimensionais e extrair seus conteúdos como uma lista unidimensional, está na hora de ordenar essas listas.

Com essa nova habilidade, Jaime pode adicionar uma nova funcionalidade ao seu sistema. Ele agora vai criar sua grade de horários da universidade.

Assim, já que cada matéria possui um nome, um departamento, um professor e dias de aula, o uso de listas multidimensionais é uma ótima ferramenta para representar uma grade com várias dessas matérias


## 🛠️ SUA TAREFA

Novamente, você receberá uma sequência de inputs de `materias`, que continuam até o input de `encerramento` (a string **fim**).

Cada input de `materia` é uma **lista unidimensional**, que contém as informações de uma matéria, no seguinte formato:

- nome,departamento,professor,diaX/diaY/diaZ:
  - **Ex:** Calculo 1,Departamento de Matematica,Gottfried Leibniz,seg/qua/sex

Para cada input de `materia` você deve criar uma sublista. Seguindo o exemplo acima, a sublista para representar essa matéria seria:

      ['Calculo 1', 'Departamento de Matematica', 'Gottfried Leibniz', ['seg', 'qua', 'sex']]

Todas as sublistas criadas devem ser armazenadas, **em ordem alfabética** (de acordo com o nome da matéria), em uma **lista principal** chamada, obrigatoriamente, `minha_grade`.

Entre alguns inputs, a função do testador `imprimir_grade()` irá ser invocada com o argumento `minha_grade`.

Esses testes intermediários vão validar se sua lista está sempre ordenada.

>**DICA:** É mais fácil encontrar a posição correta em uma lista unidimensional. Tente comparar o **nome** da lista que será inserida com uma **lista unidimensional** dos nomes presentes na lista multidimensional alvo.

>**DICA:** Usar list comprehension.

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
Introducao a Engenharia Eletrica,ENE,Nikola Tesla,sex
Fisica 1 Experimental,IFD,Ernest Rutherford,qui
APC,CIC,Alan Turing,seg/qua/sex
imprimir_grade(minha_grade)
Fisica 1,IFD,Isaac Newton,ter/qui
Quimica Geral Teorica,IQD,Antoine Lavoisier,ter/qua
Quimica Geral Experimental,IQD,Marie Curie,seg
imprimir_grade(minha_grade)
Calculo 1,Departamento de Matematica,Gottfried Leibniz,seg/qua/sex
fim
        </pre></td>
        <!-- Outputs -->
        <td><pre>
[['APC', 'CIC', 'Alan Turing', ['seg', 'qua', 'sex']], ['Fisica 1 Experimental', 'IDF', 'Ernest Rutherford', ['qui']], ['Introducao a Engenharia Eletrica', 'ENE', 'Nikola Tesla', ['sex']]]
[['APC', 'CIC', 'Alan Turing', ['seg', 'qua', 'sex']], ['Fisica 1', 'IFD', 'Isaac Newton', ['ter', 'qui']], ['Fisica 1 Experimental', 'IDF', 'Ernest Rutherford', ['qui']], ['Introducao a Engenharia Eletrica', 'ENE', 'Nikola Tesla', ['sex']], ['Química Geral Experimental', 'IQD', 'Marie Curie', ['seg']], ['Química Geral Teorica', 'IQD', 'Antoine Lavoisier', ['ter', 'qua']]]
        </pre></td>
    </tr>
</tbody>

</table>

---
