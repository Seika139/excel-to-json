#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import json
import os
import pandas as pd
import re

import ui_operator

def main(excel_path):
    root = os.path.abspath(os.path.dirname(__file__))
    filename = re.split(f'{os.sep}|\.',excel_path)[-2]
    save_dir = os.path.join(root,'json-files',filename)
    os.makedirs(save_dir,exist_ok=True)

    for sheet_name in pd.ExcelFile(excel_path).sheet_names:
        df = pd.read_excel(excel_path, sheet_name=sheet_name,index_col=0)
        dic = df.to_dict()
        with codecs.open(os.path.join(save_dir, f'{sheet_name}.json'),'w',encoding='utf-8') as f:
            dump = json.dumps(dic,indent=2,ensure_ascii=False)
            f.write(dump)

if __name__ == '__main__':
    main(ui_operator.select_xlsx())
