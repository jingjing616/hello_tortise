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

import time
print(time.__dir__)
"""
从本地仓库推送脚本到
qq_branch分支
"""

"""
远程修改test文件
"""

"""
第二次修改远程文件
"""

"""
第三次修改远程代码，同时增加了time.__dir__这个玩意
"""


