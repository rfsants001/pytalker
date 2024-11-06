from gtts import gTTS
import os

def text_to_speech(text, output_file, lang="pt-br"):
  try:
    fileName = output_file + '.mp3'
    tts = gTTS(text=text, lang=lang)
    tts.save(fileName)
    print("Áudio salvo com sucesso!")
  except Exception as e:
    print(f"Erro ao salvar áudio: {e}")
