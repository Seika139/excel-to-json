#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tkinter, tkinter.filedialog, tkinter.messagebox

# return one xlsx file
def select_xlsx():
    root = tkinter.Tk()
    root.withdraw()
    filetype = [("", "*.xlsx")]
    tkinter.messagebox.showinfo('ファイル選択', '取得するxlsxファイルを選択してください')
    xlsx_path = tkinter.filedialog.askopenfilename(filetypes=filetype)
    print(f'selected filename : {xlsx_path}')
    return xlsx_path

# return [several xlsx files]
def select_multi_xlsx():
    xlsx_paths = []
    root = tkinter.Tk()
    root.withdraw()
    filetype = [("", "*.xlsx")]
    tkinter.messagebox.showinfo('ファイル選択(複数)', 'xlsxファイルを選択してください(複数選択可)')
    ans = True
    file_num = 0
    while ans:
        selected_paths = tkinter.filedialog.askopenfilenames(filetypes=filetype)
        print('<< selected filename >>')
        for path in selected_paths:
            i += 1
            xlsx_paths.append(path)
            print(f'{i} : {path}')
        print()
        ans = tkinter.messagebox.askyesno('ファイル選択(複数)','さらにファイルを選びますか？')
    return xlsx_paths
