from helper.py_helper import get_work_project_time

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_a3data_info(idiom: str)-> str:

    ini_date = '2022-12-01'
    end_date = '2023-03-31'

    job_time, detail = get_work_project_time(idiom = idiom, ini_date = ini_date, end_date = end_date)

    if idiom == 'en':
            
        title = f'Big Data Engineer | A3 Data | {job_time}'
        info = f'''
        {div_ini}

        #{detail}

        {div_end}
        '''

        return title, info
    
    elif idiom == 'br':

        title = f'Engenheiro de Big Data | A3 Data | {job_time}'
        info = f'''
        {div_ini}

        #{detail}

        {div_end}
        '''

        return title, info

def get_a3data_project_01(idiom: str)-> str:

    ini_date = '2022-12-01'
    end_date = '2023-03-31'
    
    job_time, detail = get_work_project_time(idiom = idiom, ini_date = ini_date, end_date = end_date)

    if idiom == 'en':

        title = f'Datalake project - Stellantis Company | {job_time}'
        info = f'''
        {div_ini}

        #{detail}
        #### << GCP - Google Cloud Platform >>

        Responsible for creating tools to interect data at plataform.

        Tools used:
        - Terraform;
        - Google Storage;
        - BigQuery;
        - Google Functions;
        - Airflow;
        - Python;
        - SQL.

        {div_end}
        '''

        return title, info
    
    elif idiom == 'br':
        
        title = f'Projeto Datalake - Empresa Stellantis | {job_time}'
        info = f'''
        {div_ini}

        #{detail}
        #### << GCP - Platform Google em nuvem >>

        Responsável por criar ferramentas para interagir com dados na plataforma.

        Ferramentas utilizadas:
        - Terraform;
        - Google Storage;
        - BigQuery;
        - Google Functions;
        - Airflow;
        - Python;
        - SQL.
        
        {div_end}
        '''

        return title, info
