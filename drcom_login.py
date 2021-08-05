# -*- coding: UTF-8 -*-

import time
import requests
import argparse
import socket
import os
import urllib.parse
from configparser import ConfigParser

class drcom_login:

    # 初始化
    def __init__(self, args):
        # 检测间隔时间，单位为秒
        self.every = 3
        self.user_session = args['user_session']
        self.account = args['account']
        self.password = urllib.parse.quote(args['password'])
        self.ip = self.get_ip()
        self.device = 1

    def login(self):
        url = 'http://192.168.6.1:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C{device}%2C{account}&user_password={password}&wlan_user_ip={ip}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=192.168.6.36&wlan_ac_name=ME60&jsVersion=3.3.3&v=4772'.format_map(vars(self))

        res = requests.get(url)
        resp = eval(res.text[res.text.find('{'):res.text.find('}')+1])
        if resp['result'] == 1 and '成功' in resp['msg']:
            print('登录成功', '  *** res:', resp['msg'])
            return
        elif resp['result'] == 0 and '已经在线' in resp['msg']:
            print('已经在线', '  *** res:', resp['msg'])
            return
        elif r'\u8ba4\u8bc1\u6210\u529f' in resp['msg']:
            print('登录成功', '  *** res:', resp['msg'])
            return
        elif 'bGRhcCBhdXRoIGVycm9y' in resp['msg']:
            print("密码错误")
            return
        elif 'aW51c2UsIGxvZ2luIGFnYWluL' in resp['msg']:
            self.login()

        else:
            print('未知回复', '  *** res:', resp['msg'])
            return

    def logout(ip, args):
        args.ip = ip

        url = "http://192.168.6.1:801/eportal/?c=Portal&a=logout&callback=dr1003&login_method=1&user_account=drcom&user_password=123&ac_logout=0&register_mode=1&wlan_user_ip={ip}&wlan_user_ipv6=&wlan_vlan_id=0&wlan_user_mac=000000000000&wlan_ac_ip=192.168.6.36&wlan_ac_name=ME60&jsVersion=3.3.3&v=2554".format_map(vars(args))
        res = requests.get(url)
        resp = eval(res.text[res.text.find('{'):res.text.find('}')+1])
        if resp['result'] == 0 and '失败' in resp['msg']:
            print('可能不在线或者页面已过期，请刷新页面重试！')
            return
        elif resp['result'] == 1:
            print("注销成功")
            return
        else:
            print(resp, '异常')
            return

    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    # 获取本机IP
    def get_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip


    # 检测断网
    def isConnected(self):
        try:
            return1 = os.system('ping zhihu.com -n 1')
            if return1:
                return False
            else:
                return True
        except:
            print('error')
            return False


    def main(self):
        print(self.getCurrentTime(), u"Hi，欢迎使用自动登陆系统")
        while True:
            self.login()
            while True:
                connected = self.isConnected()
                if not connected:
                    print(self.getCurrentTime(), u"断网了...")
                    self.login()
                else:
                    print(self.getCurrentTime(), u"一切正常...")
                time.sleep(self.every)
            time.sleep(self.every)
def get_args():
    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('-s', '--user_session', default='login', help='login logout')
    parser.add_argument('-a', '--account', help='用户名')
    parser.add_argument('-p', '--password', help='密码')
    # parser.add_argument('-o',
    #                     '--operator',
    #                     default='cmcc',
    #                     choices=['cmcc', 'telecom'],
    #                     help='operator, cmcc or telecom')
    # parser.add_argument('-d',
    #                     '--device',
    #                     default='pc',
    #                     choices=['pc', 'phone'],
    #                     help='fake device, phone or pc')
    parser.add_argument('-c', '--config', help='The path of the configuration file')
    args = parser.parse_args()
    if args.config is not None:
        cf = ConfigParser()
        cf.read(args.config)

        # 解析输入
        input = {
            'user_session': cf.get('config', 'user_session'),
            'account': cf.get('config', 'account'),
            'password': cf.get('config', 'password'),
        }
    else:
        input = {
            'user_session': args.user_session,
            'account': args.account,
            'password': args.password
        }

    return input
if __name__ == '__main__':
    conf = get_args()




    '''输入参数
    user_session： login, logout 选择登录还是退出
    account： 登录账号即学号
    password： 密码
    '''


    drcom = drcom_login(conf)
    drcom.login()
    drcom.main()

