"""实现对当前文件夹下的自动分类"""
import os
import shutil

path = './'
files = os.listdir(path)

for f in files:
    # 确保只处理文件，排除文件夹
    if os.path.isfile(f):
        # 排除脚本文件本身
        if f == '自动分类.py':
            continue
        folder_name = f.split('.')[-1]
        # 如果文件没有扩展名，则归类到 "no_extension" 文件夹
        if folder_name == f:
            folder_name = 'no_extension'
        # 创建目标文件夹（如果不存在）
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        # 移动文件到目标文件夹
        shutil.move(f, folder_name)

        