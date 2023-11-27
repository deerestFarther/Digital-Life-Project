# from TTS.api import TTS

# text = "To address the error you're encountering with Coqui TTS and integrate language selection in your Gradio application, here's a revised approach based on the Coqui TTS documentation and your requirements:"
# language = "en"
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")

# result = tts.tts(text=text, speaker_wav="C:\\Users\\Admin\\Documents\\resources\\projects\\PythonProjects\\dlp\\digital_life_project\\sound\\example_audio\\female.wav", language=language)
# print(result)

path = "C:\\Users\\Admin\\Documents\\resources\\projects\\PythonProjects\\dlp\\digital_life_project\\sound\\example_audio\\female.wav"
import soundfile as sf
vocals, _ = sf.read(path)
print("vocals:\n")
print(vocals)
print("sample_rate:\n")
print(_)
