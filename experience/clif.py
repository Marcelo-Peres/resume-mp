from pandas import to_datetime
from dateutil.relativedelta import relativedelta

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_clif_info(info_requested:str)-> str:
    clif = to_datetime('2019-04-01').date()
    clif_end_date = to_datetime('2021-06-30').date()
    clif_diff = relativedelta(clif_end_date, clif)

    clif_years = clif_diff.years
    clif_months = clif_diff.months

    if clif_years == 0:
        if clif_months < 10:
            clif_job = f'0{clif_months} month(s)'
        else:
            clif_job = f'{clif_months} month(s)'
    else:
        if clif_months < 10:
            clif_job = f'0{clif_years} years and 0{clif_months} month(s)'
        else:
            clif_job = f'0{clif_years} years and {clif_months} month(s)'
    
    title = f'IT Analyst | CLIF | {clif_job}'
    info = f'''
    {div_ini}

    #### Apr 2019 to Jun 2021
    {div_end}
    '''

    return eval(info_requested)

def get_clif_project(info_requested: str)-> str:
    
    title = f'Systems and BI Management | CLIF | 02 years and 03 months'
    
    info = f'''
    {div_ini}

    #### Apr 2019 to Jun 2021
    #### CLIF - Centro Logístico Integrado FastCargo S.A
    #### Systems Management

    - Responsible for managing the SARA system, Logix, My Checklist & Customer Service Portal;
    - Application of SARA customs system update packages;
    - Updating of stored procedures in SQL;
    - SQL Trigger Updates;
    - Module Reviews among others;
    - Creating a Python script to insert and update ships and related data on the Customer Service Portal;

    #### BI Management

    Creation of reports in Power BI as:

    - Registration management and control;
    - Unit management and control;
    - Transport management and control;
    - Ship management and control;

    The above reports are synchronized and loaded into Power BI containing data from 02 different databases and a loading of data from a Python Script connected to an API available by Porto Itapoá containing the dates of ship movements, thus making it possible to cross all information among those different data to better management of customer assets.
    
    {div_end}
    '''
    return eval(info_requested)
