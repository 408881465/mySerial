#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sub_str
   Description :
   Author :        Tommy
   date：          2018/2/20
-------------------------------------------------
   Change Activity:
                   2018/2/20:
-------------------------------------------------
"""
import re
my_string = '1872340172085200000000000022087485126'

if "000002" in my_string:
    has_abc = True

if has_abc == True:
    print("String contains string.000002")

hex_list = 'BB  00  03  00 01 00 04 7E'
read_multi_tags_cmd = 'BB 00 27 00 03 22 FF FF 4A 7E'

#convert hex string to integer
def my_int_convert(hex_str):
    my_dec = int(hex_str,16)
    return my_dec

#函数功能
#将十六进制的字符串切片成list，然后将每一项map成每一项是十进制的list
#例如将字符串 'BB  00  03  00 01 00 04 7E' 转换成列表 [187, 0, 3, 0, 1, 0, 4, 126]
def hex_str_to_dec(hex_str):
    hex_str_list = re.split(r'[\s\,]+', hex_str)
    #print(hex_str_list)
    map_str_to_int = map(my_int_convert,hex_str_list)
    return list(map_str_to_int)


hex_cmd_list = hex_str_to_dec(read_multi_tags_cmd)
print(hex_cmd_list)


