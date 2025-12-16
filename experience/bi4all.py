from pandas import to_datetime
from dateutil.relativedelta import relativedelta

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_bi4all_info(info_requested:str, idiom: str)-> str:

    ini_date = to_datetime('2021-07-01').date()
    end_date = to_datetime('2022-05-31').date()
    diff_date = relativedelta(end_date, ini_date)

    years = diff_date.years
    months = diff_date.months

    if idiom == 'en':
        if years == 0:
            if months < 10:
                bi4all_job = f'0{months} month(s)'
            else:
                bi4all_job = f'{months} month(s)'
        else:
            if months < 10:
                bi4all_job = f'0{years} years and 0{months} month(s)'
            else:
                bi4all_job = f'0{years} years and {months} month(s)'
            
        title = f'Data Engineer Consultant | BI4ALL | {bi4all_job}'
        info = f'''
        {div_ini}

        #### Jul 2021 to May 2022

        {div_end}
        '''
    
    elif idiom == 'br':
        if years == 0:
            if months == 1:
                bi4all_job = f'0{months} mês'
            elif months < 10:
                bi4all_job = f'0{months} meses'
            else:
                bi4all_job = f'{months} meses'
        else:
            if months == 1:
                bi4all_job = f'0{years} ano(s) e 0{months} mês'
            if months < 10:
                bi4all_job = f'0{years} ano(s) e 0{months} meses'
            else:
                bi4all_job = f'0{years} ano(s) e {months} meses'

        title = f'Engenheiro de Dados Consultor | BI4ALL | {bi4all_job}'
        info = f'''
            {div_ini}

            #### De Julho de 2021 até Maio de 2022

            {div_end}
            '''

    return eval(info_requested)

def get_bi4all_project_01(info_requested: str, idiom: str)-> str:

    ini_date = to_datetime('2021-07-01').date()
    end_date = to_datetime('2022-05-31').date()
    diff_date = relativedelta(end_date, ini_date)

    years = diff_date.years
    months = diff_date.months
    
    if idiom == 'en':
        if years == 0:
            if months < 10:
                p01 = f'0{months} month(s)'
            else:
                p01 = f'{months} month(s)'
        else:
            if months < 10:
                p01 = f'0{years} years and 0{months} month(s)'
            else:
                p01 = f'0{years} years and {months} month(s)'
        
        title = f'Project - BI in AWS | {p01}'
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
    
    elif idiom == 'br':
        if years == 0:
            if months == 1:
                p01 = f'0{months} mês'
            elif months < 10:
                p01 = f'0{months} meses'
            else:
                p01 = f'{months} meses'
        else:
            if months == 1:
                p01 = f'0{years} ano(s) e 0{months} mês'
            if months < 10:
                p01 = f'0{years} ano(s) e 0{months} meses'
            else:
                p01 = f'0{years} ano(s) e {months} meses'

        title = f'Projeto - BI na AWS | {p01}'
        info = f'''
        {div_ini}

        #### De Julho de 2021 até Maio de 2022
        #### Manserv
        #### Projeto - BI na AWS

        Responsável pela criação de pipelines de dados para enviar dados para o S3 usando funções AWS Lambda em Python.
        Utilizando pacotes como awswrangler, xmltodict, json e muitos outros.
        Participando de ótimos projetos, demonstrando as habilidades relevantes, acessando diferentes APIs de vários provedores.

        Alguns deles são:

        - Volvo
        - Nuntec
        - Komatsu
        - Komtrax
        - Caterpillar and many others.

        Além disso, atuando em extrações de APIs de retorno XML e JSON, transformando em dados tabulares para serem registrados no formato de tabela Parquet, permitindo um melhor aproveitamento do bucket S3 e ganhando desempenho em um formato de arquivo compactado.
        
        {div_end}
        '''

    return eval(info_requested)
