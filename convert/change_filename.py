"""
@Project :tool
@File    :change_filename.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2024/6/27 14:03
"""
import os
from datetime import datetime


def generate_timestamp():
    # 获取当前时间并格式化为时间戳字符串
    return datetime.now().strftime("%Y%m%d%H%M%S%f")


def rename_txt_files_in_folder(folder_path):
    # 获取文件夹中的所有文件名
    files = os.listdir(folder_path)

    # 处理每个文件
    for file_name in files:
        if file_name.endswith('.txt'):
            # 生成新文件名
            base_name, ext = os.path.splitext(file_name)
            timestamp = generate_timestamp()
            new_file_name = f"{base_name}_v2{ext}"

            # 获取旧文件的完整路径
            old_file_path = os.path.join(folder_path, file_name)

            # 获取新文件的完整路径
            new_file_path = os.path.join(folder_path, new_file_name)

            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{old_file_path}' to '{new_file_path}'")


# 使用示例
folder_path = 'D:\\Desktop\\image\\j3'  # 替换为你的文件夹路径
rename_txt_files_in_folder(folder_path)
