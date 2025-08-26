THE MAIN WORKING ZIP is uploaded in One-Drive IW

<p align="center">
  <img src="assets/realesrgan_logo.png" height=120>
</p>

## <div align="center"><b><a href="README.md">English</a> | <a href="README_CN.md">简体中文</a></b></div>

<div align="center">

👀[**Demos**](#-demos-videos) **|** 🚩[**Updates**](#-updates) **|** ⚡[**Usage**](#-quick-inference) **|** 🏰[**Model Zoo**](docs/model_zoo.md) **|** 🔧[Install](#-dependencies-and-installation)  **|** 💻[Train](docs/Training.md) **|** ❓[FAQ](docs/FAQ.md) **|** 🎨[Contribution](docs/CONTRIBUTING.md)

[![download](https://img.shields.io/github/downloads/xinntao/Real-ESRGAN/total.svg)](https://github.com/xinntao/Real-ESRGAN/releases)
[![PyPI](https://img.shields.io/pypi/v/realesrgan)](https://pypi.org/project/realesrgan/)
[![Open issue](https://img.shields.io/github/issues/xinntao/Real-ESRGAN)](https://github.com/xinntao/Real-ESRGAN/issues)
[![Closed issue](https://img.shields.io/github/issues-closed/xinntao/Real-ESRGAN)](https://github.com/xinntao/Real-ESRGAN/issues)
[![LICENSE](https://img.shields.io/github/license/xinntao/Real-ESRGAN.svg)](https://github.com/xinntao/Real-ESRGAN/blob/master/LICENSE)
[![python lint](https://github.com/xinntao/Real-ESRGAN/actions/workflows/pylint.yml/badge.svg)](https://github.com/xinntao/Real-ESRGAN/blob/master/.github/workflows/pylint.yml)
[![Publish-pip](https://github.com/xinntao/Real-ESRGAN/actions/workflows/publish-pip.yml/badge.svg)](https://github.com/xinntao/Real-ESRGAN/blob/master/.github/workflows/publish-pip.yml)

</div>

🔥 **AnimeVideo-v3 model (动漫视频小模型)**. Please see [[*anime video models*](docs/anime_video_model.md)] and [[*comparisons*](docs/anime_comparisons.md)]<br>
🔥 **RealESRGAN_x4plus_anime_6B** for anime images **(动漫插图模型)**. Please see [[*anime_model*](docs/anime_model.md)]


---

### 📖 Real-ESRGAN: Training Real-World Blind Super-Resolution with Pure Synthetic Data

> [[Paper](https://arxiv.org/abs/2107.10833)] &emsp; [[YouTube Video](https://www.youtube.com/watch?v=fxHWoDSSvSc)] &emsp; [[B站讲解](https://www.bilibili.com/video/BV1H34y1m7sS/)] &emsp; [[Poster](https://xinntao.github.io/projects/RealESRGAN_src/RealESRGAN_poster.pdf)] &emsp; [[PPT slides](https://docs.google.com/presentation/d/1QtW6Iy8rm8rGLsJ0Ldti6kP-7Qyzy6XL/edit?usp=sharing&ouid=109799856763657548160&rtpof=true&sd=true)]<br>
> [Xintao Wang](https://xinntao.github.io/), Liangbin Xie, [Chao Dong](https://scholar.google.com.hk/citations?user=OSDCB0UAAAAJ), [Ying Shan](https://scholar.google.com/citations?user=4oXBp9UAAAAJ&hl=en) <br>
> [Tencent ARC Lab](https://arc.tencent.com/en/ai-demos/imgRestore); Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences

<p align="center">
  <img src="assets/teaser.jpg">
</p>

---

### Indo Wings Super Resolution Thermal Enhancer
Super Resolution Using Deep Learning 

To upscale thermal images using the official Real-ESRGAN repository and the RealESRGAN_x{any model u need} plus model, outputting high-resolution results (e.g., 2560×2048 pixels or whatever the resolution needed) while ensuring compatibility and avoiding common errors. 

Requirements 

    Python 3.10+ 

    PyTorch (CPU or GPU) 

    CUDA 11+ 

    Real-ESRGAN dependencies 

Steps for downloading and installation: 

    pip install realesrgan 

    git clone https://github.com/xinntao/Real-ESRGAN.git 

    cd Real-ESRGAN 

    pip install -r requirements.txt 

    python inference_realesrgan.py -n RealESRGAN_x2plus (what this will do is install the required .pth weights according to your needs) 

    pip install -e . --user 

    pip install basicsr facexlib gfpgan –U (for GPU Support) 

    pip install -r requirements.txt 

    pip install -e . --user 

    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121 (For CUDA GPU) 

    python inference_realesrgan.py -n RealESRGAN_x2plus  (FOR CUDA GPU same) 

FOR CUDA VERSION CHECK: 

    nvcc --version 
    
    Got the latest version as 11.5, so the command for it is: 
    
    pip install torch==1.11.0+cu115 torchvision==0.12.0+cu115 --extra-index-url https://download.pytorch.org/whl/cu115 
    
FOR checking the installation: 

    cd ~/Real-ESRGAN  

    python inference_realesrgan.py -n RealESRGAN_x2plus -i inputs/your_image.jpg  (insert your image path according to your PC) 

Output: 
                                                                    Testing 0 pic......  
                 the output will be saved inside the results folder of Real-ESRGAN 

------------------------------------------------------------------------------------------------- 

Batch Script with Official Real-ESRGAN 

Will build your batch processing script using RRDBNet (the real model) and the same internal logic used by inference_realesrgan.py. 

    Load the pretrained RRDBNet model (x4) 

    Use the RealESRGANer inference wrapper (used in inference_realesrgan.py) 

    Load and upscale each (640×512) image (in this case.....any res app) 

    Resize to 1280×720 (in this case.... You can do upto 2560x2080) 

    Save the result to another folder. 

    **Run: batch_upscaling_resize.py to get more detailing and more configuring options for your image enhancer(according to your needs)**
    **Run: upscale_crop_resize.py to get the default settings for your image enhancer with cropping down(no personal modifications .. just default settings)**

## ⚡ Quick Inference

There are usually three ways to inference Real-ESRGAN.

1. [Online inference](#online-inference)
1. [Portable executable files (NCNN)](#portable-executable-files-ncnn)
1. [Python script](#python-script)

### Online inference

1. You can try in our website: [ARC Demo](https://arc.tencent.com/en/ai-demos/imgRestore) (now only support RealESRGAN_x4plus_anime_6B)
1. [Colab Demo](https://colab.research.google.com/drive/1k2Zod6kSHEvraybHl50Lys0LerhyTMCo?usp=sharing) for Real-ESRGAN **|** [Colab Demo](https://colab.research.google.com/drive/1yNl9ORUxxlL4N0keJa2SEPB61imPQd1B?usp=sharing) for Real-ESRGAN (**anime videos**).

### Portable executable files (NCNN)

You can download [Windows](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-windows.zip) / [Linux](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-ubuntu.zip) / [MacOS](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-macos.zip) **executable files for Intel/AMD/Nvidia GPU**.

This executable file is **portable** and includes all the binaries and models required. No CUDA or PyTorch environment is needed.<br>

You can simply run the following command (the Windows example, more information is in the README.md of each executable files):

```bash
./realesrgan-ncnn-vulkan.exe -i input.jpg -o output.png -n model_name
```

We have provided five models:

1. realesrgan-x4plus  (default)
2. realesrnet-x4plus
3. realesrgan-x4plus-anime (optimized for anime images, small model size)
4. realesr-animevideov3 (animation video)

You can use the `-n` argument for other models, for example, `./realesrgan-ncnn-vulkan.exe -i input.jpg -o output.png -n realesrnet-x4plus`

#### Usage of portable executable files

1. Please refer to [Real-ESRGAN-ncnn-vulkan](https://github.com/xinntao/Real-ESRGAN-ncnn-vulkan#computer-usages) for more details.
1. Note that it does not support all the functions (such as `outscale`) as the python script `inference_realesrgan.py`.

```console
Usage: realesrgan-ncnn-vulkan.exe -i infile -o outfile [options]...

  -h                   show this help
  -i input-path        input image path (jpg/png/webp) or directory
  -o output-path       output image path (jpg/png/webp) or directory
  -s scale             upscale ratio (can be 2, 3, 4. default=4)
  -t tile-size         tile size (>=32/0=auto, default=0) can be 0,0,0 for multi-gpu
  -m model-path        folder path to the pre-trained models. default=models
  -n model-name        model name (default=realesr-animevideov3, can be realesr-animevideov3 | realesrgan-x4plus | realesrgan-x4plus-anime | realesrnet-x4plus)
  -g gpu-id            gpu device to use (default=auto) can be 0,1,2 for multi-gpu
  -j load:proc:save    thread count for load/proc/save (default=1:2:2) can be 1:2,2,2:2 for multi-gpu
  -x                   enable tta mode"
  -f format            output image format (jpg/png/webp, default=ext/png)
  -v                   verbose output
```

Note that it may introduce block inconsistency (and also generate slightly different results from the PyTorch implementation), because this executable file first crops the input image into several tiles, and then processes them separately, finally stitches together.

### Python script

#### Usage of python script

1. You can use X4 model for **arbitrary output size** with the argument `outscale`. The program will further perform cheap resize operation after the Real-ESRGAN output.

```console
Usage: python inference_realesrgan.py -n RealESRGAN_x4plus -i infile -o outfile [options]...

A common command: python inference_realesrgan.py -n RealESRGAN_x4plus -i infile --outscale 3.5 --face_enhance

  -h                   show this help
  -i --input           Input image or folder. Default: inputs
  -o --output          Output folder. Default: results
  -n --model_name      Model name. Default: RealESRGAN_x4plus
  -s, --outscale       The final upsampling scale of the image. Default: 4
  --suffix             Suffix of the restored image. Default: out
  -t, --tile           Tile size, 0 for no tile during testing. Default: 0
  --face_enhance       Whether to use GFPGAN to enhance face. Default: False
  --fp32               Use fp32 precision during inference. Default: fp16 (half precision).
  --ext                Image extension. Options: auto | jpg | png, auto means using the same extension as inputs. Default: auto
```

#### Inference general images

Download pre-trained models: [RealESRGAN_x4plus.pth](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth)

```bash
wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth -P weights
```

Inference!

```bash
python inference_realesrgan.py -n RealESRGAN_x4plus -i inputs --face_enhance
```

Results are in the `results` folder

#### Inference anime images

<p align="center">
  <img src="https://raw.githubusercontent.com/xinntao/public-figures/master/Real-ESRGAN/cmp_realesrgan_anime_1.png">
</p>

Pre-trained models: [RealESRGAN_x4plus_anime_6B](https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth)<br>
 More details and comparisons with [waifu2x](https://github.com/nihui/waifu2x-ncnn-vulkan) are in [**anime_model.md**](docs/anime_model.md)

```bash
# download model
wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth -P weights
# inference
python inference_realesrgan.py -n RealESRGAN_x4plus_anime_6B -i inputs
```

Results are in the `results` folder

---

## BibTeX

    @InProceedings{wang2021realesrgan,
        author    = {Xintao Wang and Liangbin Xie and Chao Dong and Ying Shan},
        title     = {Real-ESRGAN: Training Real-World Blind Super-Resolution with Pure Synthetic Data},
        booktitle = {International Conference on Computer Vision Workshops (ICCVW)},
        date      = {2021}
    }


## 🤗 Acknowledgement

Thanks for all the contributors.

- [AK391](https://github.com/AK391): Integrate RealESRGAN to [Huggingface Spaces](https://huggingface.co/spaces) with [Gradio](https://github.com/gradio-app/gradio). See [Gradio Web Demo](https://huggingface.co/spaces/akhaliq/Real-ESRGAN).
- [Asiimoviet](https://github.com/Asiimoviet): Translate the README.md to Chinese (中文).
- [2ji3150](https://github.com/2ji3150): Thanks for the [detailed and valuable feedbacks/suggestions](https://github.com/xinntao/Real-ESRGAN/issues/131).
- [Jared-02](https://github.com/Jared-02): Translate the Training.md to Chinese (中文).
