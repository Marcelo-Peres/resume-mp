from dateutil.relativedelta import relativedelta
from pandas import to_datetime

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_via_consulting_info(info_requested: str, idiom: str)-> str:
    
    ini_date = to_datetime('2022-04-01').date()
    end_date = to_datetime('2022-09-30').date()
    diff_date = relativedelta(end_date, ini_date)

    years = diff_date.years
    months = diff_date.months

    if idiom == 'en':
        if years == 0:
            if months < 10:
                via_consulting_job = f'0{months} month(s)'
            else:
                via_consulting_job = f'{months} month(s)'
        else:
            if months < 10:
                via_consulting_job = f'0{years} years and 0{months} month(s)'
            else:
                via_consulting_job = f'0{years} years and {months} month(s)'
        
        title = f'Data Engineer Consultant | Via Consulting | {via_consulting_job}'
        info = f'''
        {div_ini}

        #### Apr 2022 to Sep 2022
        
        {div_end}
        '''
    
    elif idiom == 'br':
        if years == 0:
            if months == 1:
                via_consulting_job = f'0{months} mês'
            elif months < 10:
                via_consulting_job = f'0{months} meses'
            else:
                via_consulting_job = f'{months} meses'
        else:
            if months == 1:
                via_consulting_job = f'0{years} ano(s) e 0{months} mês'
            if months < 10:
                via_consulting_job = f'0{years} ano(s) e 0{months} meses'
            else:
                via_consulting_job = f'0{years} ano(s) e {months} meses'
        
        title = f'Engenheiro de Dados Consultor | Via Consulting | {via_consulting_job}'
        info = f'''
        {div_ini}

        ####  De Abril de 2022 até Setembro de 2022
        
        {div_end}
        '''

    return eval(info_requested)

def get_via_consulting_project_03(info_requested: str, idiom: str)-> str:

    ini_date = to_datetime('2022-08-01').date()
    end_date = to_datetime('2022-09-01').date()
    diff_date = relativedelta(end_date, ini_date)

    years = diff_date.years
    months = diff_date.months

    if idiom == 'en':
        if years == 0:
            if months < 10:
                p03 = f'0{months} month(s)'
            else:
                p03 = f'{months} month(s)'
        else:
            if months < 10:
                p03 = f'0{years} years and 0{months} month(s)'
            else:
                p03 = f'0{years} years and {months} month(s)'
        
        title = f'Project - Gol Spend & Get| {p03}'
        info = f'''
        {div_ini}

        #### Ago 2022 to Ago 2022
        #### Smiles S.A.

        AWS Python lambda function that validates files to be called by an API.
        
        Resources:
        
        - Cloud Formation | Python with unit tests | Github release info | Jenkins to observe github uploaded code | Sonar for code quality | End of Devops stack with deploy.
        
        {div_end}
        '''
    
    elif idiom == 'br':
        if years == 0:
            if months == 1:
                p03 = f'0{months} mês'
            elif months < 10:
                p03 = f'0{months} meses'
            else:
                p03 = f'{months} meses'
        else:
            if months == 1:
                p03 = f'0{years} ano(s) e 0{months} mês'
            if months < 10:
                p03 = f'0{years} ano(s) e 0{months} meses'
            else:
                p03 = f'0{years} ano(s) e {months} meses'
        
        title = f'Projeto - Gol Gaste & Ganhe | {p03}'
        info = f'''
        {div_ini}

        #### De Agosto de 2022 até Agosto de 2022
        #### Smiles S.A.

        Função Lambda AWS Python que valida arquivos para serem enviados para uma API.
        
        Recursos:
        
        - Cloud Formation | Python com testes unitários | Github CICD | Jenkins para observabilidade | Sonar para qualidade de código | Finalização do código no repositório.
        
        {div_end}
        '''

    return eval(info_requested)


def get_via_consulting_project_02(info_requested: str, idiom: str)-> str:

    ini_date = to_datetime('2022-07-01').date()
    end_date = to_datetime('2022-08-01').date()
    diff_date = relativedelta(end_date, ini_date)
    
    years = diff_date.years
    months = diff_date.months

    if idiom == 'en':
        if years == 0:
            if months < 10:
                p02 = f'0{months} month(s)'
            else:
                p02 = f'{months} month(s)'
        else:
            if months < 10:
                p02 = f'0{years} years and 0{months} month(s)'
            else:
                p02 = f'0{years} years and {months} month(s)'
        
        title = f'Project - Zendesk Replication | {p02}'
        info = f'''
        {div_ini}

        #### Jul 2022 to Jul 2022

        Continuous pushing of data in a AWS environment using tools like:
        
        - Pyspark Spark Glue jobs | Cloud Formation | AWS Athena | Apache Hudi metadata for data governance.
        {div_end}
        '''

    elif idiom == 'br':
        if years == 0:
            if months == 1:
                p02 = f'0{months} mês'
            elif months < 10:
                p02 = f'0{months} meses'
            else:
                p02 = f'{months} meses'
        else:
            if months == 1:
                p02 = f'0{years} ano(s) e 0{months} mês'
            if months < 10:
                p02 = f'0{years} ano(s) e 0{months} meses'
            else:
                p02 = f'0{years} ano(s) e {months} meses'
        
        title = f'Projeto - Replicação Zendesk | {p02}'
        info = f'''
        {div_ini}

        #### De Julho de 2022 até Julho de 2022

        Processo contínuo de envio de dados numa ambiente AWS usando ferramentas como:
        
        - Pyspark Spark Glue jobs | Cloud Formation | AWS Athena | Apache Hudi metadata for data governance.
        {div_end}
        '''

    return eval(info_requested)

def get_via_consulting_project_01(info_requested:str, idiom: str)-> str:

    ini_date = to_datetime('2022-06-01').date()
    end_date = to_datetime('2022-09-30').date()
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
        
        title = f'Project Unimed - Stuffed Wallet | {p01}'
        info = f'''
        {div_ini}

        #### Apr 2022 to Jun 2022
        #### Unimed Insurance

        Colaborating with the team in a ETL process using tools like:
        
        - Informatica Powercenter | PLSQL - Oracle.
        
        The idea of the project is a campaign that supports the score of the company's brokers.
            
        {div_end}
        '''
    
    elif idiom == 'br':
        if years == 0:
            if months == 1:
                p02 = f'0{months} mês'
            elif months < 10:
                p02 = f'0{months} meses'
            else:
                p02 = f'{months} meses'
        else:
            if months == 1:
                p02 = f'0{years} ano(s) e 0{months} mês'
            if months < 10:
                p02 = f'0{years} ano(s) e 0{months} meses'
            else:
                p02 = f'0{years} ano(s) e {months} meses'

        title = f'Projeto Unimed - Carteira Recheada | {p02}'
        info = f'''
        {div_ini}

        #### De Abril de 2022 até Junho de 2022
        #### Unimed Seguros

        Colaborando com a equipe em processos de ETL usando ferramentas como:
        
        - Informatica Powercenter | PLSQL - Oracle.
        
        A idea do projeto é uma campanha que apoia a pontuação dos corretoras da empresa e posteriormente premiação.
            
        {div_end}
        '''

    return eval(info_requested)
