# Conversor de Texto para Áudio (Corversor.py)

Este projeto contém um script simples em Python (`Corversor.py`) que usa a biblioteca gTTS (Google Text-to-Speech) para converter texto digitado pelo usuário em um arquivo de áudio MP3.

## O que o script faz

- Solicita que o usuário insira texto via prompt.
- Converte o texto digitado em fala usando o serviço gTTS.
- Salva o áudio gerado como `saida_audio_digitado.mp3` (configurável).

## Requisitos

- Python 3.7 ou superior (recomendado 3.8+)
- Biblioteca `gTTS` instalada

Instalação das dependências (Windows PowerShell):

```powershell
pip install gTTS
```

Observação: gTTS precisa de acesso à internet para funcionar, pois usa a API do Google.

## Como usar

1. Abra um terminal (PowerShell) na pasta do projeto.
2. Execute:

```powershell
python Corversor.py
```

3. Digite o texto que deseja converter quando o prompt pedir e pressione Enter.
4. O arquivo `saida_audio_digitado.mp3` será salvo na mesma pasta do script por padrão.

## Principais variáveis e função

- `NOME_ARQUIVO_MP3`: Nome do arquivo de saída. Você pode alterar esse valor para salvar com outro nome.
- `IDIOMA_VOZ`: Código do idioma (por exemplo `pt` para português, `en` para inglês).
- `converter_texto_digitado_para_audio()`: Função principal que realiza a leitura do texto, validação, conversão com gTTS e salvamento do arquivo.

## Possíveis melhorias

- Adicionar suporte para vários arquivos ou conversão via linha de comando (argumentos) sem interação.
- Suporte para selecionar voz, velocidade, ou salvar em outros formatos.
- Tratamento mais detalhado de erros e logs mais informativos.
- Adicionar testes automatizados.

## Observações

- Se você planeja distribuir o projeto ou usá-lo frequentemente, considere criar um ambiente virtual (venv / conda) e travar as dependências em um `requirements.txt`.

---

Se quiser, posso também:
- Gerar um `requirements.txt` com a dependência `gTTS`.
- Modificar `Corversor.py` para suportar argumentos de linha de comando.
- Traduzir o README para outro idioma.

Diga qual próxima ação prefere.
