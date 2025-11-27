def get_about_introduction(info_requested: str = '')-> str:
    '''
    Get Introduction Information

    :param info_requested: Parts of text
    from p1 to p5
    :type info_requested: str
    :return: Text called p1 to p5
    :rtype: str
    '''    
    div_ini = '<div style="text-align: justify;">'
    div_end = '</div>'

    p1 = f'I am a Big Data Engineer with 8 years of experience specializing in Python, PySpark, and Spark SQL.'
    p2 = f'For the past 2 years, I have been working extensively in the Databricks ecosystem within the AWS platform, leading efforts to migrate complex ETL/ELT processes from EMR clusters.'
    p3 = f'I have hands-on experience with data orchestration tools, particularly Apache Airflow and Control-M, where I designed and optimized workflows for scalable data pipelines. I have been making a lot efforts to work with Airflow and enable me to do efficiently schedule, monitor, and maintain reliable data operations across distributed systems.'
    p4 = f'With a passion for collaboration, I excel in fostering teamwork by sharing knowledge and best practices to help teams grow and achieve business goals. I firmly believe that the greatest asset a professional can have is the ability to share skills and empower others without fear of competition.'
    p5 = f'My commitment to technical excellence and continuous learning drives me to stay at the forefront of emerging technologies, always delivering value and maintaining high development standards.'

    if info_requested.startswith('p'):
        return div_ini + eval(info_requested) + div_end
    else:
        return '\n\n'.join([div_ini, p1, p2, p3, p4, p5, div_end])
