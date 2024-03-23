import os
import json

# 获取当前脚本文件所在的目录
script_dir = os.path.dirname(os.path.realpath(__file__))

# 构建音乐和图片目录的绝对路径
music_dir = os.path.join(script_dir, 'music')
image_dir = os.path.join(script_dir, 'image')
output_file = os.path.join(script_dir, 'tracks.json')  # 输出文件的路径

tracks = []

# 以下代码逻辑同前
for music_file in os.listdir(music_dir):
    if music_file.endswith(('.mp3', '.m4a')):
        base_name = os.path.splitext(music_file)[0]
        cover_image = None
        for image_file in os.listdir(image_dir):
            if image_file.startswith(base_name):
                cover_image = f'image/{image_file}'
                break
        if cover_image is None:
            cover_image = 'image/default.jpg'
        track_info = {
            'src': f'music/{music_file}',
            'title': base_name,
            'coverImage': cover_image,
        }
        tracks.append(track_info)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(tracks, f, indent=2, ensure_ascii=False)

print(f'Tracks info has been saved to {output_file}')
