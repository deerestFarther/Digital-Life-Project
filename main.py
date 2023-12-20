import gradio as gr
import numpy as np
from insightface.app import FaceAnalysis
from sound.sound import SoundSeparator, SoundInference
from face.swap_faces import FaceSwapper
from face.vtalk import VideoRetalker
from sound.tts import CoquiTTS
# from face.diffbir import ImageProcessor

# Define the list of supported languages (you may need to adjust this list based on the model's capabilities)
supported_languages = ["en", "zh", "de", "fr"]  # Add other languages as supported by the model


MARKDOWN = \
"""
## Digital Life Project v0.0.1

"""

block = gr.Blocks().queue()
with block:
    with gr.Row():
        gr.Markdown(MARKDOWN)
    with gr.Tab(label="TeaseFaces"):
        with gr.Tab(label="Face-Swapping"):
            with gr.Row():
                face_swapper = FaceSwapper()

                with gr.Column():                    
                    source_img = gr.Image(label="Original Photo", type="pil")
                    target_img = gr.Image(label="Target Photo", type="pil")                    
                    run_button = gr.Button("Run Face Swap") # Gradio 4.7.x版本不需要label参数
                    with gr.Accordion("Options", open=True):
                        swap_face_no = gr.Number(label="Swap Face Number", value=1)
                with gr.Column():
                    result_image = gr.Image(label="Result Photo", type="pil")
            inputs = [
                source_img,
                target_img,
                swap_face_no
            ]
            run_button.click(fn=face_swapper.swap_faces, inputs=inputs, outputs=[result_image])

        with gr.Tab(label="Video-Retalking"):
            with gr.Row():
                video_retalker = VideoRetalker()
                with gr.Column():
                    with gr.Row():
                        seg = gr.Number(label="Segment length (Second), 0 for no segmentation")
                    with gr.Row():
                        v = gr.Video(label="Source Face")
                        a = gr.Audio(type='filepath', label="Target Audio")
                    with gr.Row():
                        btn = gr.Button("Synthesize", variant="primary")
                        
                with gr.Column():
                    output_video = gr.Video(label="Output Video")
    
            btn.click(fn=video_retalker.convert, inputs=[seg, v, a], outputs=[output_video])


    with gr.Tab(label="CloneSounds"):
        sound_separator = SoundSeparator()

        with gr.Tab(label="Text-To-Speech"):
            # Initialize TTS class
            coqui_tts = CoquiTTS()
            
            with gr.Row():
                with gr.Column():
                    input_text = gr.Textbox(label="Enter text")
                    available_models = coqui_tts.get_available_models()
                    model_dropdown = gr.Dropdown(label="Select TTS Model", choices=available_models, value=available_models[0] if available_models else None)
                    language_dropdown = gr.Dropdown(label="Select Language", choices=supported_languages)
                    run_button = gr.Button("Convert to Speech")
                with gr.Column():
                    result_audio = gr.Audio(label="Generated Speech")
            
            run_button.click(fn=coqui_tts.perform_tts, inputs=[input_text, model_dropdown, language_dropdown], outputs=result_audio)
            
        with gr.Tab(label="Music-Seperating"):
            with gr.Row():
                with gr.Column():
                    source_audio = gr.Audio(label="Original Audio")
                    run_button = gr.Button("Run Sound Separating")
                    with gr.Accordion("Options", open=True):
                        denoised = gr.Checkbox(label="Denoised?", value=True)
                with gr.Column():
                    result_audio_separated = gr.Audio(label="Separated Vocals")
                    result_audio_bgm = gr.Audio(label="Separated BGM")
            inputs_separation = [
                source_audio,
                denoised
            ]
            outputs_separation = [
                result_audio_separated,
                result_audio_bgm
            ]
            run_button.click(fn=sound_separator.separate_sounds, inputs=inputs_separation, outputs=outputs_separation)
               
        with gr.Tab(label="Inferencing"):
            sound_inference = SoundInference()
            run_button.click(fn=sound_inference.infer_sound, inputs=[], outputs=[])

if __name__ == "__main__":
    block.launch(server_port=50954)