#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: sensitive_words_2.py
#          Desc: 敏感词文本文件 filtered_words.txt，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
#        Author: Jase Chen
#         Email: xxmm@live.cn
#      HomePage: https://jase.im/
#       Version: 0.0.1
#       License: GPLv2
#    LastChange: 2018-05-31 22:58:17
#       History:
# =============================================================================
'''
import wx
import basewin
from time import ctime
import sensitive_words_1
import re


class baseMianWindow(basewin.baseMainWindow):

    # 不能直接覆盖原有__ini__方法，这样会导致窗体启动失败。咱们新建一个，然后再调用
    def init_main_window(self):
        self.sensi_words_list = sensitive_words_1.get_sensi_words()
        self.output_textCtrl.AppendText('消息将会过滤。。。')
        self.output_textCtrl.AppendText('\n')

    def submit(self, event):
        get_input = self.input_textCtrl.GetValue() + '\n'
        Found = False
        for word in self.sensi_words_list:
            if re.findall(r'(?:%s)'%(word), get_input):
                Found = True
                get_input = get_input.replace(word, '**')
                print('Replace successful!')
        self.output_textCtrl.AppendText(get_input)
        print('Submit successful!')

def main():
    app = wx.App()
    # None表示的是此窗口没有上级父窗体。如果有，就直接在父窗体代码调用的时候填入‘self’就好了。
    main_win = baseMianWindow(None)
    main_win.init_main_window()
    main_win.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
