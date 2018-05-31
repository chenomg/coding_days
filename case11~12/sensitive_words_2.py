#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: socket_client_def.py
#          Desc: 使用socket, threading和函数实现多线程
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-05-28 23:49:35
#       History:
# =============================================================================
'''
import wx
import basewin
from socket import *
from time import ctime
import threading
from time import sleep


class MianWindow(basewin.baseMainWindows):

    # 不能直接覆盖原有__ini__方法，这样会导致窗体启动失败。咱们新建一个，然后再调用
    def init_main_window(self):
        self.BUFSIZE = 1024
        # 此flag标记是否仍保持连接
        self.isConnected = False
        # 初始状态发送按钮不可用
        self.submit_button.Enabled = False
        # 初始状态断开连接按钮不可用
        self.disconnect_button.Enabled = False

    def multi_threads(self):
        print("Multi threads start...")
        # 主线程以外需要运行的子线程
        self.threads = []
        # 此线程用于接收信息, 并显示在聊天记录框内
        receive_message_thread = threading.Thread(
            target=self.message_receive, daemon=True)
        self.threads.append(receive_message_thread)
        for i in range(len(self.threads)):
            self.threads[i].start()

    def room1_selected(self, event):
        # 此项功能暂未添加
        # 选择房间号，然后显示该房间的聊天内容
        # self.chatting_textCtrl.SetMaxLength('Room 1')
        pass

    def get_dest(self):
        # 获取目标地址信息
        self.HOST = '127.0.0.1'
        self.PORT = 21345

    def connect_server(self, event):
        # 还需增加一个守护线程，获取是否保持连接，若断开则连接按钮可用，输入框不可用
        # 尝试连接目的地
        self.get_dest()
        self.ADDR = (self.HOST, self.PORT)
        try:
            self.tcpCliSock = socket()
            self.tcpCliSock.connect(self.ADDR)
            self.connect_button.Enabled = False
            self.isConnected = True
            self.submit_button.Enabled = True
            # 连接成功后执行消息接收和检查连接情况多线程
            self.multi_threads()
            self.disconnect_button.Enabled = True
        except:
            # 若连接失败
            print('Connection to {} Failed...'.format(self.ADDR))
            pass

    def disconnect_server(self, event):
        # 断开与服务器的连接
        self.connect_button.Enabled = True
        self.isConnected = False
        self.submit_button.Enabled = False
        self.tcpCliSock.close()
        self.disconnect_button.Enabled = False

    def verify_connection(self):
        # 此功能暂未添加
        # 单独线程运行，用以检查与服务器的连接状态，并相应动作
        while self.isConnected:
            pass

    def message_send(self, event):
        if self.isConnected:
            # 获取文本输入框内的内容
            text = self.send_text_textCtrl.GetValue()
            print("text: {}".format(text))
            if text:
                data = bytes(text, 'utf-8')
                # 发送数据
                self.tcpCliSock.send(data)
                print('Message send.')
                # 在聊天消息框内显示消息
                self.chatting_textCtrl.AppendText("Me({}):\n{}\n".format(
                    ctime(), text))
            else:
                pass

    def message_receive(self):
        # 此线程用以接收服务器返回的数据
        while True:
            if self.isConnected:
                try:
                    # 接收消息
                    data = self.tcpCliSock.recv(self.BUFSIZE)
                    data_str = data.decode('utf-8')
                    print('[{}] Server: {}'.format(ctime(), data_str))
                    # wx.textctrl控件在操作时若服务器返回后与发送后的同时操作会报错
                    # 用CallAfter解决此问题
                    wx.CallAfter(self.chatting_textCtrl.AppendText,
                                 "Server({}):\n{}\n".format(ctime(), data_str))
                except IOError:
                    pass
            else:
                break


def main():
    app = wx.App()
    # None表示的是此窗口没有上级父窗体。如果有，就直接在父窗体代码调用的时候填入‘self’就好了。
    main_win = MianWindow(None)
    main_win.init_main_window()
    main_win.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
