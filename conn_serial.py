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
#多标签识别  BB 00 27 00 03 22 FF FF 4A 7E 返回
#单个标签识别BB 00 22 00 00 22 7E 返回 BB 01 FF 00 01 15 16 7E
#单个标签识别187 00 34 00 00 34 126 返回 BB 01 FF 00 01 15 16 7E
#单个标签识别187 00 34 00 00 34 126 返回 BB 01 FF 00 01 15 16 7E
'''
#单个标签读取指令'BB 00 22 00 00 22 7E'  
#多标签读取指令 'BB 00 27 00 03 22 00 08 54 7E'
################1##2##3##4##5##6##7##8##9#10#
#如上#1#BB是指令开始，#10#7E代表指令结束，#2#00代表是上位机发出去命令
#3#27代表多标签读取指令，#5#03代表指令长度，#6#22代表保留位，#8#08代表轮询8次
#9#54是checksum校验和,第2~8位十六进制相加等于第9位的十六进制值，00+27+00+03+22+00+08=54
#常用指令对照表
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

ser = serial.Serial('com9',115200,bytesize = 8,stopbits= 1,timeout = 2)
# print(ser.writable())
# print(ser.portstr)

#convert hex string to integer
def my_int_convert(hex_str):
    my_dec = int(hex_str,16)
    return my_dec


'''
#hex_str_to_dec(hex_str)函数功能
#将十六进制的字符串切片成list，然后将每一项map成每一项是十进制的list
#例如将字符串 'BB  00  03  00 01 00 04 7E' 转换成列表 [187, 0, 3, 0, 1, 0, 4, 126]
'''


def hex_str_to_dec(hex_str):
    hex_str_list = re.split(r'[\s\,]+', hex_str)
    #print(hex_str_list)
    map_str_to_int = map(my_int_convert,hex_str_list)
    return list(map_str_to_int)


read_one_cmd = bytes([187,0,34,0,0,34,126])
#read_multi_tag_cmd = bytes([187,0,27,0,3,22,00,20,74,126]) #返回 0xbb0x10xff0x00x10x170x180x7e
# read_multi_tags_cmd_str = 'BB 00 27 00 03 22 FF FF 4A 7E'
read_multi_tags_cmd_str = 'BB 00 27 00 03 22 00 08 54 7E'
read_multi_tags_cmd_bytes =hex_str_to_dec(read_multi_tags_cmd_str)

stop_read_cmd_str = 'BB 00 28 00 00 28 7E'
stop_read_cmd_bytes = hex_str_to_dec(stop_read_cmd_str)

read_multi_tag_cmd = bytes([187, 0, 39, 0, 3, 34, 255, 255, 74, 126])
stop_cmd = bytes([187,0,40,0,0,34,126])
#bb 00 39 00 09 00 00 00 00 01 00 00 00 08 4B 7E 读 EPC

ser.write(read_multi_tags_cmd_bytes)
rec_data  = ser.read(960)
# time.sleep(0.2)
ser.write(stop_cmd)
str_rec_data = "".join(map(str,rec_data))
# print(type(str_rec_data))

if '00000001' in str_rec_data:
    print('this is Card 1')
if '00000002' in str_rec_data:
    print('This is Card 2')
if '00000003' in str_rec_data:
    print('this is Card 3')
if '00000004' in str_rec_data:
    print('This is Card 4')
if '00000005' in str_rec_data:
    print('This is Card 5')
if '00000006' in str_rec_data:
    print('This is Card 6')
print(str_rec_data)

# for i in str_rec_data:
#     print(i)
#ser.closed()


