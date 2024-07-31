import json
import os

import pandas as pd

csv_file_path = f'{os.getcwd()}/trainSet_ans.csv'  # 输入 CSV 文件路径
jsonl_file_path = f'{os.getcwd()}/trainSet_ans_output.jsonl'  # 输出的 JSONL 文件路径
excel_file_path = f'{os.getcwd()}/test.xlsx'  # 输入的 excel 文件路径
excel_output_file_path = f'{os.getcwd()}/train_output.xlsx'  # 输出的 excel 文件路径
txt_path = f'{os.getcwd()}/result.jsonl'  # 输出的 excel 文件路径

# 生成模板
ai_chat = (r'{"input"："<_user>判断该msisdn是否是涉案诈骗电话，是请输出1，不是请输出0。'
           r'<_user>index1<_user>index2<_user>index3","output":"is_sa:issa"}')

def csv_to_jsonl():
    # 读取CSV文件
    df = pd.read_csv(csv_file_path)
    # 将DataFrame逐行写入JSONL文件
    with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
        for record in df.to_dict(orient='records'):
            jsonl_file.write(f"{record}\n")

def excel_to_jsonl():
    # 要读取的行
    col = {'msisdn','start_time','end_time','call_event','other_party',
           'home_area_code','visit_area_code','called_home_code','called_code','a_serv_type',
           'long_type1','roam_type','a_product_id','open_datetime','call_duration',
           'hour','phone1_type','phone2_type'}
    df = pd.read_excel(excel_file_path, usecols=col)
    # 将DataFrame逐行写入JSONL文件
    with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
        for record in df.to_dict(orient='records'):
            jsonl_file.write(f"{json.dumps(record)}\n")

def csv_change():
    # 读取CSV文件
    df = pd.read_csv(csv_file_path)    # 转为list并拿到msisdn
    list = df.to_dict(orient='list').get('msisdn')
    # 读取excel文件
    pd_excel = pd.read_excel(excel_file_path)
    # 筛选excel 只留下msisdn在list中出现的数据
    filtered_df = pd_excel[pd_excel['msisdn'].isin(list)]
    # 存储为excel
    filtered_df.to_excel(excel_output_file_path)

def data_change_limit3():
    col = {'msisdn','start_time','end_time','call_event','other_party',
           'home_area_code','visit_area_code','called_home_code','called_code','a_serv_type',
           'long_type1','roam_type','a_product_id','open_datetime','call_duration',
           'hour','phone1_type','phone2_type'}
    json_data = []

    # 读取excel
    df = pd.read_excel(excel_file_path,usecols=col)
    sampled_data = df.groupby('msisdn').apply(lambda x: x.sample(min(len(x), 3)))
    sampled_data.reset_index(drop=True, inplace=True)

    # 移除多余索引
    grouped = sampled_data.groupby('msisdn')

    # 读取csv文件
    df_ans = pd.read_csv(csv_file_path)

    # 循环分组后的通话记录
    for source in grouped:
        temp_text = ai_chat
        id = 0
        count = 1
        list = source[1].to_dict(orient='records')
        for item in list:
            temp_text = temp_text.replace(f'index{count}',str(json.dumps(item).replace('{','').replace('}','')))
            id = item.get('msisdn')
            count += 1

        # 获取output的is_sa值
        is_sa_value = df_ans.loc[df_ans['msisdn'] == id, 'is_sa'].values[0]
        temp_text = temp_text.replace('issa',str(is_sa_value))
        # 将当前字典添加到json_data列表中
        json_data.append(temp_text)

    with open(txt_path, "w") as file:
        for item in json_data:
            file.write(str(item) + "\n")



if __name__ == '__main__':
    csv_to_jsonl()
    # excel_to_jsonl()