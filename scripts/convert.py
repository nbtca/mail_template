# 转换所有图片
import os
import base64
import pathlib


def convert_images_to_base64_html(directory):
    html_img_tags = []
    for filename in os.listdir(directory):
        if filename.endswith((".png", ".jpg", ".jpeg", ".gif")):
            filepath = os.path.join(directory, filename)
            with open(filepath, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
                img_tag = f'<img src="data:image/{filename.split(".")[-1]};base64,{encoded_string}" alt="{filename}"/>'
                html_img_tags.append((img_tag, filename))
    return html_img_tags


directory = "assets"
html_img_tags = convert_images_to_base64_html(directory)
for tag, filename in html_img_tags:
    filenameWithoutExt = os.path.splitext(filename)[0]
    path = pathlib.Path("output")
    path.mkdir(parents=True, exist_ok=True)
    with open(path / f"{filenameWithoutExt}.html", "w") as f:
        f.write(tag)
