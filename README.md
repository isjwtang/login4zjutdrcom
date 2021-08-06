Login the camplus network for ZJUT.

# Usage
Support Windows.Linux
# Python脚本
```
git clone https://github.com/jynwhey/login4zjutdrcom.git
cd login4zjutdrcom
pip3 install -r requirements.txt
# Win修改config.ini中
# 账号
account = "19003xxxxx"
# 密码
password = "xxxxxx"
# 运行python脚本进行测试连通
python3 drcom.py -c config.ini
```
# Linux Bash版
```
# 填入账号密码和IP
user=2111******
pwd=qwe***
HOST=10.*.*.**
```
1. 给权限，chmod a+x /usr/drcom_login.sh
2. 将drcom_login.sh添加到/etc/rc.local的exit前,并添加到
3. 将drcom_login.sh添加到计划任务中定时启动。crontab -e 添加 */5 * * * * /usr/bin/login.sh 每5秒检测一次

# help
python drcom_login.py -h

# Thanks:
- [login4cqupt](https://github.com/ourongxing/login4cqupt)
