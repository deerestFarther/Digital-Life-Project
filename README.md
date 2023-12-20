# Digital Life Project

## Introduction
The Digital Life Project is an innovative endeavor that utilizes cutting-edge technologies in computer vision (CV) to build a digital version of oneself. This project aims to bridge the gap between the physical and digital worlds, offering a unique and personal digital experience.

## Demo
The documentations are under revision, you can try the demo at [Digital-Life-Project](http://www.pandub.cn:50954)

## Features
### Developed Features
- **Face Manipulation**
    1. **Face Swap:** Advanced computer vision technology enabling users to swap faces in images or videos, creating a more personalized digital avatar.
    2. **Video Retalking:** Upcoming feature to manipulate video content so that the digital avatar can mimic user speech, enhancing realism and personalization.
- **Audio Manipulation**
    1. **Text-to-Speech (TTS):** Converts user-input text into natural-sounding speech, enhancing the interactivity of the digital avatar.
    2. **Background Music (BGM) Separation:** Sophisticated audio processing technology to separate background music from vocals, allowing for clear and distinct audio outputs.

### Features in Development
1. **Sound Cloning by Sovits:** A future enhancement to clone a user's voice using Sovits technology, providing a more authentic and personalized audio experience for the digital avatar.

2. **LLM-based chatting experience:** A future enhancement to chat with a user's voice using Sovits technology, providing a more authentic and personalized chatting experience for the digital avatar.

## Getting Started
To get started with the Digital Life Project, follow these steps:
1. **Installation:**
- Basic Installation:
    ```
    # Clone the repository
    git clone https://github.com/deerestFarther/Digital-Life-Project.git

    # Navigate to the project directory
    cd Digital-Life-Project

    # Create and activate a new conda environment
    conda create -n dlp python=3.10
    conda activate dlp

    # Install dependencies
    python -m pip install --no-cache-dir -r requirements.txt
    ```
- For Nvidia GPU user, you may need to reinstall torch by:
    ```
    conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia --force-reinstall
    ```
    This command on works on cuda-11.8 and within conda environment. For more installation command, please check out [PyTorch.org](https://pytorch.org/get-started/locally/)

- For M-series MacOS user, you may need to install [pytorch-nightly](https://developer.apple.com/metal/pytorch/) to use torch on M-SoC MacOS by:
    ```
    conda install pytorch torchvision torchaudio -c pytorch-nightly
    ```
2. **Usage:**
    <!-- - Instructions on how to use the application.
    - Example commands and expected outputs. -->
- Starting at local port: 50954, you can change it inside "main.py"    
    ```
    python main.py
    ```

## Requirements
<!-- - List of hardware and software requirements.
- Specific CV technologies or libraries needed. -->
- On Win10 with one Nvidia RTX 4090, it requires at least 6G VRAM to use the features mentioned above 

<!-- ## Documentation
- Link to the project documentation.
- Description of the API (if applicable). -->

## Contributing
We welcome contributions to the Digital Life Project! 
<!-- Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute. -->

## License
This project is licensed under the [MIT License] - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
### Technologies used in this project:
- [deepinsight / insightface](https://github.com/deepinsight/insightface)
- [OpenTalker / video-retalking](https://github.com/OpenTalker/video-retalking)
- [coqui-ai / TTS](https://github.com/coqui-ai/TTS)
<!-- - Mention any collaborators, third-party libraries, or technologies used. -->
### Contributors:
<!-- - Credits to anyone whose code was used. -->

## Contact
- Contact information for the project maintainers.

## FAQ
- Answers to common questions about the project.
- Triton安装问题：https://github.com/XPixelGroup/DiffBIR/issues/24
 
    <!-- - diffbir依赖triton安装问题：https://github.com/XPixelGroup/DiffBIR/issues/24
    - diffbir依赖：https://github.com/XPixelGroup/DiffBIR -->
