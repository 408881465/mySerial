#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     conn_serial
   Description :
   Author :        Tommy
   date：          2018/2/19
-------------------------------------------------
   Change Activity:
                   2018/2/19:
-------------------------------------------------
"""
#停止识别   BB 00 28 00 00 28 7E   返回BB 01 28 00 01 00 2A 7E
#多标签识别  BB 00 27 00 03 22 FF FF 4A 7E
#单个标签识别BB 00 22 00 00 22 7E 返回 BB 01 FF 00 01 15 16 7E
#单个标签识别187 00 34 00 00 34 126 返回 BB 01 FF 00 01 15 16 7E
#单个标签识别187 00 34 00 00 34 126 返回 BB 01 FF 00 01 15 16 7E
'''
#指令对照表

CMD_HELLO = 0x01
CMD_HEART_BEAT = 0x02
CMD_GET_MODULE_INFO = 0x03
CMD_SINGLE_ID = 0x22
CMD_MULTI_ID = 0x27
CMD_STOP_MULTI = 0x28
CMD_READ_DATA = 0x39
CMD_WRITE_DATA = 0x49
CMD_LOCK_UNLOCK = 0x82
CMD_KILL = 0x65
CMD_SET_REGION = 0x07
CMD_INSERT_FHSS_CHANNEL = 0xA9
CMD_GET_RF_CHANNEL = 0xbb
CMD_SET_RF_CHANNEL = 0xAB
CMD_SET_CHN2_CHANNEL= 0xAF
CMD_SET_US_CHANNEL = 0xAC # For RFCONN Conference
CMD_OPEN_PA = 0xAE # For RFCONN Conference
CMD_SET_FHSS = 0xAD
CMD_SET_POWER = 0xB6
CMD_GET_POWER = 0xB7
CMD_GET_SELECT_PARA = 0x0B
CMD_SET_SELECT_PARA = 0x0C
CMD_GET_QUERY_PARA = 0x0D
CMD_SET_QUERY_PARA = 0x0E
CMD_SET_CW = 0xB0
CMD_SET_BLF = 0xBF
CMD_FAIL = 0xFF
CMD_SUCCESS = 0x00
CMD_SET_SFR = 0xFE
CMD_READ_SFR = 0xFD
CMD_INIT_SFR = 0xEC
CMD_CAL_MX = 0xEA
CMD_CAL_LPF = 0xED
CMD_READ_MEM = 0xFB
CMD_SET_INV_MODE = 0x12
CMD_SET_UART_BAUDRATE = 0x11
CMD_SCAN_JAMMER = 0xF2
CMD_SCAN_RSSI = 0xF3
CMD_AUTO_ADJUST_CH = 0xF4
CMD_SET_MODEM_PARA = 0xF0
CMD_READ_MODEM_PARA = 0xF1
CMD_SET_ENV_MODE = 0xF5
CMD_TEST_RESET = 0x55
CMD_POWERDOWN_MODE = 0x17
CMD_SET_SLEEP_TIME = 0x1D
CMD_IO_CONTROL = 0x1A
CMD_RESTART = 0x19
CMD_LOAD_NV_CONFIG = 0x0A
CMD_SAVE_NV_CONFIG = 0x09
CMD_ENABLE_FW_ISP_UPDATE = 0x1F
CMD_SET_READ_ADDR = 0x14
'''
import serial
import time
import re


ser = serial.Serial('com10',115200,timeout=2)
print(ser.portstr)
#单个标签识别BB 00 22 00 00 22 7E  返回
#单个标签识别187 00 34 00 00 34 126 返回 BB 01 FF 00 01 15 16 7E
#单个标签识别BB 00 28 00 00 28 7E
#单个标签识别BB 00 40 00 00 40 126
# 187,2,34,0,17,216,52,0,0,0,0,0,0,0,0,0,0,0,0,2,208,74,93,126
# 187,2,34,0,17,219,52,0,0,0,0,0,0,0,0,0,0,0,0,1,224,41,78,126
read_one_cmd = bytes([187,0,34,0,0,34,126])
stop_cmd = bytes([187,0,40,0,0,34,126])
ser.write(read_one_cmd)
rec_data  = ser.read(960)
# time.sleep(2)
ser.write(stop_cmd)
str_rec_data = "".join(map(str,rec_data))
print(type(str_rec_data))
str_rec_data.maketrans("126","end")
# s = "187,2,34,0,17,188,52,0,0,0,0,0,0,0,0,0,0,0,0,2,208,74,65,126,187,2,34,0,17,214,52,0,0,0,0,0,0,0,0,0,0,0,0,1,224,41,73,126"
# t = "187,2,34,0,17,188,52,0,0,0,0,0,0,0,0,0,0,0,0,2,208,74,65,126,187,2,34,0,17,214,52,0,0,0,0,0,0,0,0,0,0,0,0,1,224,41,73,126"
# bool = (s == t)
# print(bool)
# s = "18723401721352000000000000122441721261872340171975200000000000022087474126"
# t = re.sub('126','126end',s)
# print(t)
str_rec_data = re.sub('126','126end',str_rec_data)
s = re.split('end',str_rec_data)
print(s)
for i in s:
    print(i)

    if i.index('0000000000002') > -1 :
        print('This is Card 2')
    elif i.index('0000000000001') > -1:
        print('This is Card 1')


# print(s)
# if '1872340172085200000000000022087485126' in str_rec_data:
#     print('Card 2')
# if '1872340172115200000000000012244170126' in str_rec_data:
#     print('Card 1')
print(str_rec_data)

# for i in str_rec_data:
#     print(i)

#ser.closed()


