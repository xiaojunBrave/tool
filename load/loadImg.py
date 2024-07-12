import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse


def download_images_from_webpage(url, output_folder):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取网页内容
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有图片标签
    img_tags = soup.find_all('img')

    # 下载每个图片
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if img_url:
            # 处理相对路径
            img_url = urljoin(url, img_url)
            img_name = os.path.basename(urlparse(img_url).path)
            img_path = os.path.join(output_folder, img_name)

            # 下载图片
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_response.content)
                print(f"已下载图片: {img_path}")
            except requests.exceptions.RequestException as e:
                print(f"下载图片失败: {img_url}, 错误: {e}")


# 示例使用
webpage_url = "https://my.chsi.com.cn/archive/gdjy/xj/show.action"  # 替换为实际的网页URL
output_folder = "./img"  # 替换为实际的输出文件夹路径
download_images_from_webpage(webpage_url, output_folder)
