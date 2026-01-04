from helper.py_helper import get_work_project_time

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_bi4all_info(idiom: str)-> str:

    ini_date = '2021-07-01'
    end_date = '2022-05-31'

    job_time, detail = get_work_project_time(idiom = idiom, ini_date = ini_date, end_date = end_date)

    if idiom == 'en':
            
        title = f'Data Engineer Consultant | BI4ALL | {job_time}'
        info = f'''
        {div_ini}

        #{detail}

        {div_end}
        '''

        return title, info
    
    elif idiom == 'br':
        
        title = f'Engenheiro de Dados Consultor | BI4ALL | {job_time}'
        info = f'''
            {div_ini}

            #{detail}

            {div_end}
            '''

        return title, info

def get_bi4all_project_01(idiom: str)-> str:

    ini_date = '2021-07-01'
    end_date = '2022-05-31'

    job_time, detail = get_work_project_time(idiom = idiom, ini_date = ini_date, end_date = end_date)

    if idiom == 'en':
                
        title = f'Project - BI in AWS | {job_time}'
        info = f'''
        {div_ini}

        #{detail}
        #### Manserv Company

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

        return title, info
    
    elif idiom == 'br':
        
        title = f'Projeto - BI na AWS | {job_time}'
        info = f'''
        {div_ini}

        #{detail}
        #### EmpresaManserv

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

        return title, info
