from dateutil.relativedelta import relativedelta
from pandas import to_datetime

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_a3data_info(info_requested:str)-> str:

    a3data = to_datetime('2022-12-01').date()
    a3data_end_date = to_datetime('2023-03-31').date()
    a3data_diff = relativedelta(a3data_end_date, a3data)

    a3data_years = a3data_diff.years
    a3data_months = a3data_diff.months

    if a3data_years == 0:
        if a3data_months < 10:
            a3data_job = f'0{a3data_months} month(s)'
        else:
            a3data_job = f'{a3data_months} month(s)'
    else:
        if a3data_months < 10:
            a3data_job = f'0{a3data_years} years and 0{a3data_months} month(s)'
        else:
            a3data_job = f'0{a3data_years} years and {a3data_months} month(s)'
        
    title = f'Big Data Engineer | A3 Data | {a3data_job}'
    info = f'''
    {div_ini}

    #### Dec 2022 to Mar 2023

    {div_end}
    '''

    return eval(info_requested)

def get_a3data_stellantis_project(info_requested:str)-> str:

    stellantis = to_datetime('2022-12-01').date()
    stellantis_end_date = to_datetime('2023-03-31').date()
    stellantis_diff = relativedelta(stellantis_end_date, stellantis)

    stellantis_years = stellantis_diff.years
    stellantis_months = stellantis_diff.months
    
    if stellantis_years == 0:
        if stellantis_months < 10:
            stellantis_job = f'0{stellantis_months} month(s)'
        else:
            stellantis_job = f'{stellantis_months} month(s)'
    else:
        if stellantis_months < 10:
            stellantis_job = f'0{stellantis_years} years and 0{stellantis_months} month(s)'
        else:
            stellantis_job = f'0{stellantis_years} years and {stellantis_months} month(s)'
    
    title = f'Stellantis - Datalake project | {stellantis_job}'
    info = f'''
    {div_ini}

    #### Dec 2022 to Mar 2023
    #### << GCP - Google Cloud Platform >>

    Responsible for creating tools to interect data at plataform.

    - Tools used:
    - Terraform;
    - Google Storage;
    - BigQuery;
    - Google Functions;
    - Airflow;
    - Python;
    - SQL.
    {div_end}
    '''

    return eval(info_requested)
