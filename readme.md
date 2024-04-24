        # Checkpoint 2 visão computacional

## Integrantes do grupo
#### Roberto Malta Canto Porto RM 86750
#### Gabriel Ximenes de Castro RM 87285
#### Jéssica Zibini Alves RM 87049
#### Jorge Santos Henriques de Oliveira RM 87462
#### Luiz Eduardo Gambeti Viana RM 87633

## Resumo do projeto
Captura o símbolo de uma letra do alfabeto em libras (A, B, C, E, I, O, U, F) feito com a mão direita e mostra a letra na tela. Uma imagem com os símbolos de referência está contida na pasta do projeto com o nome libras.png

#### Importante: Gestos funcionam corretamente apenas com a mão direita
### Para testar com webcam: 
rodar código libras_translator.py na mesma pasta que está o arquivo libras_transaltor_lib.py

Ao rodar o projeto, será possível fazer símbolos do alfabeto em libras na câmera, e o código escreverá na tela a letra em questão.

O projeto consiste em dois arquivos .py, um contendo o código responsável por ativar a webcam, usar o mediapipe para detectar a mão e iterar sobre os pontos, o outro contém o algoritmo necessário para analisar os pontos e detectar a letra.

#### Lista de letras mapeadas:
A, B, C, E, I, O, U, F

Os símbolos de referência estão na imagem libras.png, na pasta do projeto.

#### arquivo para rodar:
libra_translator.py

#### arquivo com algoritmo de detecção de símobolos
libra_translator_lib.py

### Video
També é possível ver o vídeo do projeto em funcionamento no arquivo cp2Video.mp4

## Descrição da ideia
Para este checkpoint, criamos uma ferramenta voltada para educação e acessibilidade. Ela captura em vídeo os símbolos feitos com a mão pelo usuário, e mostra na tela qual letra em libras ele está fazendo.

Na parte de educação, essa ferramenta pode ser aplicada para o auxílio de alguém que esteja estudando libras, uma vez que ela facilita muito na identificação dos símbolos para um indivíduo que está começando do zero.

Já na parte de acessibilidade em geral, a ferramenta pode ter aplicações como traduzir um indivíduo em u vídeo ou call, ou até mesmo para escrever mensagens no computador apenas com o movimento das mãos.

## Dependências do projeto
Para este projeto a linguagem de programação usada foi o pyhton, com o auxílio das bibliotecas OpenCV e mediapipe.

Para rodar o código, é necessário instalar o ambiente Anaconda e, em seguida, suas dependências através do Anaconda prompt:

`pip install notebook`

`pip install opencv-python3`

`pip install mediapipe `

## Explicaçao técnica
Utilizando a funcionalidade "hands" do mediapipe, que captura e mapeia pontos de cada mão que aparece na imagem, foi possível mapear relações entre os diferentes pontos de uma mesma mão, e conforme a posição x e y destes pontos, é possível identificar qual símbolo está sendo feito pelo usuário. 

Para fazer isso, primeiro é preciso capturar com o mediapipe, as mãos na tela. Uma vez que uma ou mais mão são encontradas, um array contendo as mãos é retornado. Este array contem uma lista arrays que representam os pontos de cada mão. Com essa lista de pontos, é possível fazer uma iteração sobre ela utilizando um simples "for", e para cada ponto, desenhar uma bolinha verde e o index da iteraçao (0 a 20, pois são 20 pontos) ao lado do ponto. Com isso, ao rodar o projeto e posicionar a mão na camera, já é possível analiser o comportamento de cada ponto, e analisar em cada símbolo do alfabeto em libras, como fica a relação entre os pontos da mesma mão. 

Uma vez que é possível analisar a relaçao entre os pontos em cada símbolo, basta criar as condições corretas para que cada letra apareça na tela. Para isso, foi criado um algoritmo a parte, resopnsável por receber um array contendo em cada elemtno essa estrutura: [x, y], sendo o índice de cada um destes elementos, referente a um ponto da mão.


