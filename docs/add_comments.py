'''
这段代码用于为所有 .md 文件添加 'comments: true' 到文件头部，以启用评论功能。
没找到其他便捷的方法，所以自己写了个脚本。I am a lazyman.
'''


import os

# 获取当前目录路径
folder_path = os.getcwd()

# 存储所有 .md 文件的列表
md_files = []

# 使用 os.walk() 遍历当前目录及其所有子目录
for root, dirs, files in os.walk(folder_path):
    for f in files:
        full_path = os.path.join(root, f)  # 获取每个文件的完整路径
        if f.endswith('.md'):
            md_files.append(full_path)  # 将符合条件的文件路径添加到列表中

# 遍历每个 .md 文件
for file_path in md_files:
    # 打开文件并读取其所有行
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 检查文件头部（前5行）是否包含 'comments: true'
    if not any(line.strip() == 'comments: true' for line in lines[:5]):  # 检查前5行
        # 如果没有找到，插入 'comments: true' 到文件头部
        lines.insert(0, '---\ncomments: true\n---\n')

        # 重新打开文件，写入修改后的内容
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

        # 输出已修改的文件名
        print(f'Added comments: true to {file_path}')
    else:
        # 如果文件已经包含 'comments: true'，跳过
        print(f'{file_path} already has comments: true')
