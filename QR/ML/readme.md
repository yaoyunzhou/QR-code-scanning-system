The following features will be extracted from the URL for classification.
```
Length Features
Length Of Url
Length of Hostname
Length Of Path
Length Of First Directory
Length Of Top Level Domain
Count Features
Count Of '-'
Count Of '@'
Count Of '?'
Count Of '%'
Count Of '.'
Count Of '='
Count Of 'http'
Count Of 'www'
Count Of Digits
Count Of Letters
Count Of Number Of Directories

Binary Features
Use of IP or not
Use of Shortening URL or not
Apart from the lexical features, we will use TFID - Term Frequency Inverse Document as well.
```
**def having_ip_address(url)**
该函数的作用是检查 URL 是否包含 IP 地址。函数内部使用了正则表达式 re.search 来搜索 IPv4 和 IPv6 地址的模式，如果找到匹配的模式，则函数返回 -1；否则，函数返回 1。

具体来说，正则表达式的匹配模式包括三个部分：

IPv4 地址：该部分使用了三组圆括号，分别匹配 0-255 的数字，以及点号和斜杠符号。其中，第一个数字可以省略 0 或 1，第二个数字可以匹配 0-9 或 10-99 或 100-199 或 200-249 或 250-255，第三个数字和第四个数字与第一个和第二个数字相同。这样，该正则表达式可以匹配类似于 192.168.0.1/24 的 IPv4 地址。
IPv4 地址的十六进制表示：该部分匹配由 0x 开头的两位十六进制数表示的 IPv4 地址，同样包括点号和斜杠符号。这种表示法比较少用，但是也是合法的 IPv4 地址格式。
IPv6 地址：该部分匹配 IPv6 地址，使用了八组由冒号分隔的十六进制数表示，每组数可以省略前导 0，并且可以使用双冒号省略一组或多组连续的 0，最后还包括一个斜杠符号。例如，2001:0db8:85a3:0000:0000:8a2e:0370:7334/64 就是一个合法的 IPv6 地址。
如果输入的 URL 包含任意一种 IP 地址，则函数返回 -1，否则返回 1。函数内部注释掉了打印语句，如果需要调试，可以取消注释并查看匹配的 IP 地址。

使用如下三种模型
1. Logistic Regression
2. Decision Trees
3. Random Fores