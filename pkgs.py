import torch

print(f'CUDA: {torch.cuda.is_available()}')
print(f'Torch: {torch.__version__}')