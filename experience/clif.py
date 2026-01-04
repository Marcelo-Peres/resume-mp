from helper.py_helper import get_work_project_time

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_clif_info(idiom: str)-> str:

    ini_date = '2019-04-01'
    end_date = '2021-06-30'
    
    job_time, detail = get_work_project_time(idiom = idiom, ini_date = ini_date, end_date = end_date)

    if idiom == 'en':
        
        title = f'IT Analyst | CLIF | {job_time}'
        info = f'''
        {div_ini}

        #{detail}

        {div_end}
        '''

        return title, info
    
    elif idiom == 'br':
        
        title = f'Analista de TI | CLIF | {job_time}'
        info = f'''
            {div_ini}

            #{detail}

            {div_end}
            '''

        return title, info

def get_clif_project_01(idiom: str)-> str:

    ini_date = '2019-04-01'
    end_date = '2021-06-30'
    
    job_time, detail = get_work_project_time(idiom = idiom, ini_date = ini_date, end_date = end_date)
    
    if idiom == 'en':
                
        title = f'Systems and BI Management | CLIF | {job_time}'
        info = f'''
        {div_ini}

        #{detail}
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

        return title, info
    
    elif idiom == 'br':
        
        title = f'Gestor de Sistemas e desenvolvedor de BI | CLIF | {job_time}'
        info = f'''
        {div_ini}

        #{detail}
        #### CLIF - Centro Logístico Integrado FastCargo S.A
        #### Gestor de Sistemas

        - Responsável pela gestão dos sistemas SARA, Logix, My Checklist e Portal de Atendimento ao Cliente;
        - Aplicação de pacotes de atualização do sistema alfandegado SARA;
        - Atualização de procedimentos armazenados em SQL;
        - Atualizações de gatilhos SQL;
        - Revisões de módulos, entre outras atividades;
        - Criação de um script em Python para inserir e atualizar dados de navios e informações relacionadas no Portal de Atendimento ao Cliente;

        #### Desenvolvedor de BI

        Criação de relatórios no Power BI:

        - Gestão e controle de cadastros;
        - Gestão e controle de unidades;
        - Gestão e controle de transportes;
        - Gestão e controle de navios.

        Os relatórios acima são sincronizados e carregados no Power BI, contendo dados de 2 bancos de dados diferentes e um carregamento de dados de um script Python conectado a uma API disponibilizada pelo Porto Itapoá, contendo as datas de movimentação dos navios. Isso possibilita o cruzamento de todas as informações entre esses diferentes bancos de dados para uma melhor gestão dos ativos dos clientes.
        
        {div_end}
        '''

        return title, info
