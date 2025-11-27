from dateutil.relativedelta import relativedelta
from pandas import to_datetime

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_via_consulting_info(info_requested:str)-> str:
    via_consulting = to_datetime('2022-04-01').date()
    via_consulting_end_date = to_datetime('2022-09-30').date()
    via_consulting_diff = relativedelta(via_consulting_end_date, via_consulting)

    via_consulting_years = via_consulting_diff.years
    via_consulting_months = via_consulting_diff.months

    if via_consulting_years == 0:
        if via_consulting_months < 10:
            via_consulting_job = f'0{via_consulting_months} month(s)'
        else:
            via_consulting_job = f'{via_consulting_months} month(s)'
    else:
        if via_consulting_months < 10:
            via_consulting_job = f'0{via_consulting_years} years and 0{via_consulting_months} month(s)'
        else:
            via_consulting_job = f'0{via_consulting_years} years and {via_consulting_months} month(s)'
    
    title = f'Data Engineer Consultant | Via Consulting | {via_consulting_job}'
    info = f'''
    {div_ini}

    #### Apr 2022 to Sep 2022
    {div_end}
    '''

    return eval(info_requested)

def get_via_consulting_gol_project(info_requested:str)-> str:

    gol = to_datetime('2022-08-01').date()
    gol_end_date = to_datetime('2022-09-01').date()
    gol_diff = relativedelta(gol_end_date, gol)

    gol_years = gol_diff.years
    gol_months = gol_diff.months

    if gol_years == 0:
        if gol_months < 10:
            gol_job = f'0{gol_months} month(s)'
        else:
            gol_job = f'{gol_months} month(s)'
    else:
        if gol_months < 10:
            gol_job = f'0{gol_years} years and 0{gol_months} month(s)'
        else:
            gol_job = f'0{gol_years} years and {gol_months} month(s)'
    
    title = f'Project - Gol Spend & Get| {gol_job}'
    info = f'''
    {div_ini}

    #### Ago 2022 to Ago 2022
    #### Smiles S.A.
    #### Project - Gol Spend & Get

    AWS Python lambda function that validates files to be called by an API.
    
    Resources:
    
    - Cloud Formation;
    - Python with unit tests;
    - Github release info;
    - Jenkins to observe github uploaded code;
    - Sonar for code quality;
    - End of Devops stack with deploy.
    {div_end}
    '''

    return eval(info_requested)


def get_via_consulting_zendesk_project(info_requested:str)-> str:

    zendesk = to_datetime('2022-07-01').date()
    zendesk_end_date = to_datetime('2022-08-01').date()
    zendesk_diff = relativedelta(zendesk_end_date, zendesk)

    zendesk_years = zendesk_diff.years
    zendesk_months = zendesk_diff.months

    if zendesk_years == 0:
        if zendesk_months < 10:
            zendesk_job = f'0{zendesk_months} month(s)'
        else:
            zendesk_job = f'{zendesk_months} month(s)'
    else:
        if zendesk_months < 10:
            zendesk_job = f'0{zendesk_years} years and 0{zendesk_months} month(s)'
        else:
            zendesk_job = f'0{zendesk_years} years and {zendesk_months} month(s)'
    
    title = f'Project - Zendesk Replication | {zendesk_job}'
    info = f'''
    {div_ini}

    #### Jul 2022 to Jul 2022
    #### Project - Zendesk Replication

    Continuous pushing of data in a AWS environment using tools like:
    
    - Pyspark Spark Glue jobs;
    - Cloud Formation;
    - AWS Athena;
    - Apache Hudi metadata for data governance.
    {div_end}
    '''

    return eval(info_requested)

def get_via_consulting_unimed_project(info_requested:str)-> str:

    unimed = to_datetime('2022-06-01').date()
    unimed_end_date = to_datetime('2022-09-30').date()
    unimed_diff = relativedelta(unimed_end_date, unimed)

    unimed_years = unimed_diff.years
    unimed_months = unimed_diff.months

    if unimed_years == 0:
        if unimed_months < 10:
            unimed_job = f'0{unimed_months} month(s)'
        else:
            unimed_job = f'{unimed_months} month(s)'
    else:
        if unimed_months < 10:
            unimed_job = f'0{unimed_years} years and 0{unimed_months} month(s)'
        else:
            unimed_job = f'0{unimed_years} years and {unimed_months} month(s)'
    
    title = f'Project - Stuffed Wallet | {unimed_job}'
    info = f'''
    {div_ini}

    #### Apr 2022 to Jun 2022
    #### Unimed Insurance
    #### Project - Stuffed Wallet (Carteira Recheada)

    Colaborating with the team in a ETL process using tools like:
    
    - Informatica Powercenter;
    - PLSQL - Oracle.
    
    The idea of the project is a campaign that supports the score of the company's brokers.
    {div_end}
    '''

    return eval(info_requested)
