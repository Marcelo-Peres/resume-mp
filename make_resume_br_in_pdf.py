from markdown_pdf import MarkdownPdf, Section
from about.content import get_about_introduction
from experience.apllos import (
    get_apllos_info,
    get_apllos_project_05,
    get_apllos_project_04,
    get_apllos_project_03,
    get_apllos_project_02,
    get_apllos_project_01
)
from experience.a3data import (
    get_a3data_info,
    get_a3data_project_01
)
from experience.via_consulting import (
    get_via_consulting_info,
    get_via_consulting_project_03,
    get_via_consulting_project_02,
    get_via_consulting_project_01
)
from experience.bi4all import (
    get_bi4all_info,
    get_bi4all_project_01
)
from experience.clif import (
    get_clif_info,
    get_clif_project_01
)

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'

new_page = '<div style="page-break-after: always;"></div>'

name = '## Marcelo Peres'

persoanl_info = '''
### Engenheiro de Big Data
|                      |
|----------------------|
| Email: brmarcelo.peres@gmail.com |
| LinkedIn: [My Profile](https://www.linkedin.com/in/marcelo-peres-de/) |
| Github: [My Repo!](https://github.com/Marcelo-Peres?tab=repositories) |
'''

introduction = div_ini + '\n\n'.join(get_about_introduction('br')) + div_end
image = '[![img](img/img-project.png)](https://github.com/Marcelo-Peres/dbt-snowflake-airflow)'

img = '''
<figure>
  <img src="img/img-project.png" alt="Example image" width="800" height="300">
</figure>
'''
# <figcaption>This is a caption for the image.</figcaption>

experiences = '## Experiências Profissionais'

apllos_title, apllos_info = get_apllos_info(idiom = 'br')
apllos_title = '### ' + apllos_title
apllos_info = apllos_info.strip()

apllos_p05_title, apllos_p05_info = get_apllos_project_05(idiom = 'br')
apllos_p05_title = '### ' + apllos_p05_title
apllos_p05_info = '\n'.join([data.strip() for data in apllos_p05_info.split('\n')])

apllos_p04_title, apllos_p04_info = get_apllos_project_04(idiom = 'br')
apllos_p04_title = '### ' + apllos_p04_title
apllos_p04_info = '\n'.join([data.strip() for data in apllos_p04_info.split('\n')])

apllos_p03_title, apllos_p03_info = get_apllos_project_03(idiom = 'br')
apllos_p03_title = '### ' + apllos_p03_title
apllos_p03_info = '\n'.join([data.strip() for data in apllos_p03_info.split('\n')])

apllos_p02_title, apllos_p02_info = get_apllos_project_02(idiom = 'br')
apllos_p02_title = '### ' + apllos_p02_title
apllos_p02_info = '\n'.join([data.strip() for data in apllos_p02_info.split('\n')])

apllos_p01_title, apllos_p01_info = get_apllos_project_01(idiom = 'br')
apllos_p01_title = '### ' + apllos_p01_title
apllos_p01_info = '\n'.join([data.strip() for data in apllos_p01_info.split('\n')])

a3data_title, a3data_info = get_a3data_info(idiom = 'br')
a3data_title = '### ' + a3data_title
a3data_info = '\n'.join([data.strip() for data in a3data_info.split('\n')])

a3data_p01_title, a3data_p01_info = get_a3data_project_01(idiom = 'br')
a3data_p01_title = '### ' + a3data_p01_title
a3data_p01_info = '\n'.join([data.strip() for data in a3data_p01_info.split('\n')])

via_consulting_title, via_consulting_info = get_via_consulting_info(idiom = 'br')
via_consulting_title = '### ' + via_consulting_title
via_consulting_info = '\n'.join([data.strip() for data in via_consulting_info.split('\n')])

via_consulting_p03_title, via_consulting_p03_info = get_via_consulting_project_03(idiom = 'br')
via_consulting_p03_title = '### ' + via_consulting_p03_title
via_consulting_p03_info = '\n'.join([data.strip() for data in via_consulting_p03_info.split('\n')])

via_consulting_p02_title, via_consulting_p02_info = get_via_consulting_project_02(idiom = 'br')
via_consulting_p02_title = '### ' + via_consulting_p02_title
via_consulting_p02_info = '\n'.join([data.strip() for data in via_consulting_p02_info.split('\n')])

via_consulting_p01_title, via_consulting_p01_info = get_via_consulting_project_01(idiom = 'br')
via_consulting_p01_title = '### ' + via_consulting_p01_title
via_consulting_p01_info = '\n'.join([data.strip() for data in via_consulting_p01_info.split('\n')])

bi4all_title, bi4all_info = get_bi4all_info(idiom = 'br')
bi4all_title = '### ' + bi4all_title
bi4all_info = '\n'.join([data.strip() for data in bi4all_info.split('\n')])

bi4all_p01_title, bi4all_p01_info = get_bi4all_project_01(idiom = 'br')
bi4all_p01_title = '### ' + bi4all_p01_title
bi4all_p01_info = '\n'.join([data.strip() for data in bi4all_p01_info.split('\n')])

clif_title, clif_info = get_clif_info(idiom = 'br')
clif_title = '### ' + clif_title
clif_info = '\n'.join([data.strip() for data in clif_info.split('\n')])

clif_p01_title, clif_p01_info = get_clif_project_01(idiom = 'br')
clif_p01_title = '### ' + clif_p01_title
clif_p01_info = '\n'.join([data.strip() for data in clif_p01_info.split('\n')])

result = '\n\n'.join([
    '#',
    name,
    persoanl_info,
    '---',
    introduction,
    '---',
    '[Github Exemplo de Projeto](https://github.com/Marcelo-Peres/dbt-snowflake-airflow)',
    img,
    '---',
    new_page,
    experiences,
    '---',
    apllos_title,
    apllos_info,
    '---',
    apllos_p05_title,
    apllos_p05_info,
    '---',
    apllos_p04_title,
    apllos_p04_info,
    '---',
    apllos_p03_title,
    apllos_p03_info,
    '---',
    new_page,
    '---',
    apllos_p02_title,
    apllos_p02_info,
    '---',
    apllos_p01_title,
    apllos_p01_info,
    '---',
    new_page,
    '---',
    a3data_title,
    a3data_info,
    '---',
    a3data_p01_title,
    a3data_p01_info,
    '---',
    new_page,
    '---',
    via_consulting_title,
    via_consulting_info,
    '---',
    via_consulting_p03_title,
    via_consulting_p03_info,
    '---',
    via_consulting_p02_title,
    via_consulting_p02_info,
    '---',
    via_consulting_p01_title,
    via_consulting_p01_info,
    '---',
    new_page,
    '---',
    bi4all_title,
    bi4all_info,
    '---',
    bi4all_p01_title,
    bi4all_p01_info,
    '---',
    new_page,
    '---',
    clif_title,
    clif_info,
    '---',
    clif_p01_title,
    clif_p01_info,
    '---'
])

# Create a MarkdownPdf object
pdf = MarkdownPdf()

def load_data_resume_br_for_pdf():
    # Add a section to the PDF from your Markdown file
    # Replace 'your_markdown_file.md' with the actual path to your MD file

    pdf.add_section(Section(result))

    # Optionally, set metadata for the PDF
    pdf.meta['title'] = 'Meu Currículo'
    pdf.meta['author'] = 'Marcelo Peres'

    # Save the PDF to a file
    # Replace 'output.pdf' with your desired output filename
    return pdf.save('static/Marcelo_Peres_CV.pdf')
