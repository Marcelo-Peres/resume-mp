from helper.py_helper import get_work_project_time

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_via_consulting_info(idiom: str)-> str:
    
    ini_date = '2022-04-01'
    end_date = '2022-09-30'
    
    job_time, detail = get_work_project_time(idiom = idiom, ini_date = ini_date, end_date = end_date)

    if idiom == 'en':
                
        title = f'Data Engineer Consultant | Via Consulting | {job_time}'
        info = f'''
        {div_ini}

        #{detail}
        
        {div_end}
        '''

        return title, info
    
    elif idiom == 'br':
                
        title = f'Engenheiro de Dados Consultor | Via Consulting | {job_time}'
        info = f'''
        {div_ini}

        #{detail}
        
        {div_end}
        '''

        return title, info

def get_via_consulting_project_03(idiom: str)-> str:

    ini_date = '2022-08-01'
    end_date = '2022-09-01'
    
    job_time, detail = get_work_project_time(idiom = idiom, ini_date = ini_date, end_date = end_date)

    if idiom == 'en':
                
        title = f'Project - Gol Spend & Get| {job_time}'
        info = f'''
        {div_ini}

        #{detail}
        #### Smiles S.A.

        AWS Python lambda function that validates files to be called by an API.
        
        Resources:
        
        - Cloud Formation | Python with unit tests | Github release info | Jenkins to observe github uploaded code | Sonar for code quality | End of Devops stack with deploy.
        
        {div_end}
        '''

        return title, info
    
    elif idiom == 'br':
        
        title = f'Projeto - Gol Gaste & Ganhe | {job_time}'
        info = f'''
        {div_ini}

        #{detail}
        #### Smiles S.A.

        Função Lambda AWS Python que valida arquivos para serem enviados para uma API.
        
        Recursos:
        
        - Cloud Formation | Python com testes unitários | Github CICD | Jenkins para observabilidade | Sonar para qualidade de código | Finalização do código no repositório.
        
        {div_end}
        '''

        return title, info


def get_via_consulting_project_02(idiom: str)-> str:

    ini_date = '2022-07-01'
    end_date = '2022-08-01'
    
    job_time, detail = get_work_project_time(idiom = idiom, ini_date = ini_date, end_date = end_date)

    if idiom == 'en':
                
        title = f'Project - Zendesk Replication | {job_time}'
        info = f'''
        {div_ini}

        #{detail}

        Continuous pushing of data in a AWS environment using tools like:
        
        - Pyspark Spark Glue jobs | Cloud Formation | AWS Athena | Apache Hudi metadata for data governance.
        {div_end}
        '''

        return title, info

    elif idiom == 'br':
                
        title = f'Projeto - Replicação Zendesk | {job_time}'
        info = f'''
        {div_ini}

        #{detail}

        Processo contínuo de envio de dados numa ambiente AWS usando ferramentas como:
        
        - Pyspark Spark Glue jobs | Cloud Formation | AWS Athena | Apache Hudi metadata for data governance.
        {div_end}
        '''

        return title, info

def get_via_consulting_project_01(idiom: str)-> str:

    ini_date = '2022-06-01'
    end_date = '2022-09-30'

    job_time, detail = get_work_project_time(idiom = idiom, ini_date = ini_date, end_date = end_date)

    if idiom == 'en':
                
        title = f'Project Unimed - Stuffed Wallet | {job_time}'
        info = f'''
        {div_ini}

        #{detail}
        #### Unimed Insurance

        Colaborating with the team in a ETL process using tools like:
        
        - Informatica Powercenter | PLSQL - Oracle.
        
        The idea of the project is a campaign that supports the score of the company's brokers.
            
        {div_end}
        '''

        return title, info
    
    elif idiom == 'br':
        
        title = f'Projeto Unimed - Carteira Recheada | {job_time}'
        info = f'''
        {div_ini}

        #{detail}
        #### Unimed Seguros

        Colaborando com a equipe em processos de ETL usando ferramentas como:
        
        - Informatica Powercenter | PLSQL - Oracle.
        
        A idea do projeto é uma campanha que apoia a pontuação dos corretoras da empresa e posteriormente premiação.
            
        {div_end}
        '''

        return title, info
