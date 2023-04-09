from rich import print

def opo(row):
    # aaa = f'''
    #     <tr>
    #         <td><input type="number" name="table_2_col-1_row-{row}" id="table_2_col-1_row-{row}"></td>
    #         <td><input type="number" name="table_2_col-2_row-{row}" id="table_2_col-2_row-{row}"></td>
    #     </tr>
    # '''
    aaa = f'''
        <tr>
            <td><input type="number" name="table_3_col-1_row-{row}" id="table_3_col-1_row-{row}"></td>
            <td><input type="number" name="table_3_col-2_row-{row}" id="table_3_col-2_row-{row}"></td>
            <td><input type="number" name="table_3_col-3_row-{row}" id="table_3_col-3_row-{row}"></td>
        </tr>
    '''
    return aaa
for i in range(1, 18):
    print(opo(i))