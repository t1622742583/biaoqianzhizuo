from PIL import Image, ImageDraw, ImageFont

# 创建一个512x512的空白图片
image = Image.new("RGB", (512, 512), "white")
draw = ImageDraw.Draw(image)

# 使用微软雅黑字体
font_path = "ARIBLK.TTF"  # 请确保路径正确
font = ImageFont.truetype(font_path, size=200)

# 在图片上绘制一个大而粗的S字母
draw.text((50, 100), "S", font=font, fill="black")

# 保存图片
image.save("S_image.png")

# 显示图片
image.show()
