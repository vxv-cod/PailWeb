import eel
from mainpy.StatzondWeb import raschet

# from rich import print

@eel.expose
def printpy(*args):
    print(args)

@eel.expose
def value_py(respo):
    # print(f"respo = {respo}")
    
    dannie_key = [
        'Otmetka_verha',
        'Dlina',
        'Diam',
        'Tolchina',
        'Plotnost',
        '--Нагрузка--',
        'Sjim',
        'Vider',
        'Yr_otv',
        'Koef_smerz',
        '--Коэф.-т надежности:--'
        'dlymetalla',
        'dlybetona',
        '--Данные грунтов --',
        'promerz_grunta',
        'qsi_max',
        'qsi_min',
        'vopornomgrunte',
        'gruntpodsvaeu'
    ]
    
    ige_skv_key = [
        'table_2_col-1_row-1',
        'table_2_col-1_row-2',
        'table_2_col-1_row-3',
        'table_2_col-1_row-4',
        'table_2_col-1_row-5',
        'table_2_col-1_row-6',
        'table_2_col-1_row-7',
        'table_2_col-1_row-8',
        'table_2_col-1_row-9',
        'table_2_col-1_row-10',
        'table_2_col-1_row-11',
        'table_2_col-1_row-12',
        'table_2_col-1_row-13',
        'table_2_col-1_row-14',
        'table_2_col-1_row-15',
        'table_2_col-1_row-16',
        'table_2_col-1_row-17'
    ]
    
    nni_key = [
        'table_2_col-2_row-1',
        'table_2_col-2_row-2',
        'table_2_col-2_row-3',
        'table_2_col-2_row-4',
        'table_2_col-2_row-5',
        'table_2_col-2_row-6',
        'table_2_col-2_row-7',
        'table_2_col-2_row-8',
        'table_2_col-2_row-9',
        'table_2_col-2_row-10',
        'table_2_col-2_row-11',
        'table_2_col-2_row-12',
        'table_2_col-2_row-13',
        'table_2_col-2_row-14',
        'table_2_col-2_row-15',
        'table_2_col-2_row-16',
        'table_2_col-2_row-17'
        
    ]
    
    ige_xap_key = [
        'table_3_col-1_row-1',
        'table_3_col-1_row-2',
        'table_3_col-1_row-3',
        'table_3_col-1_row-4',
        'table_3_col-1_row-5',
        'table_3_col-1_row-6',
        'table_3_col-1_row-7',
        'table_3_col-1_row-8',
        'table_3_col-1_row-9',
        'table_3_col-1_row-10',
        'table_3_col-1_row-11',
        'table_3_col-1_row-12',
        'table_3_col-1_row-13',
        'table_3_col-1_row-14',
        'table_3_col-1_row-15',
        'table_3_col-1_row-16',
        'table_3_col-1_row-17'
    ]
    
    qi_xap_key = [
        'table_3_col-2_row-1',
        'table_3_col-2_row-2',
        'table_3_col-2_row-3',
        'table_3_col-2_row-4',
        'table_3_col-2_row-5',
        'table_3_col-2_row-6',
        'table_3_col-2_row-7',
        'table_3_col-2_row-8',
        'table_3_col-2_row-9',
        'table_3_col-2_row-10',
        'table_3_col-2_row-11',
        'table_3_col-2_row-12',
        'table_3_col-2_row-13',
        'table_3_col-2_row-14',
        'table_3_col-2_row-15',
        'table_3_col-2_row-16',
        'table_3_col-2_row-17'
    ]
    
    fi_xap_key = [
        'table_3_col-3_row-1',
        'table_3_col-3_row-2',
        'table_3_col-3_row-3',
        'table_3_col-3_row-4',
        'table_3_col-3_row-5',
        'table_3_col-3_row-6',
        'table_3_col-3_row-7',
        'table_3_col-3_row-8',
        'table_3_col-3_row-9',
        'table_3_col-3_row-10',
        'table_3_col-3_row-11',
        'table_3_col-3_row-12',
        'table_3_col-3_row-13',
        'table_3_col-3_row-14',
        'table_3_col-3_row-15',
        'table_3_col-3_row-16',
        'table_3_col-3_row-17'
    ]
    
    
    global dannie, ige_skv, nni, ige_xap, qi_xap, fi_xap
    
    def sbor(list_key):
        list_ = []
        # print(respo)
        
        for i in list_key:
            if i in respo:
                xxx = respo[i]
                try:
                    xxx = float(xxx)
                except:
                    pass
                list_.append(xxx)
            else:
                list_.append(0)
        return list_
    
    dannie = sbor(dannie_key)
    ige_skv = sbor(ige_skv_key)
    nni = sbor(nni_key)
    ige_xap = sbor(ige_xap_key)
    qi_xap = sbor(qi_xap_key)
    fi_xap = sbor(fi_xap_key)
    
    textweb = raschet(dannie, ige_skv, nni, ige_xap, qi_xap, fi_xap)
    
    return textweb
    
    

