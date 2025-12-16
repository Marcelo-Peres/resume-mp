from dateutil.relativedelta import relativedelta
from pandas import to_datetime

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_a3data_info(info_requested:str, idiom: str)-> str:

    ini_date = to_datetime('2022-12-01').date()
    end_date = to_datetime('2023-03-31').date()
    diff_date = relativedelta(end_date, ini_date)

    years = diff_date.years
    months = diff_date.months

    if idiom == 'en':
        if years == 0:
            if months < 10:
                a3data_job = f'0{months} month(s)'
            else:
                a3data_job = f'{months} month(s)'
        else:
            if months < 10:
                a3data_job = f'0{years} years and 0{months} month(s)'
            else:
                a3data_job = f'0{years} years and {months} month(s)'
            
        title = f'Big Data Engineer | A3 Data | {a3data_job}'
        info = f'''
        {div_ini}

        #### Dec 2022 to Mar 2023

        {div_end}
        '''
    
    elif idiom == 'br':
        if years == 0:
            if months == 1:
                a3data_p01 = f'0{months} mês'
            elif months < 10:
                a3data_p01 = f'0{months} meses'
            else:
                a3data_p01 = f'{months} meses'
        else:
            if months == 1:
                a3data_p01 = f'0{years} ano(s) e 0{months} mês'
            if months < 10:
                a3data_p01 = f'0{years} ano(s) e 0{months} meses'
            else:
                a3data_p01 = f'0{years} ano(s) e {months} meses'

        title = f'Engenheiro de Big Data | A3 Data | {a3data_p01}'
        info = f'''
            {div_ini}

            #### De Dezembro de 2022 até Março de 2023

            {div_end}
            '''

    return eval(info_requested)

def get_a3data_project_01(info_requested: str, idiom: str)-> str:

    ini_date = to_datetime('2022-12-01').date()
    end_date = to_datetime('2023-03-31').date()
    diff_date = relativedelta(end_date, ini_date)

    years = diff_date.years
    months = diff_date.months
    
    if idiom == 'en':
        if years == 0:
            if months < 10:
                a3data_p01 = f'0{months} month(s)'
            else:
                a3data_p01 = f'{months} month(s)'
        else:
            if months < 10:
                a3data_p01 = f'0{years} years and 0{months} month(s)'
            else:
                a3data_p01 = f'0{years} years and {months} month(s)'
        
        title = f'Datalake project - Stellantis Company | {a3data_p01}'
        info = f'''
        {div_ini}

        #### From Dec 2022 to Mar 2023
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
    
    elif idiom == 'br':
        if years == 0:
            if months == 1:
                a3data_p01 = f'0{months} mês'
            elif months < 10:
                a3data_p01 = f'0{months} meses'
            else:
                a3data_p01 = f'{months} meses'
        else:
            if months == 1:
                a3data_p01 = f'0{years} ano(s) e 0{months} mês'
            if months < 10:
                a3data_p01 = f'0{years} ano(s) e 0{months} meses'
            else:
                a3data_p01 = f'0{years} ano(s) e {months} meses'

        title = f'Projeto Datalake - Empresa Stellantis | {a3data_p01}'
        info = f'''
        {div_ini}

        #### De Dezembro de 2022 até Março de 2023
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

    return eval(info_requested)
