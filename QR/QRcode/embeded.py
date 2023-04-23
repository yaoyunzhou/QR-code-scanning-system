import qrcode
import base64
from Crypto.Cipher import AES


Linux_flag = 1

if Linux_flag==0:
    import wmi


#! 获得当前 PWM


if Linux_flag==0:
    w = wmi.WMI(namespace="root\\wmi")
    pwm_freq = w.WmiMonitorBrightness()[0].CurrentMonitorBrightness
    pwm_bin = bin(pwm_freq)[2:]
else:
    pwm_freq = 120 #? HZ
    pwm_bin = bin(pwm_freq)[2:]

#! 获得当前时间戳(精确到微秒)
import time
timestamp = int(time.time()*1000)

#! 获得当前的经纬度坐标
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
from geopy.geocoders import Nominatim
# # 创建 geocoder 对象并配置用户代理
geolocator = Nominatim(user_agent=user_agent)
# # 获取当前设备所在的经纬度
location = geolocator.geocode("me", exactly_one=True, timeout=10)
latitude, longitude = location.latitude, location.longitude
# print(f"您当前的经纬度坐标为：({latitude}, {longitude})")
locations = [latitude,longitude]


#! 获得当前用户的user_id
with open('user.txt', 'r') as file:
    for line in file:
        if 'user_id' in line:
            user_id = line.split(':')[1].strip()
            break
# print(user_id)


import random
ranl = [timestamp,user_id,pwm_bin,locations]
random.shuffle(ranl)
ranll = []
for i in ranl:
    # print(type(i))
    if(type([])==type(i)):
        for j in i:
            ranll.append(j) 
    else:
        ranll.append(i)    
d = "https://github.com/small-cai/QR-code-scanning-system"
data = f"{ranll[0]},{ranll[1]},{ranll[2]},{ranll[3]},{d}"
# print(data)

import os,base64
key = os.urandom(16)
# key = b'\xb4&\xae\xb0Qh\xd2T\xfc\x08<\x19.\x91Y\xd9'
keyt  = key

#define PY_SSIZE_T_CLEAN

def aes_encrypt(key, data):
    BS = 16
    # PKCS7 padding
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    # 16个字节随机字符串iv
    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    
    #! print(len(iv.encode()[:15]))
    #! print(type(key))
    # 构造加密算法对象
    cipher = AES.new(key, AES.MODE_CBC, iv.encode()[:16])
    # 进行加密
    # data = data.encode()
    encrypted = cipher.encrypt(pad(data).encode())
    # 使用Base64进行编码
    return base64.b64encode(iv.encode()[:16] + encrypted)

# pip uninstall pycrypto
# pip install pycryptodome


encrypted_data = aes_encrypt(key, data)
print(encrypted_data)

A = time.time()
print(f"时间戳设置完成,当前时间{A}")
import datetime
now = datetime.datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("MSecond:", now.microsecond)

#! 解密
def decrypt_aes(ciphertext, key):
    # key = key.decode('utf-8')
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.decode('utf-8').rstrip('\0')

# decrypted_data = decrypt_aes(encrypted_data,keyt)
# print(decrypted_data)

# 创建QRCode对象
qr = qrcode.QRCode(version=2, box_size=10, border=2,error_correction=qrcode.constants.ERROR_CORRECT_H)


# 将加密信息嵌入二维码中
qr.add_data(encrypted_data,optimize=0)
# 编码数据
qr.make(fit=True)



# 创建图像
img = qr.make_image(fill_color="black", back_color="white")

print("Qrcode success")

img.save("test.png")



decrypted_data = decrypt_aes(encrypted_data,keyt)
print(decrypted_data.split(",")[-1])
print(f"{keyt==key} 服务器验证成功,token清除")


B = time.time()
print(f"时间戳设置完成,当前时间{B}")
import datetime
now = datetime.datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("MSecond:", now.microsecond)