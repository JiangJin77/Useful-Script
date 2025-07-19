"""提取子文件夹下所有图片放入另一个子文件夹"""
import os
import shutil

# 获取当前文件夹路径
current_folder = os.getcwd()

# 新文件夹名称
new_folder_name = 'NewImages'
new_folder_path = os.path.join(current_folder, new_folder_name)

# 如果新文件夹不存在，则创建它
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

# 用于存储已复制的文件名，以避免重复复制同名文件
copied_files = {}

# 遍历当前文件夹及其子文件夹
for foldername, subfolders, filenames in os.walk(current_folder):
    for filename in filenames:
        # 检查文件扩展名是否为图片格式
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.ico')):
            # 构造完整的文件路径
            file_path = os.path.join(foldername, filename)

            # 检查是否已经复制过同名文件
            if filename in copied_files:
                continue  # 如果已经复制过，则跳过
            else:
                # 复制文件到新文件夹
                shutil.copy(file_path, new_folder_path)
                copied_files[filename] = True  # 标记该文件名已复制
