import os

import pandas as pd
import requests


def download_file_from_url(url, name):
    r = requests.get(url, allow_redirects=True)
    open(f'{name}.xlsx', 'wb').write(r.content)


def get_path_to_dataframe(file_name):
    loc_file = os.path.dirname(os.path.abspath(file_name))
    pd.ExcelFile(loc_file + f'/{file_name}.xlsx')
    return pd.ExcelFile(loc_file + f'/{file_name}.xlsx')


def get_sheet_by_index(table, sheet_index):
    sheet_names = table.sheet_names
    return table.parse(sheet_name=sheet_names[sheet_index])


def get_array_by_rows(table, from_row, to_row):
    arr = []
    for row in range(from_row, to_row):
        arr.append(table[row])
    return arr


def get_result_array(table_list_1, table_list_2):
    result = []
    for l1, l2 in zip(table_list_1, table_list_2):
        result.append(max(l1, l2))
    return result


class main:
    # url: https://drive.google.com/uc?export=download&id=11fqThaYsMl5Naldw7Qd3ruCEs5m92sng

    input_url = input("Enter the wanted URL: ")
    input_file = input("Enter the wanted name of file: ")
    input_indexes = (
        int(input("Enter the first table index (i.e: 4): ")) - 1,
        int(input("Enter the second table index (i.e: 5): ")) - 1,
        int(input("Enter the column index (i.e: for column F insert 5): ")),
        int(input("From row (i.e: 15): ")) - 2,
        int(input("To row (i.e: 30): ")) - 1
    )

    download_file_from_url(input_url, input_file)
    df = get_path_to_dataframe(input_file)

    table_2 = get_sheet_by_index(df, input_indexes[0])
    table_3 = get_sheet_by_index(df, input_indexes[1])

    arr_table_2 = get_array_by_rows(table_2.loc[:, table_2.columns[input_indexes[2]]],
                                    input_indexes[3],
                                    input_indexes[4])
    arr_table_3 = get_array_by_rows(table_3.loc[:, table_3.columns[input_indexes[2]]],
                                    input_indexes[3],
                                    input_indexes[4])

    arr_result = get_result_array(arr_table_2, arr_table_3)

    print(f'\narray 1: {arr_table_2}')
    print(f'array 2: {arr_table_3}')
    print(f'array r: {arr_result}')
