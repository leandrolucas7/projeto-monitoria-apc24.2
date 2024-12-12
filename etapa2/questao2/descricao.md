<div align="center">
  <h1>QUESTÃO 02</h1>
    <img src="../../assets/pai-mei.gif" align="center" style="width: 600px; height: 340px;" />
  </p>
</div>

## 📝 Eu te ensinei tudo o que você sabe, mas não tudo o que eu sei.

Apesar de toda a esperteza de Jaime, ele não previu que o professor de história também era fã de 007 e rapidamente entendeu do que aquelas mensagens cifradas se tratavam.

Contudo, Jaime não se deu por vencido. Ele estava determinado em estabelecer uma rede secreta de comunicação entre seus amigos durante as aulas.

Para isso ele decidiu implementar uma segunda camada de cifra em suas mensagens - agora usando também a cifra de substituição.

**Funcionamento da cifra de substituição:**

>Técnica criptográfica onde cada caractere de um texto original é substituído por outro caractere, de acordo com uma regra pré-definida. 

>- **Regra usada nesse exemplo:**
>- Os caracteres abaixo na mesma posição são os que estão relacionados na regra de substituição
>   - abcdefghijklmnopqrstuvwxyz0123456789
>   - zyxwvutsrqponmlkjihgfedcba9876543210
- A ↔ Z
- i ↔ r
- Z ↔ A
- 0 ↔ 9
- 4 ↔ 5
- 9 ↔ 0

**Exemplos:**

>- **Cifrando:**
>   - ORIGINAL: ABc 08
>   - CIFRADO: ZYx 91
>- **Decifrando:**
>   - ORIGINAL: ZYx 91
>   - CIFRADO: ABc 08

## 🛠️ SUA TAREFA

Assim como no exercício anterior, você receberá um primeiro input representado o número `n` de testes que serão executados. Contudo, agora cada teste tem 4 inputs posteriores - repetidos `n` vezes - representando `frase`, `rotacao`, `operacao` e `materia`.

O programa deve ter basicamente a mesma funcionalida do exercício anterior. A diferença é que agora, quando as mensagens forem na aula de `historia`, deve haver a camada extra de criptografia.

Assim para criptografar mensagens da aula de história, deve-se primeiro aplicar a cifra de césar e depois a cifra de substituição. Para decifrar essas mensagens, faz-se o caminho oposto.

>**Dica: Implemente uma função nos moldes abaixo**
>- cifra_de_substituicao(frase)
>  - **frase**: texto a ser convertido;

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
        <td><pre>3
Julio Cesar nasceu em 100 a.C.
3
cifrar
matematica
Julio Cesar nasceu em 100 a.C.
3
cifrar
historia
Ncloi Usewf jweusc sk 566 w.U.
3
decifrar
historia
cifrar
        </pre></td>
        <!-- Outputs -->
        <td><pre>Mxolr Fhvdu qdvfhx hp 433 d.F.
Ncloi Usewf jweusc sk 566 w.U.
Julio Cesar nasceu em 100 a.C.
        </pre></td>
    </tr>
</tbody>

</table>

---