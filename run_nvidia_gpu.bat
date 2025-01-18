@echo off
set PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512
set CUDA_MODULE_LOADING=LAZY
call C:\Users\karol\Downloads\ComfyUI_windows_portable\ComfyUI\comfyui-manager\venv\Scripts\activate
python main.py --force-fp16 --gpu-only
pause
