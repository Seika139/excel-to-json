#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import json
import os
import pandas as pd
import re

import ui_operator

def main(path_xlsx):
    root_dir = os.path.abspath(os.path.dirname(__file__))
    child_dir = re.split(f'{os.sep}|\.',path_xlsx)[-2]
    save_dir = os.path.join(root_dir,'json-files',child_dir)
    os.makedirs(save_dir,exist_ok=True)

    for sheet_name in pd.ExcelFile(path_xlsx).sheet_names:
        df = pd.read_excel(path_xlsx, sheet_name=sheet_name,index_col=0)
        dic = df.to_dict()
        with codecs.open(os.path.join(save_dir, f'{sheet_name}.json'),'w',encoding='utf-8') as f:
            dump = json.dumps(dic,indent=2,ensure_ascii=False)
            f.write(dump)

if __name__ == '__main__':
    main(ui_operator.select_xlsx())
