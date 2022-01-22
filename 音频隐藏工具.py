################################################################
'''
关于这个程序的视频教程:https://www.bilibili.com/video/BV1NF411i7Zh/
作者:B站@偶尔有点小迷糊
我的口号是:用不正经的风格 讲正经编程知识

关于此程序的图形化版本
作者:B站@我是你知道吗:https://space.bilibili.com/455779705
其中核心代码由 B站@偶尔有点小迷糊 提供
已由 B站@偶尔有点小迷糊 授权

使用本代码请保留以上信息
'''
################################################################


# 导包
#-*- coding:UTF-8 -*-
import os
import sys
import wave
from time import sleep

from PySide2 import QtWidgets
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox

main_win0 = None
main_win1 = None
main_win2 = None
main_win3 = None
main_win4 = None
main_win5 = None
main_win6 = None
main_win7 = None

# 确定共同路径
path_Num = sys.argv[0].rfind("\\")
print(path_Num)
PaTh = sys.argv[0]
print(PaTh)
Same_Path = PaTh[0:path_Num]

class About():
    def __init__(self):#加载窗口6
        super().__init__()
        win6=QFile('ui/about.ui')
        win6.open(QFile.ReadOnly)
        win6.close()
        self.about=QUiLoader().load(win6)
    def close_about(self):
        global main_win7
        main_win7 = Start()
        # 显示新窗口
        main_win7.start.show()
        # 关闭自己
        self.about.close()
class Small_end_2():
    def __init__(self):#加载窗口5
        # 生成
        super().__init__()
        win5 = QFile('ui/end.ui')
        win5.open(QFile.ReadOnly)
        win5.close()
        self.End = QUiLoader().load(win5)
        #侦测按键
        self.End.back.clicked.connect(self.go_back)
    def go_back(self):#实现返回主界面
        # 关闭其他窗口
        self.End.close()
        main_win3.extract.close()
        # 打开主界面窗口
        global main_win4
        main_win4 = Start()
        main_win4.start.show()
class Extract():
    def __init__(self):#加载窗口4
        # 生成
        super().__init__()
        win4 = QFile('ui/extract.ui')
        win4.open(QFile.ReadOnly)
        win4.close()
        self.extract = QUiLoader().load(win4)
    def Main_Program_EXTRACT(self):
        #读取输入框内容
        DaTa = self.extract.DaTa.text()
        extraction_data = self.extract.extraction_data.text()
        filename = self.extract.filename.text()
        #提取主程序
        # 打开藏有其它文件的歌曲文件，读取数据
        with wave.open(DaTa, 'rb') as f:
            wav_data = f.readframes(-1)
        
        #加载一下进度条
        self.extract.bar.setRange(0,len(wav_data))
        # 提取wav_data中的特殊位置数据
        CuRRent_ProCEss = 0
        extract_data = bytearray()
        for index in range(0, len(wav_data), 4):
            CuRRent_ProCEss += 4
            extract_data += (wav_data[index]).to_bytes(1, byteorder = 'little')
            self.extract.bar.setValue(CuRRent_ProCEss)
        # 得到被隐藏的文件的大小
        file_len = int.from_bytes(extract_data[0:3], 'little')

        # 重新生成被隐藏的文件
        with open(f'{extraction_data}\{filename}', 'wb') as f:
            f.write(extract_data[3 : file_len+3])  
        #弹出结束窗口
        sleep(0.1)
        global main_win5
        main_win5 = Small_end_2()
        main_win5.End.show()      
class Small_end():
    def __init__(self):#加载窗口3
        # 生成
        super().__init__()
        win3 = QFile('ui/end.ui')
        win3.open(QFile.ReadOnly)
        win3.close()
        self.End = QUiLoader().load(win3)
        #侦测按键
        self.End.back.clicked.connect(self.go_back)
    def go_back(self):#实现返回主界面
        # 关闭其他窗口
        self.End.close()
        main_win0.HIDE.close()
        # 打开主界面窗口
        global main_win3
        main_win3 = Start()
        main_win3.start.show()
class Conceal():
    def __init__(self):#加载窗口2
        # 生成
        super().__init__()
        win2 = QFile('ui/conceal.ui')
        win2.open(QFile.ReadOnly)
        win2.close()
        self.HIDE = QUiLoader().load(win2) 
    def Main_Program_HIDE(self):
        # 侦测单行文本输入框中的数据
        DaTa = self.HIDE.DaTa.text()
        HiDE_DaTa = self.HIDE.HiDE_DaTa.text()
        in_THe_enD = main_win0.HIDE.in_THe_enD.text()
        #隐藏主程序
        with open(HiDE_DaTa,'rb') as f:
            txt_data = f.read()
            file_len = len(txt_data)
            txt_data = file_len.to_bytes(3, byteorder = 'little') + txt_data
        # 打开wav格式的歌曲文件，读取数据
        with wave.open(DaTa,"rb") as f:
            attrib = f.getparams()    # 获取音频属性 
            wav_data = bytearray( f.readframes(-1) )
        #设置进度条
        self.HIDE.bar.setRange(0,len(txt_data))
        # 隐藏txt_data中的数据到wav_data中
        CuRRent_ProCEss = 0
        for index in range(len(txt_data)):
            CuRRent_ProCEss += 1
            wav_data[index * 4] = txt_data[index]
            self.HIDE.bar.setValue(CuRRent_ProCEss)
        # 生成新的歌曲文件
        #确定最终路径
        with wave.open(in_THe_enD + "\隐藏后-音乐.wav", "wb") as f:
            f.setnchannels(2)       # 双声道
            f.setsampwidth(2)       # 采样数据为两个字节
            f.setframerate(22050)   # 采样率
            f.setparams(attrib)     # 设置音频属性    
            f.writeframes(wav_data) # 写入数据
        #弹出结束窗口
        sleep(0.1)
        global main_win1
        main_win1 = Small_end()
        main_win1.End.show()
class Start():
    def __init__(self):#加载窗口1
        # 生成
        super().__init__()
        win1 = QFile('ui/start.ui')
        win1.open(QFile.ReadOnly)
        win1.close()
        self.start = QUiLoader().load(win1)
        # 按键侦测
        self.start.HIDE.clicked.connect(self.HIDE_main)# 隐藏模式
        self.start.extract.clicked.connect(self.EXTRACT_main)# 提取模式
        self.start.about.clicked.connect(self.goto_about)#关于
    def goto_about(self):
        global main_win6
        main_win6 = About()
        # 显示新窗口
        main_win6.about.show()
        # 关闭自己
        self.start.hide()
        #返回按键
        main_win6.about.goto_2.clicked.connect(main_win6.close_about)
    def HIDE_main(self):
        global main_win0
        main_win0 = Conceal()
        # 显示新窗口
        main_win0.HIDE.show()
        # 关闭自己
        self.start.close()
        #将默认路径写进去
        global Same_Path
        #第一行
        All_Files_1 = os.listdir(Same_Path + '\被写入的音频\\')
        if All_Files_1 == []:#判断有没有文件，防止报错
            main_win0.HIDE.DaTa.setText(Same_Path + '\被写入的音频\\')
        else:
            main_win0.HIDE.DaTa.setText(Same_Path + '\被写入的音频\\' + All_Files_1[0])
        #第二行
        All_Files_2 = os.listdir(Same_Path + '\要隐藏的文件\\')
        if All_Files_2 == []:#判断有没有文件，防止报错
            main_win0.HIDE.HiDE_DaTa.setText(Same_Path + '\要隐藏的文件\\')
        else:
            main_win0.HIDE.HiDE_DaTa.setText(Same_Path + '\要隐藏的文件\\' + All_Files_2[0])
        #第三行
        main_win0.HIDE.in_THe_enD.setText(Same_Path + '\转化后的音频\\')
        #更改进度条（进度条一开始会显示24%）
        main_win0.HIDE.bar.setRange(0,1)
        #侦测用户按下开始按键 button
        main_win0.HIDE.start_begin.clicked.connect(main_win0.Main_Program_HIDE)
    def EXTRACT_main(self):
        global main_win3
        main_win3 = Extract()
        # 显示新窗口
        main_win3.extract.show()
        # 关闭自己
        self.start.close()
        #写默认路径
        global Same_Path
        #第一行
        All_Files_3 = os.listdir(Same_Path + '\要提取的音频\\')
        if All_Files_3 == []:#判断有没有文件，防止报错
            main_win3.extract.DaTa.setText(Same_Path + '\要提取的音频\\')
        else:
            main_win3.extract.DaTa.setText(Same_Path + '\要提取的音频\\' + All_Files_3[0])
        #第二行
        main_win3.extract.extraction_data.setText(Same_Path + '\提取出的文件\\')
        # 修改进度条（默认显示24%） 
        main_win3.extract.bar.setRange(0,1)
        #等待按下开始按键
        main_win3.extract.start_begin.clicked.connect(main_win3.Main_Program_EXTRACT)                  
if __name__ == '__main__':# 加载窗口
    app = QtWidgets.QApplication(sys.argv)
    window = Start()
    window.start.show()
    sys.exit(app.exec_())
