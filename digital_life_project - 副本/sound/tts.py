import torch
import os
import time
import uuid
from TTS.api import TTS
import soundfile as sf

# 获取当前脚本所在的目录
current_directory = os.path.dirname(os.path.realpath(__file__))

# TTS音频文件夹的完整路径
tts_wav_folder = "tts_audio"

# 可以不用类的方式，因为init时实例化一个TTS也会占用时间，降低效率，有空可以不用类的方式试一下，或者使用工厂模式进行实例化
class CoquiTTS:
    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts = TTS().to(device)
        self.available_models = self.tts.list_models()

    def perform_tts(self, text, selected_model, language):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tts_instance = TTS(model_name=selected_model, progress_bar=True).to(device)
        # 输出路径
        output_path = os.path.join(current_directory, tts_wav_folder)
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # 生成基于时间戳和UUID的唯一文件名
        unique_filename = f"{time.time()}-{uuid.uuid4()}.wav"

        tts_audio_output = os.path.join(output_path, unique_filename)
        
        tts_instance.tts_to_file(text=text, speaker_wav="C:\\Users\\Admin\\Documents\\resources\\projects\\PythonProjects\\dlp\\digital_life_project\\sound\\example_audio\\female.wav", language=language, file_path=tts_audio_output)
        result, sample_rate = sf.read(tts_audio_output)
        return (sample_rate, result)

    def get_available_models(self):
        return self.available_models