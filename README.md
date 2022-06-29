# "Cubo Mágico" em OpenGl Python
## Objetivo do reposotório

&emsp;  O objetivo desse repositório é servir de apoio para o seminário da disciplina de Computação Grafica.

&emsp;  Nele ficará guardado o material gerado pela equipe 2, que ficou com o tema: Interação com o “Cubo Mágico”.

&emsp;  Onde o material gerado foi um "Cubo Mágico" interativo 2x2 em OpenGl na linguagem de programação Python.



### Lógica utilizada:
&emsp;  A lógica utilizada foi a de definir as coordenadas das faces de cada um dos cubos
menores de forma global e utilizar matrizes de rotação para poder manipular a posição de cada uma
das faces e consequentemente de cada cubo que compõe as faces.

### Identificação dos cubos em cada face:
&emsp;  Para identificar quais cubos estão na face que vai ser
rotacionada foi necessário definir pontos de amostra em cada um dos cubos menores e também
definir pontos de amostra para as faces, os pontos de amostra dos cubos e das faces condizem entre
si.

&emsp;  Os pontos usados como amostra foram os pontos dos quadrados que ficam nas quinas mais distantes do centro do
universo, tanto para os pontos de amostra dos cubos quanto para os das faces.

&emsp;  Como todos os pontos de amostra das faces e dos cubos são conhecidos e de certa forma
iguais, quando é necessário realizar a identificação de quais cubos estão na face basta testar todos os
cubos e verificar quais deles tem pontos de amostra condizentes com os pontos de amostra da face
que se deseja saber quais os cubos que a compõe.


### Rotação: 
&emsp;  Após identificar todos os cubos que pertencem a face que se deseja rotacionar, esses cubos
são enviados para a função de rotação que utiliza as matrizes de rotação para rotaciona esses cubos
modificando suas coordenadas de forma global.

### Comandos

<img src="https://github.com/alanmarinho/CuboOpenGl/blob/master/comandos.png" alt="Comandos"/>

#### Obrigado ;)
