#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import json
import os
import pandas as pd

import ui_operator

SAVE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),'json-files')
os.makedirs(SAVE_DIR,exist_ok=True)

excel = ui_operator.select_xlsx()
input_file = pd.ExcelFile(excel)

for sheet_name in input_file.sheet_names:
    df = pd.read_excel(excel, sheet_name=sheet_name,index_col=0)
    dic = df.to_dict()
    with codecs.open(os.path.join(SAVE_DIR, f'{sheet_name}.json'),'w',encoding='utf-8') as f:
        dump = json.dumps(dic,indent=2,ensure_ascii=False)
        f.write(dump)
