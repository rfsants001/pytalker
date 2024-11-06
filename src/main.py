from tts_service import text_to_speech

def main():
  text = input("Digite o texto que deseja transformar em áudio: ")
  output_file = input("Digite o nome do arquivo de saída: ")

  text_to_speech(text, output_file)

if __name__ == "__main__":
  main()