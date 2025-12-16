def get_about_introduction(info_requested: str)-> list:
    '''
    Get Introduction Information

    :param info_requested: Parts of text
    from p1 to p5
    :type info_requested: str
    :return: Text called p1 to p5
    :rtype: str
    '''    
    
    u1 = f'I am a Big Data Engineer with 8 years of experience specializing in Python, PySpark, and Spark SQL.'
    u2 = f'For the past 2 years, I have been working extensively in the Databricks ecosystem within the AWS platform, leading efforts to migrate complex ETL/ELT processes from EMR clusters.'
    u3 = f'I have hands-on experience with data orchestration tools, particularly Apache Airflow and Control-M, where I designed and optimized workflows for scalable data pipelines. I have been making a lot efforts to work with Airflow and enable me to do efficiently schedule, monitor, and maintain reliable data operations across distributed systems.'
    u4 = f'With a passion for collaboration, I excel in fostering teamwork by sharing knowledge and best practices to help teams grow and achieve business goals. I firmly believe that the greatest asset a professional can have is the ability to share skills and empower others without fear of competition.'
    u5 = f'My commitment to technical excellence and continuous learning drives me to stay at the forefront of emerging technologies, always delivering value and maintaining high development standards.'

    en_list = [u1, u2, u3, u4, u5]

    p1 = f'Sou um Engenheiro de Big Data com 8 anos de experiência, especializado em Python, PySpark e Spark SQL.'
    p2 = f'Nos últimos dois anos, tenho trabalhado intensamente no ecossistema Databricks dentro da plataforma AWS, liderando esforços para migrar processos complexos de ETL/ELT de clusters EMR.'
    p3 = f'Tenho experiência prática com ferramentas de orquestração de dados, particularmente Apache Airflow e Control-M, onde projetei e otimizei fluxos de trabalho para pipelines de dados escaláveis. Tenho me dedicado bastante ao Airflow, o que me permite agendar, monitorar e manter operações de dados confiáveis ​​em sistemas distribuídos de forma eficiente.'
    p4 = f'Com paixão pela colaboração, destaco-me na promoção do trabalho em equipe, compartilhando conhecimento e boas práticas para ajudar as equipes a crescer e alcançar seus objetivos de negócios. Acredito firmemente que o maior trunfo que um profissional pode ter é a capacidade de compartilhar habilidades e empoderar outras pessoas sem medo da competição.'
    p5 = f'Meu compromisso com a excelência técnica e o aprendizado contínuo me impulsiona a estar na vanguarda das tecnologias emergentes, sempre agregando valor e mantendo altos padrões de desenvolvimento.'

    br_list = [p1, p2, p3, p4, p5]

    if info_requested =='en':
        return en_list
    elif info_requested == 'br':
        return br_list