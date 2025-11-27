from pandas import to_datetime
from dateutil.relativedelta import relativedelta

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_bi4all_info(info_requested:str)-> str:
    bi4all = to_datetime('2021-07-01').date()
    bi4all_end_date = to_datetime('2022-05-31').date()
    bi4all_diff = relativedelta(bi4all_end_date, bi4all)

    bi4all_years = bi4all_diff.years
    bi4all_months = bi4all_diff.months

    if bi4all_years == 0:
        if bi4all_months < 10:
            bi4all_job = f'0{bi4all_months} month(s)'
        else:
            bi4all_job = f'{bi4all_months} month(s)'
    else:
        if bi4all_months < 10:
            bi4all_job = f'0{bi4all_years} years and 0{bi4all_months} month(s)'
        else:
            bi4all_job = f'0{bi4all_years} years and {bi4all_months} month(s)'
    
    title = f'Data Engineer Consultant | BI4ALL | {bi4all_job}'
    info = f'''
    {div_ini}

    #### Jul 2021 to May 2022
    {div_end}
    '''

    return eval(info_requested)

def get_bi4all_bi_project(info_requested:str)-> str:

    bi = to_datetime('2021-07-01').date()
    bi_end_date = to_datetime('2022-05-31').date()
    bi_diff = relativedelta(bi_end_date, bi)

    bi_years = bi_diff.years
    bi_months = bi_diff.months

    if bi_years == 0:
        if bi_months < 10:
            bi_job = f'0{bi_months} month(s)'
        else:
            bi_job = f'{bi_months} month(s)'
    else:
        if bi_months < 10:
            bi_job = f'0{bi_years} years and 0{bi_months} month(s)'
        else:
            bi_job = f'0{bi_years} years and {bi_months} month(s)'
    
    title = f'Project - BI in AWS | {bi_job}'
    info = f'''
    {div_ini}
    
    #### Jul 2021 to May 2022
    #### Manserv
    #### Project - BI in AWS

    Responsible for creating data pipelines to push data in S3 using python AWS lambda funtions.
    Using packages such as awswrangler, xmltodict, json and much more.
    Being involved in great projects with the relevant skills, accessing different APIs from several providers.

    Some of these ones are:

    - Volvo
    - Nuntec
    - Komatsu
    - Komtrax
    - Caterpillar and many others.

    Also Transforming XML and JSON API extrations into tabular data to be recorded in parquet table format, grating a better use of S3 bucket as much as gaing performance in a compressed file format.
    
    {div_end}
    '''

    return eval(info_requested)
