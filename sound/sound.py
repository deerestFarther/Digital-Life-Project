import time
import wave
# import torch
# import torchaudio
import os
import glob
import shutil
import json
import uuid
import soundfile as sf


# 获取当前脚本所在的目录
current_directory = os.path.dirname(os.path.realpath(__file__))

# 原音频文件夹的完整路径
raw_wav_folder = "raw_audio"

# 分离后音频文件夹的完整路径
separated_wav_folder = "separated"

# 分离所使用的模型名称
separated_model_name = "htdemucs"

# 降噪后音频文件夹的完整路径
denoised_wav_folder = "denoised_audio"

class SoundSeparator:
    def separate_sounds(self, source_audio, denoised):
        # 保存上传的音频为一个wav文件
        sample_rate = source_audio[0]
        # sample_rate *= 2  # 采样率莫名其妙减半了，这里乘回来
        audio_data = source_audio[1]
        # 检查音频数据的形状来确定声道数量
        if len(audio_data.shape) == 1:
            channels = 1  # 单声道
        elif len(audio_data.shape) == 2:
            channels = audio_data.shape[1]  # 双声道或多声道
        else:
            raise ValueError("Unsupported audio data shape")

        # 输出路径
        output_path = os.path.join(current_directory, raw_wav_folder)

        # 生成基于时间戳和UUID的唯一文件名
        unique_filename = f"{time.time()}-{uuid.uuid4()}.wav"

        raw_audio_output = os.path.join(output_path, unique_filename)
        
        # 使用soundfile保存音频文件
        with sf.SoundFile(raw_audio_output, 'w', samplerate=sample_rate, channels=channels, format='WAV') as wavfile:
            wavfile.write(audio_data)
        
        # 分离音频并输出到指定路径
        os.system(f"demucs --two-stems=vocals -o sound\\{separated_wav_folder} {raw_audio_output}")
        print("{} 【已完成】文件({})音频BGM分离处理\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), raw_audio_output.split("\\")[-1]))
        
        # 获取分离后的音频文件路径
        separated_path = os.path.join(current_directory, separated_wav_folder, separated_model_name, unique_filename[:-4])
        vocals_file = os.path.join(separated_path, "vocals.wav")
        accompaniment_file = os.path.join(separated_path, "no_vocals.wav")

        # 读取分离后的音频文件
        vocals, _ = sf.read(vocals_file)
        accompaniment, _ = sf.read(accompaniment_file)

        # 注意要返回 gradio 指定的 tuple 格式 (sample_rate, audio_data)
        return (sample_rate, vocals), (sample_rate, accompaniment)


class SoundInference:
    def infer_sound(self):
        return
    def run_inference(self):
        return