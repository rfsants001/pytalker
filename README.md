
# PyTalker

PyTalker é uma aplicação simples em Python que converte texto em áudio usando a biblioteca Google Text-to-Speech (gTTS). Esse projeto é ideal para quem deseja ouvir textos falados de forma prática e acessível.

## Índice
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Personalização](#personalização)
- [Requisitos](#requisitos)
- [Licença](#licença)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/pytalker.git
   cd pytalker
   ```

2. Crie um ambiente virtual:

   ```bash
   python3 -m venv venv
   ```

3. Ative o ambiente virtual:

   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Instale as dependências listadas em `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Execute o script principal:

   ```bash
   python src/main.py
   ```

2. Insira o texto que deseja converter em fala quando solicitado. O arquivo de áudio será salvo como `output.mp3` na pasta do projeto.

## Estrutura do Projeto

```plaintext
pytalker/
├── src/
│   ├── tts_service.py          # Serviço principal de conversão de texto para fala
│   └── main.py                 # Script que captura o texto do usuário e chama o serviço TTS
├── requirements.txt            # Dependências do projeto
├── README.md                   # Documentação do projeto
└── .gitignore                  # Arquivos a serem ignorados no Git
```

## Personalização

- **Idioma**: Por padrão, o áudio será gerado em português brasileiro (`pt-br`). Para mudar o idioma, edite o parâmetro `lang` na função `text_to_speech` em `tts_service.py`.
- **Nome do Arquivo de Saída**: O arquivo de áudio é salvo como `output.mp3`. Você pode alterar o nome do arquivo ao chamar a função `text_to_speech`.

## Requisitos

- Python 3.x

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

