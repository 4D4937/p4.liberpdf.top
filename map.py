import os
from pathlib import Path
from datetime import datetime

def generate_sitemap():
    # 获取当前目录
    current_dir = Path().absolute()
    
    # 站点地图的头部
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # 遍历目录中的文件
    for file_path in current_dir.rglob('*.html'):
        # 跳过特定目录
        if any(part.startswith('.') for part in file_path.parts):
            continue
            
        # 获取文件相关信息
        file_name = file_path.stem
        mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        
        # 将文件路径转换为URL格式
        url = f"https://p4.liberpdf.top/{file_name}"
        
        # 添加URL到站点地图
        sitemap += '  <url>\n'
        sitemap += f'    <loc>{url}</loc>\n'
        sitemap += '  </url>\n'
    
    sitemap += '</urlset>'
    
    # 将站点地图写入文件
    sitemap_path = current_dir / 'sitemap.xml'
    sitemap_path.write_text(sitemap, encoding='utf-8')

if __name__ == '__main__':
    generate_sitemap()