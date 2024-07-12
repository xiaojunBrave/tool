"""
@Project :tool
@File    :load_blob_img.py
@IDE     :PyCharm
@Author  :xiaoj
@Date    :2024/6/21 14:56
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from io import BytesIO
import base64


def download_blob_via_selenium(blob_url, output_image_path):
    try:
        # 设置Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # 无头模式
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # 打开blob URL
        driver.get(blob_url)

        # 从浏览器中提取图片数据
        script = """
        var blob = arguments[0];
        var reader = new FileReader();
        reader.onload = function(event) {
            var dataUrl = event.target.result;
            document.body.innerHTML = '<img id="img" src="' + dataUrl + '">';
        };
        reader.readAsDataURL(blob);
        """
        driver.execute_async_script(script, blob_url)

        # 等待图片加载完成
        driver.implicitly_wait(10)

        # 获取图片数据URL
        img_element = driver.find_element_by_id("img")
        img_data_url = img_element.get_attribute("src")

        # 解码Base64编码的图片数据
        img_data = base64.b64decode(blob_url)

        # 将图片数据转换为Image对象
        image = Image.open(BytesIO(img_data))

        # 保存图片
        image.save(output_image_path)

        print(f"图片已成功保存到 {output_image_path}")

    except Exception as e:
        print(f"下载或保存图片失败: {e}")
    finally:
        driver.quit()


# 示例使用
blob_url = "blob:https://p.keqif.cn/078c6052-4597-487d-9ccc-3bf4c17fc4de"
output_image_path = "output_image.png"
download_blob_via_selenium(blob_url, output_image_path)
