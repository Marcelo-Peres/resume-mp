from dateutil.relativedelta import relativedelta
from pandas import to_datetime

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

def get_apllos_info(info_requested:str, idiom: str)-> str:

    ini_date = to_datetime('2023-07-01').date()
    end_date = to_datetime('now').date()
    diff_date = relativedelta(end_date, ini_date)

    years = diff_date.years
    months = diff_date.months

    if idiom == 'en':
        if years == 0:
            if months < 10:
                p04 = f'0{months} month(s)'
            else:
                p04 = f'{months} month(s)'
        else:
            if months < 10:
                p04 = f'0{years} years and 0{months} month(s)'
            else:
                p04 = f'0{years} years and {months} month(s)'

        title = f'Senior Big Data Engineer | Apllos Solutions | {p04}'
        info = f'''
        #### From Jul 2023 to nowadays
        '''
        return eval(info_requested)
    
    elif idiom == 'br':
        if years == 0:
            if months == 1:
                p04 = f'0{months} mês'
            elif months < 10:
                p04 = f'0{months} meses'
            else:
                p04 = f'{months} meses'
        else:
            if months == 1:
                p04 = f'0{years} ano(s) e 0{months} mês'
            if months < 10:
                p04 = f'0{years} ano(s) e 0{months} meses'
            else:
                p04 = f'0{years} ano(s) e {months} meses'

        title = f'Engenheiro Big Data Senior | Apllos Solutions | {p04}'
        info = f'''
        #### Desde Julho de 2023 até o presente momento
        '''
        
        return eval(info_requested)

def get_apllos_project_03(info_requested: str, idiom: str)-> str:
    
    ini_date = to_datetime('2025-01-01').date()
    end_date = to_datetime('now').date()
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
    
        title = f'Project Audlab | {p03}'
        info = f'''
        {div_ini}

        #### From Jan 2025 to nowadays
                
        Now developing into data lake Delta Lake tables and Postgre tables for Gerdau Commercial Assets.
        Some tables in Postgres for apps interaction and decision making through PBI Reports.

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
                p04 = f'0{years} ano(s) e 0{months} mês'
            if months < 10:
                p04 = f'0{years} ano(s) e 0{months} meses'
            else:
                p04 = f'0{years} ano(s) e {months} meses'

        title = f'Projeto Audlab | {p03}'
        info = f'''
        {div_ini}
        
        #### De Janeiro de 2025 até o presente momento
        
        Atualmente desenvolvendo um data lake com tabelas Delta Lake e tabelas PostgreSQL para os ativos comerciais da Gerdau.
        Algumas tabelas no PostgreSQL servem para interação com aplicativos e tomada de decisões por meio de relatórios do Power BI.

        {div_end}
        '''

    return eval(info_requested)

def get_apllos_project_02(info_requested: str, idiom: str)-> str:
    
    ini_date = to_datetime('2024-09-01').date()
    end_date = to_datetime('2024-12-31').date()
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
        
        title = f'Project GAB - Industrial Maintenance | {p02}'
        info = f'''
        {div_ini}
        
        #### From Sep 2024 to Dec 2024

        In charge of migrate and rebuild ETL process in Pyspark.
        The original scope was only migrate the scripts and put in a CICD environment, and configure jobs schedule in Control-M plataform.

        However, due to a delay faced through PBI workflows, the project suffered a change bringing a big part of process to databricks.
        New tables were created, steps were adpted and the project ajusted.

        Final charge time has been reduced and the PBI charges becmes faster. 
                
        For three large tables the gains were awesome as below mentioned: 

        - **The first table took 01h20 before.**
        - **The second one took 03h13 before.**
        - **The third one took 01h30 before.**
        
        **Now each one of them is taking 10 minutes or less for loading PBI Insights.**

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

        title = f'Projeto GAB - Manutenção Industrial | {p02}'
        info = f'''
        {div_ini}
        
        #### De Setembro de 2024 até Dezembre de 2024

        Responsável pela migração e reconstrução do processo ETL em PySpark.
        O escopo original era apenas migrar os scripts e implementá-los em um ambiente CI/CD, além de configurar o agendamento de jobs na plataforma Control-M.

        No entanto, devido a um atraso nos fluxos de trabalho do Power BI, o projeto sofreu uma alteração, levando grande parte do processo para o Databricks.

        Novas tabelas foram criadas, etapas foram adaptadas e o projeto foi ajustado.

        O tempo de faturamento final foi reduzido e o faturamento do Power BI tornou-se mais rápido.

        Para três tabelas grandes, os ganhos foram impressionantes, conforme mencionado abaixo:

        - **A primeira tabela levava 01h20.**
        - **A segunda levava 03h13.**
        - **A terceira levava 01h30.**
        
        **Agora cada uma das tabelas leva apenas 10 minutos ou menos para carregar os dados para o Power BI.**

        {div_end}
        '''

    return eval(info_requested)

def get_apllos_project_01(info_requested: str, idiom: str)-> str:
        
    ini_date = to_datetime('2023-07-01').date()
    end_date = to_datetime('2024-09-30').date()
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
        
        title = f'Project Databricks Migration Audlab | {p01}'
        info = f'''
        {div_ini}
        
        #### From Jul 2023 to Sep 2024

        In charge of data ingestions.

        Audlab is an Audit department in Gerdau Company.
        Gerdau is an important enterprise in Brazil that works with iron and steel, producing several tools for different segments in the world.

        In this department I provide a full control of gitlab and deploying scripts.

        Control - M is responsible to execute EMR clusters and scripts in python and pyspark through different assets.
        Producing ETL and Data Science Scripts for machine learning and data transformation.

        I was one of core people helping data migration steps from AWS tools to Databricks.
        EMR clusters now replicated accordingly in Databricks.

        The migration was well successed.
        Finnaly working in Databricks.

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

        title = f'Projeto Audlab | {p02}'
        info = f'''
        {div_ini}
        
        #### De Julho de 2023 até Setembro de 2024

        Responsável pela ingestão de dados.

        A Audlab é um departamento de Auditoria na empresa Gerdau.
        A Gerdau é uma importante empresa brasileira do setor metalurgico, que produz diversas ferramentas para diferentes segmentos globais.
        Neste departamento, eu tinha controle total do GitLab e da implantação de scripts.
        
        O Control-M era responsável pela execução de clusters EMR e scripts em Python e PySpark por meio de diferentes recursos.
        Produzia scripts de ETL e Ciência de Dados para aprendizado de máquina e transformação de dados.
        Fui um dos principais responsáveis p​ela migração de dados das ferramentas da AWS para o Databricks.

        Os clusters EMR agora estão replicados corretamente no Databricks.
        A migração foi um sucesso.

        Finalmente, estou trabalhando no Databricks.

        {div_end}
        '''

    return eval(info_requested)
