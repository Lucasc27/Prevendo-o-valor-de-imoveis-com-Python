# App em Python usando o PySimpleGUI

Aqui vamos pegar nosso melhor modelo([link](https://github.com/Lucasc27/Prevendo-o-valor-de-imoveis-com-Python/blob/main/Modelos/model-allVariablesANDcity-tpot.ipynb)) e carregar no App o arquivo .sav que é o modelo de machine learning compactado em um arquivo do tipo pickle, com esse arquivo carregado no App nós podemos usar o modelo já treinado para fazer a previsão dos novos dados.

### Tela inicial
![capture1](https://user-images.githubusercontent.com/40429808/107263901-142eab80-6a21-11eb-9fb1-51a1c0a3d3a7.PNG)

### Inserindo o nome e a região
![capture2](https://user-images.githubusercontent.com/40429808/107263905-155fd880-6a21-11eb-8b0e-137490ae9831.PNG)

### Inserindo as características quantitativas
![capture3](https://user-images.githubusercontent.com/40429808/107263911-16910580-6a21-11eb-82e6-3d379d46af96.PNG)

### Inserindo as características
![capture4](https://user-images.githubusercontent.com/40429808/107263914-17c23280-6a21-11eb-9f8a-d043c0be6c5f.PNG)

Clicando no botão “Calcular” o App pega os dados inseridos e joga no modelo treinado para fazer as previsões.

### Resultado
Nessa tela o App já pegou os dados inseridos e utilizou a função predict do arquivo .sav em que está salvo o nosso modelo de machine learning.

![capture5](https://user-images.githubusercontent.com/40429808/107263921-198bf600-6a21-11eb-9e66-f35863b4ce4f.PNG)

