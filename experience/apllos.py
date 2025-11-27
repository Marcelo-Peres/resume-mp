from dateutil.relativedelta import relativedelta
from pandas import to_datetime

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_apllos_info(info_requested:str)-> str:

    apllos = to_datetime('2023-07-01').date()
    current_date = to_datetime('now').date()
    diff = relativedelta(current_date, apllos)

    years = diff.years
    months = diff.months

    if years == 0:
        if months < 10:
            current_job = f'0{months} month(s)'
        else:
            current_job = f'{months} month(s)'
    else:
        if months < 10:
            current_job = f'0{years} years and 0{months} month(s)'
        else:
            current_job = f'0{years} years and {months} month(s)'

    title = f'Senior Big Data Engineer | Apllos Solutions | {current_job}'
    info = f'''
    #### From Jul 2023 to nowadays
    '''
    return eval(info_requested)

def get_apllos_current_project(info_requested: str)-> str:
    audlab = to_datetime('2025-01-01').date()
    audlab_current_date = to_datetime('now').date()
    audlab_diff = relativedelta(audlab_current_date, audlab)

    audlab_years = audlab_diff.years
    audlab_months = audlab_diff.months

    if audlab_years == 0:
        if audlab_months < 10:
            audlab_job = f'0{audlab_months} month(s)'
        else:
            audlab_job = f'{audlab_months} month(s)'
    else:
        if audlab_months < 10:
            audlab_job = f'0{audlab_years} years and 0{audlab_months} month(s)'
        else:
            audlab_job = f'0{audlab_years} years and {audlab_months} month(s)'
    
    title = f'Project Audlab | {audlab_job}'
    info = f'''
    {div_ini}

    #### << Project Audlab >>
    #### From Jan 2025 to nowadays
            
    Now developing into data lake Delta Lake tables and Postgre tables for Gerdau Commercial Assets.
    Some tables in Postgres for apps interaction and decision making through PBI Reports.

    {div_end}
    '''

    return eval(info_requested)


def get_apllos_gab_project(info_requested: str)-> str:
    gab = to_datetime('2024-09-01').date()
    gab_end_date = to_datetime('2024-12-31').date()
    gab_diff = relativedelta(gab_end_date, gab)

    gab_years = gab_diff.years
    gab_months = gab_diff.months

    if gab_years == 0:
        if gab_months < 10:
            gab_job = f'0{gab_months} month(s)'
        else:
            gab_job = f'{gab_months} month(s)'
    else:
        if gab_months < 10:
            gab_job = f'0{gab_years} years and 0{gab_months} month(s)'
        else:
            gab_job = f'0{gab_years} years and {gab_months} month(s)'
    
    title = f'Project GAB - Industrial Maintenance | {gab_job}'
    info = f'''
    {div_ini}

    #### << Project GAB - Industrial Maintenance >>
    #### From Sep 2024 to Dec 2024

    In charge of migrate and rebuild ETL process in Pyspark.
    The original scope was only migrate the scripts and put in a CICD environment, and configure jobs schedule in Control-M plataform.

    However, due to a delay faced through PBI workflows, the project suffered a change bringing a big part of process to databricks.
    New tables were created, steps were adpted and the project ajusted.

    Final charge time has been reduced and the PBI charges becmes faster. 
    
    
    For three large tables the gains were awesome as below mentioned: 


    - **The first table took 01h20 before, reduced to 10 minutes to charge PBI file.** 
    - **The second one took 03h13 before, reduced to 10 minutes to charge PBI file.** 
    - **The third one took 01h30 before, reduced to 10 minutes to charge PBI file.** 

    {div_end}
    '''

    return eval(info_requested)

def get_apllos_audlab_project(info_requested: str)-> str:
        
    audlab = to_datetime('2023-07-01').date()
    audlab_end_date = to_datetime('2024-09-30').date()
    audlab_diff = relativedelta(audlab_end_date, audlab)

    audlab_years = audlab_diff.years
    audlab_months = audlab_diff.months

    if audlab_years == 0:
        if audlab_months < 10:
            audlab_job = f'0{audlab_months} month(s)'
        else:
            audlab_job = f'{audlab_months} month(s)'
    else:
        if audlab_months < 10:
            audlab_job = f'0{audlab_years} years and 0{audlab_months} month(s)'
        else:
            audlab_job = f'0{audlab_years} years and {audlab_months} month(s)'
    
    title = f'Project Databricks Migration Audlab | {audlab_job}'
    info = f'''
    {div_ini}

    #### << Audlab >>
    #### From Jul 2023 to Sep 2024

    In charge of data ingestions.

    Audlab is an Audit department in Gerdau Company.
    Gerdau is an important enterprise in Brazil that works with iron and steel, producing several tools for different segments in the world.

    In this department I provide a full control of gitlab and deploying scripts.

    Control - M is responsible to execute EMR clusters and scripts in python and pyspark through different assets.
    Producing ETL and Data Science Scripts for machine learning and data transformation.

    I was one of core people helping data migration steps from AWS tools to Databricks.
    EMR clusters now replicated accordingly in Databricks.

    The migration was well successed!
    Finnaly working in Databricks!
    {div_end}
    '''

    return eval(info_requested)
