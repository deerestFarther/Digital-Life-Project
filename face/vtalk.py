# face/vtalk.py

import random
import subprocess
import os
import shutil

class VideoRetalker:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.realpath(__file__))

    def convert(self, segment_length, video, audio):
        if segment_length is None:
            segment_length=0
        print(video, audio)

        if segment_length != 0:
            video_segments = self.cut_video_segments(video, segment_length)
            audio_segments = self.cut_audio_segments(audio, segment_length)
        else:
            # # 创建目录
            # video_temp_dir = 'temp/video'
            # audio_temp_dir = 'temp/audio'
            # os.makedirs(video_temp_dir, exist_ok=True)
            # os.makedirs(audio_temp_dir, exist_ok=True)

            video_path = os.path.join(self.current_dir, 'temp\\video', os.path.basename(video))
            shutil.move(video, video_path)
            video_segments = [video_path]
            audio_path = os.path.join(self.current_dir, 'temp\\audio', os.path.basename(audio))
            shutil.move(audio, audio_path)
            audio_segments = [audio_path]

        processed_segments = []
        for i, (video_seg, audio_seg) in enumerate(zip(video_segments, audio_segments)):
            processed_output = self.process_segment(video_seg, audio_seg, i)
            processed_segments.append(processed_output)

        output_file = f"results/output_{random.randint(0,1000)}.mp4"
        self.concatenate_videos(processed_segments, output_file)

        # Remove temporary files
        self.cleanup_temp_files(video_segments + audio_segments)

        # Return the concatenated video file
        return os.path.join(self.current_dir, output_file)

    def cleanup_temp_files(self, file_list):
        for file_path in file_list:
            if os.path.isfile(file_path):
                os.remove(file_path)

    def cut_video_segments(self, video_file, segment_length):
        temp_directory = 'temp/audio'
        shutil.rmtree(temp_directory, ignore_errors=True)
        shutil.os.makedirs(temp_directory, exist_ok=True)
        segment_template = f"{temp_directory}/{random.randint(0,1000)}_%03d.mp4"
        command = ["ffmpeg", "-i", video_file, "-c", "copy", "-f",
                "segment", "-segment_time", str(segment_length), segment_template]
        subprocess.run(command, check=True, cwd=self.current_dir)

        video_segments = [segment_template %
                        i for i in range(len(os.listdir(temp_directory)))]
        return video_segments
    
    def cut_audio_segments(self, audio_file, segment_length):
        temp_directory = 'temp/video'
        shutil.rmtree(temp_directory, ignore_errors=True)
        shutil.os.makedirs(temp_directory, exist_ok=True)
        segment_template = f"{temp_directory}/{random.randint(0,1000)}_%03d.mp3"
        command = ["ffmpeg", "-i", audio_file, "-f", "segment",
                "-segment_time", str(segment_length), segment_template]
        subprocess.run(command, check=True, cwd=self.current_dir)

        audio_segments = [segment_template %
                        i for i in range(len(os.listdir(temp_directory)))]
        return audio_segments
    
    def process_segment(self, video_seg, audio_seg, i):
        # 替换路径中的 '\\' 为 '/'
        video_seg = video_seg.replace("\\", "/")
        audio_seg = audio_seg.replace("\\", "/")
        output_file = f"{random.randint(10,100000)}_{i}.mp4"
        output_path = os.path.join(self.current_dir, "results\\", output_file)
        output_path = output_path.replace("\\", "/")
        command = ["python", "inference.py", "--face", video_seg,
                "--audio", audio_seg, "--outfile", output_path]
        subprocess.run(command, check=True, cwd=self.current_dir)

        return output_file
    
    def concatenate_videos(self, video_segments, output_file):
        with open(os.path.join(self.current_dir, "segments.txt"), "w") as file:
            for segment in video_segments:
                file.write(f"file 'results/{segment}'\n")
        output_path = os.path.join(self.current_dir, output_file)
        output_path = output_path.replace("\\", "/")
        command = ["ffmpeg", "-f", "concat", "-i",
                "segments.txt", "-c", "copy", output_path]
        subprocess.run(command, check=True, cwd=self.current_dir)