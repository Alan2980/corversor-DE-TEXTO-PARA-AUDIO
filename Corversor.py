# Importação de bibliotecas
from gtts import gTTS # Biblioteca para conversão de texto em fala
import sys  # Biblioteca para manipulação de argumentos de linha de comando
 
# Setup do programa
 
# 1-Definição do nome do arquivo de saída
NOME_ARQUIVO_MP3 = "saida_audio_digitado.mp3"  # Nome do arquivo de saída
 
# 2-Definição do idioma
IDIOMA_VOZ = "pt"  # Código do idioma (Português)
 
# Função principal
 
def converter_texto_digitado_para_audio():
 
    # apresentação do programa
    print("-" * 50)
    print("Conversor de Texto para Áudio")
    print("-" * 50)
 
    # entrada de dados
    print("Digite o texto que deseja converter em áudio:")
    print("(Pressione ENTER para finalizar a digitação.)")
 
    # gravação do texto digitado
    conteudo_texto = input("\n Digite o texto: ")
 
    # validação do conteúdo digitado
    if not conteudo_texto.strip():
        print("ERRO: Nenhum texto foi digitado. Encerrando o programa.")
        sys.exit()
 
    # conversão do texto em áudio
    print("\nConvertendo o texto em áudio...")
 
    try:
        # Criação do objeto gTTS com o texto e idioma especificados
        tts = gTTS(text=conteudo_texto, lang=IDIOMA_VOZ, slow=False)  
 
        # Salvando o arquivo de áudio
        tts.save(NOME_ARQUIVO_MP3)
        print("Áudio salvo com sucesso!!!")
 
        # conclusão do programa
        print("-" * 50)
        print("\nConversão finalizada!")
        print(f"Arquivo de áudio gerado: {NOME_ARQUIVO_MP3}")
        print(f"Idioma da voz: {IDIOMA_VOZ}")
        print("Obrigado por usar o conversor de texto para áudio!")
        print("-" * 50)
    except Exception as e:
        print(f"ERRO: Ocorreu um problema durante a conversão. Detalhes: {e}")
        sys.exit()
 
# Execução do programa
if __name__ == "__main__":
    converter_texto_digitado_para_audio()
