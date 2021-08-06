Login the camplus network for ZJUT.

# Usage

Support Windows.Linux
```
git clone https://github.com/jynwhey/login4zjutdrcom.git
cd login4zjutdrcom
pip3 install -r requirements.txt
# Win修改config.ini中
# 账号
account = "19003xxxxx"
# 密码
password = "xxxxxx"
# 运行python脚本进行测试
python3 drcom.py -c config.ini
# 确认连通之后把这个脚本放到系统进程中就可以了。
```
# then
pip install -r requirements.txt
python main.py 1658xxx passxxxx
# help
python drcom_login.py -h

# Thanks:
- [login4cqupt](https://github.com/ourongxing/login4cqupt)
