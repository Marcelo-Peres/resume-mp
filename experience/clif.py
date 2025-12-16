from pandas import to_datetime
from dateutil.relativedelta import relativedelta

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_clif_info(info_requested:str, idiom: str)-> str:

    ini_date = to_datetime('2019-04-01').date()
    end_date = to_datetime('2021-06-30').date()
    diff_date = relativedelta(end_date, ini_date)

    years = diff_date.years
    months = diff_date.months

    if idiom == 'en':
        if years == 0:
            if months < 10:
                clif_job = f'0{months} month(s)'
            else:
                clif_job = f'{months} month(s)'
        else:
            if months < 10:
                clif_job = f'0{years} years and 0{months} month(s)'
            else:
                clif_job = f'0{years} years and {months} month(s)'
            
        title = f'IT Analyst | CLIF | {clif_job}'
        info = f'''
        {div_ini}

        #### Apr 2019 to Jun 2021

        {div_end}
        '''
    
    elif idiom == 'br':
        if years == 0:
            if months == 1:
                clif_job = f'0{months} mês'
            elif months < 10:
                clif_job = f'0{months} meses'
            else:
                clif_job = f'{months} meses'
        else:
            if months == 1:
                clif_job = f'0{years} ano(s) e 0{months} mês'
            if months < 10:
                clif_job = f'0{years} ano(s) e 0{months} meses'
            else:
                clif_job = f'0{years} ano(s) e {months} meses'

        title = f'Analista de TI | CLIF | {clif_job}'
        info = f'''
            {div_ini}

            #### De Abril de 2019 até Junho de 2021

            {div_end}
            '''

    return eval(info_requested)

def get_clif_project_01(info_requested: str, idiom: str)-> str:

    ini_date = to_datetime('2019-04-01').date()
    end_date = to_datetime('2021-06-30').date()
    diff_date = relativedelta(end_date, ini_date)

    years = diff_date.years
    months = diff_date.months

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
        
        title = f'Systems and BI Management | CLIF | {p01}'
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

        title = f'Gestor de Sistemas & desenvolvedor deBI | CLIF | {p01}'
        info = f'''
        {div_ini}

        #### Abril de 2019 até Junho de 2021
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

    return eval(info_requested)
