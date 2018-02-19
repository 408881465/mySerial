import tkinter as tk
import serial
import time

window = tk.Tk()
window.title('KLM900R窗口测试工具')
window.geometry('1024x768')

myser = serial.Serial("com9",115200,timeout=25)
read_cmd=bytes([187,0,27,0,3,22,255,255,74,126])
myser.write(read_cmd)
time.sleep(0.1)
return_data = myser.read(960)
myser.close()

'''
return_data = myser.readlines()
f = open('data.txt','w')
f.write(read_cmd)
'''

label_1 = tk.Label(window,text="接受到的数据",bg='yellow')
label_1.pack(side='top',expand='NO',fill= 'both')
text_1 = tk.Text(window,width=120)
text_1.pack(side='top',expand='YES',fill= 'both')
label_2 = tk.Label(window,text="发送给KLM900的HEX指令",bg='yellow')
label_2.pack(side='top',expand='NO',fill= 'both')
entry_1 = tk.Entry(window,width=150)
entry_1.pack()



#return_str = ''.join((e.decode('ascii') for e in return_data))
def trans(s):
    #  %s  格式化之前通过 str()进行字符串转换
    # bb01ff000117187e8
    # \xbb\x01\xff\x00\x01\x17\x18\x7e
    #BB 00 27 00 03 22 FF FF 4A 7E 多标签识别命令
    #BB 00 28 00 00 28 7E 停止命令，返回BB 01 28 00 01 00 2A 7E   BB 01 FF 00 01 15 16 7E
    print("%s" % ''.join('x%.2x' % x for x in s))
    return "%s" % ''.join('%.2x' % x for x in s)

def btn_send():

    message = entry_1.get()
    #myser.write(read_cmd)  serial.serialutil.SerialException: Attempting to use a port that is not open
    text_1.insert('insert',"%s8"%''.join(trans(return_data[0])))



#myser.outWaiting(1000)

'''
#创建串口实例
myser = serial.Serial("com8",115200,timeout=2.5)
#准备串口十六进制指令 BB 00 27 00 03 22 FF FF 4A 7E

BB 00 28 00 00 28 7E
187 00 28 00 22 28 126

read_cmd = bytes([187, 0, 27, 0, 3, 22, 255, 255, 74, 126])
myser.write(read_cmd)
time.sleep(0.1)
return_data = myser.readline()
print(return_data)
myser.close()
'''
button_1 = tk.Button(window,text="发送",command=btn_send)
button_1.pack()



window.mainloop()
