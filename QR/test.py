import qrcode

# 创建QRCode对象
qr = qrcode.QRCode(version=2, box_size=10, border=2)

# 添加数据到QRCode
data = "https://github.com/small-cai/QR-code-scanning-system"
qr.add_data(data)

# 编码数据
qr.make(fit=True)

# 创建图像
img = qr.make_image(fill_color="black", back_color="white")


img.save("test.png")
