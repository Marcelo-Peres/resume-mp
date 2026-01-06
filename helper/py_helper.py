from dateutil.relativedelta import relativedelta
from pandas import to_datetime
def get_work_project_time(
        idiom: str,
        ini_date: str,
        end_date: str = '')-> tuple[str, str]:

    meses_pt = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    
    ini_date = to_datetime(ini_date).date()
    ini_year = ini_date.year
    
    ini_month_us = ini_date.strftime('%B')
    ini_data_info_us = f'{ini_month_us} {ini_year}'

    ini_month_br = meses_pt[ini_date.month]
    ini_data_info_br = f'{ini_month_br} {ini_year}'

    if idiom == 'en':

        if end_date == '':
            end_date = to_datetime('now').date()
            end_year = end_date.year
            end_data_info = 'Nowadays'
        else:
            end_date = to_datetime(end_date).date()
            end_year = end_date.year
            end_month = end_date.strftime('%B')
            end_data_info = f'{end_month} {end_year}'
    
        diff_date = relativedelta(end_date, ini_date)
        
        years = str(diff_date.years).zfill(2)
        months = str(diff_date.months).zfill(2)
                
        if years == '00':
            if months == '01':
                job_time = f'{months} month'
            else:
                job_time = f'{months} months'
        elif years == '01':
            if months == '00':
                job_time = f'{years} year'
            elif months == '01':
                job_time = f'{years} year and {months} month'
            else:
                job_time = f'{years} year and {months} months'
        else:
            if months == '00':
                job_time = f'{years} years'
            elif months == '01':
                job_time = f'{years} years and {months} month'
            else:
                job_time = f'{years} years and {months} months'
        
        info = f'### From {ini_data_info_us} to {end_data_info}'

        return job_time, info
    
    elif idiom == 'br':
    
        if end_date == '':
            end_date = to_datetime('now').date()
            end_year = end_date.year
            end_data_info = 'o presente momento'
        else:
            end_date = to_datetime(end_date).date()
            end_year = end_date.year
            end_month = meses_pt[end_date.month]
            end_data_info = f'{end_month} {end_year}'
    
        diff_date = relativedelta(end_date, ini_date)
        
        years = str(diff_date.years).zfill(2)
        months = str(diff_date.months).zfill(2)

        if years == '00':
            if months == '01':
                job_time = f'{months} mês'
            else:
                job_time = f'{months} meses'
        elif years == '01':
            if months == '00':
                job_time = f'{years} ano'
            elif months == '01':
                job_time = f'{years} ano e {months} mês'
            else:
                job_time = f'{years} ano e {months} meses'
        else:
            if months == '00':
                job_time = f'{years} anos'
            elif months == '01':
                job_time = f'{years} anos e {months} mês'
            else:
                job_time = f'{years} anos e {months} meses'

        info = f'### Desde {ini_data_info_br} até {end_data_info}'

        return job_time, info
