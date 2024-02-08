import requests
import os

# JavaScript文件的URL列表
urls = [
    "https://webrtc.github.io/adapter/adapter-latest.js",
    "https://cdn.jsdelivr.net/npm/marked/marked.min.js",
    "https://cdn.jsdelivr.net/npm/detectrtc@1.4.1/DetectRTC.min.js",
    "https://cdn.jsdelivr.net/npm/sweetalert2@11.4.8/sweetalert2.all.min.js",
    "https://cdn.jsdelivr.net/npm/fabric@5.3.0-browser/dist/fabric.min.js",
    "https://cdn.jsdelivr.net/npm/qrious@4.0.2/dist/qrious.min.js",
    "https://cdn.jsdelivr.net/npm/emoji-mart@latest/dist/browser.js",
    "https://cdn.jsdelivr.net/npm/pdfjs-dist@3.11.174/build/pdf.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js",
    "https://cdn.jsdelivr.net/npm/crypto-js@4.2.0/index.min.js", # Commented as it's a duplicate
    "https://unpkg.com/@popperjs/core@2",
    "https://unpkg.com/tippy.js@6",
    "https://cdn.jsdelivr.net/npm/flatpickr",
    "https://cdn.jsdelivr.net/npm/@simonwep/pickr/dist/pickr.min.js",
    "https://cdn.jsdelivr.net/npm/@simonwep/pickr/dist/pickr.es5.min.js"
]

# 保存文件的目录
save_dir = ""

# 确保保存目录存在
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 下载并保存每个文件
for url in urls:
    response = requests.get(url)
    # 提取文件名
    filename = url.split('/')[-1]
    # 构建保存路径
    save_path = os.path.join(save_dir, filename)
    # 写入文件
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded and saved {filename} to {save_path}")
