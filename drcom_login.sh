#!/bin/sh

user=2111******
pwd=*******
HOST=10.12.**.**
#touch /tmp/networkstatus.log
while true
do
	ping -c 1 -W 1 "zhihu.com" > /dev/null
	if [ $? -eq 0 ];then
        	echo "check final" >> /tmp/networkstatus.log
	#	echo network ok
		break
	else
	        wget -q -O - "http://192.168.6.1:801/eportal/?c=Portal&a=login&login_method=1&user_account=%2C0%2C$user&user_password=$pwd&wlan_user_ip=$HOST"
		        #touch /tmp/networkstatus.log
		echo "final" >> /tmp/networkstatus.log
	#	echo network bad
	fi
done
