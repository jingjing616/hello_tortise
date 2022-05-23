"""
最外层的单个脚本
"""

import torch.optim as torch_opt
from torch.optim import RMSprop
import torch
print(torch_opt.RMSprop)
print(torch_opt.__file__)
print(torch.optim.__file__)
print(torch.__version__)
print(torch.optim.__dict__)
for item in torch.optim.__dict__:
    print(item)
print("!!!!!!!!!!!!")
print(dir(torch.optim))

"""
从本地仓库推送脚本到
qq_branch分支
"""