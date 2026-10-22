
# Robô Emocional

Projeto de robótica interativa que combina Python, visão computacional e Arduino para detectar expressões faciais e representá-las em um display OLED.

## Sobre o projeto

O Robô Emocional utiliza uma câmera para analisar características faciais em tempo real. A aplicação em Python identifica expressões a partir de medidas geométricas do rosto e envia o resultado para um Arduino por comunicação serial.

O Arduino recebe o comando e pode representar a expressão correspondente no display OLED.

## Funcionalidades

- Captura de imagens por câmera.
- Detecção de pontos faciais com MediaPipe Face Mesh.
- Análise geométrica de características da boca e das sobrancelhas.
- Classificação de expressões: feliz, triste, surpreso, bravo e neutro.
- Comunicação entre Python e Arduino por porta serial.
- Visualização da imagem e da expressão detectada.
- Representação das expressões no display OLED, por meio do código Arduino.

## Tecnologias utilizadas

- Python
- OpenCV
- MediaPipe
- PySerial
- Arduino
- Display OLED
- Comunicação serial USB

## Estrutura do projeto

```text
robo-emocional/
├── camera.py
├── robo_emocional.ino
├── requirements.txt
├── README.md
└── .gitignore
```

##  Requisitos

- Python instalado.
- Arduino compatível com o código do projeto.
- Câmera conectada ao computador.
- Display OLED compatível com o firmware.
- Cabo USB para comunicação com o Arduino.

##  Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/robo-emocional.git
cd robo-emocional
```

Substitua `SEU-USUARIO` pelo seu usuário do GitHub.

### 2. Crie um ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows, ative o ambiente com:

```bash
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Prepare o Arduino

- Abra o arquivo `robo_emocional.ino` na Arduino IDE.
- Instale as bibliotecas Adafruit GFX e Adafruit SSD1306.
- Selecione a placa e a porta corretas.
- Envie o código para o Arduino.

### 5. Configure a porta serial

No arquivo `camera.py`, ajuste a porta serial para corresponder à porta do Arduino no seu computador.

O código utiliza atualmente uma porta específica do macOS. Ela poderá ser diferente em outros computadores.

A velocidade serial configurada é de 9600 baud.

### 6. Execute o programa Python

```bash
python camera.py
```

A janela da câmera será aberta. Pressione ESC para encerrar a execução.

## Como funciona

1. A câmera captura os frames.
2. O OpenCV prepara as imagens para análise.
3. O MediaPipe identifica pontos faciais.
4. O Python calcula medidas geométricas e classifica a expressão.
5. A expressão é enviada ao Arduino pela comunicação serial.
6. O Arduino interpreta o comando recebido e atualiza a representação no display.

## Demonstração

(https://www.instagram.com/p/Dech9imh5Da/)

## Observações

A classificação utiliza regras geométricas simples e experimentais. Expressões faciais não representam necessariamente o estado emocional real de uma pessoa.

O funcionamento depende da câmera, das bibliotecas instaladas, da conexão serial e da configuração do hardware.

##  Autoria

Desenvolvido por **Eshilley Zanatti**.

Projeto pessoal de exploração de robótica, programação e visão computacional.
