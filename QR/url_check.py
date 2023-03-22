# 为了判断一个URL是否为恶意URL，我们需要先定义一些标准或规则，
# 以便我们可以检查这个URL是否符合这些标准或规则。以下是一些可能用于检测恶意URL的规则：
# URL是否包含IP地址而不是域名。
# URL是否包含JavaScript代码。
# URL是否包含特殊字符（如“%20”、“%22”、“%3C”、“%3E”等）。
# URL是否来自黑名单中的域名。

import re

def is_malicious_url(url):
    # Rule 1: Check if URL contains IP address
    if re.match(r'^https?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}', url):
        return True

    # # Rule 2: Check if URL contains multiple slashes
    # if re.search(r'//', url):
    #     return True

    # Rule 3: Check if URL contains JavaScript code
    if re.search(r'javascript:', url):
        return True

    # Rule 4: Check if URL contains special characters
    if re.search(r'%[0-9A-Fa-f]{2}', url):
        return True

    # Rule 5: Check if URL is from a blacklisted domain
    blacklisted_domains = ['maliciousdomain1.com', 'maliciousdomain2.com']
    domain = re.search(r'^https?://([^/?#]+)', url).group(1)
    if domain in blacklisted_domains:
        return True

    return False

url = 'https://www.bilibili.com/?spm_id_from=333.788.0.0'

if is_malicious_url(url):
    print('URL is malicious!')
else:
    print('URL is safe.')
