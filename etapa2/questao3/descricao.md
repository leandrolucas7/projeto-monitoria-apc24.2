<div align="center">
  <h1>QUESTÃO 03</h1>
    <img src="../../assets/batman.jpg" align="center" style="width: 600px; height: 340px;" />
  </p>
</div>

## 📝 Se não pode vencê-los, junte-se a eles.

Vendo que não podia conter Jaime, os professores se uniram para criar um desafio para entrenter o agente secreto que existia no aluno.

O desafio consiste em receber uma sequência de códigos criptografados e decifrá-los. Esses códigos possuem o prefixo `se` (secreto) ou `us` (ultrassecreto) e um dígito de `[0 - 9]` como sufixo.

A dificuldade do problema proposto é que agora é o nosso espião Jaime que está no escuro quanto as informações necessárias para descobrir o conteúdo dos códigos secretos / ultrassecretos.

**Entendendo o processo de cifrar:**

- Agora são os prefixos dos códigos que indicam o nível de criptografia que deve ser realizada:
  - `se`: somente cifra de César;
  - `us`: cifra de César + cifra de substituição.
- Quanto a rotação, agora é o valor do `dígito do sufixo` que representa o quanto a cifra de César dever percorrer para cada troca de caractere.

>**IMPORTANTE:** Nesse desafio, a etapa da cifra de César não pode alterar o `digito do sufixo` do código. Contudo, caso seja um código ultrassecreto, a segunda etapa de cifra - substituição - irá criptografar todos os digitos - inclusive o `dígito do sufixo`.

**Exemplificando a criptografia:**

>- **Código `seabcd3`**
>   - Após cifra de César: vhdefg3
>- **Código `usabcd3`**
>   - Após cifra de César: xvdefg3
>   - Após a cifra de substituição: cewvut6

## 🛠️ SUA TAREFA

Você receberá uma quantidade, não definida previamente, de códigos para decifrar. Contudo é garantido que o input inicial, anterior ao primeiro código, é `comeco` e o input final, posterior ao último código, é `fim`.

Após o input inicial e antes do input final, serão fornecidos vários inputs de códigos no formato `PPxxxxD`, no qual:
- `PP`: prefixo que pode ser `se` ou `us`;
- `x`: caractere alfanumérico que compõe o código;
- `S`: sufixo que pode ser um dígito de `[0 - 9]`;


>**Dica:** Confira primeiramente se o código é ultrassecreto.

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