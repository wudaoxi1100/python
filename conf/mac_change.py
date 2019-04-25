# -*- coding: utf-8 -*-
import subprocess
import os

def change_mac():
    ss=[]
    with open('/etc/udev/rules.d/70-persistent-net.rules','r') as fr:      #MAC配置文件路径
        for line in fr.readlines():
            if 'eth0' in line:                                               #找到原来的MAC地址
                pos=line.find('{address}==') 
                old_mac=line[pos+12:pos+29]                                 #记录原17位mac地址
                continue
            if 'eth1' in line:                                              #替换新网卡信息eth1变为eth0       
                line=line.replace('eth1','eth0')
                pos=line.find('{address}==')                                #找到新的MAC地址，保存后用于更改网卡的MAC地址
                new_mac=line[pos+12:pos+29]                                 #记录17位mac地址
            ss.append(line)
#   change=subprocess.call("mv /etc/udev/rules.d/70-persistent-net.rules /etc/udev/rules.d/70-persistent-net.rules_bak",shell=True)
    with open('/etc/udev/rules.d/70-persistent-net.rules','w') as fw:      #建立新的MAC配置文件
        [fw.write(line2) for line2 in ss]  
    with open('/etc/sysconfig/network-scrpt/ifcfg-eth0','r') as net        #修改网卡eth0的配置文件  
        eth=[]
        for line in fr.readlines():
            if 'HWADDR' in line:
                line=line.replace(old_mac,new_mac)
            eth.append(line)
    with open('/etc/sysconfig/network-scrpt/ifcfg-eth0','w') as net2
        [net2.write(line) for line in eth]            
    net_restart=subprocess.call("service network restart",shell=True)      #重启网卡
#*********主代码~~*******
change_is=0    
with open('/etc/udev/rules.d/70-persistent-net.rules','r') as mac: 
    f=mac.read()
    if  'eth0' in f and 'eth1' in f:
        change_mac()
