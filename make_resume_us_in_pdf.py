from markdown_pdf import MarkdownPdf, Section
from about.content import get_about_introduction
from experience.apllos import (
    get_apllos_info,
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
### Big Data Engineer
|                      |
|----------------------|
| Email: brmarcelo.peres@gmail.com |
| LinkedIn: [My Profile](https://www.linkedin.com/in/marcelo-peres-de/) |
| Github: [My Repo!](https://github.com/Marcelo-Peres?tab=repositories) |
'''

introduction = div_ini + '\n\n'.join(get_about_introduction('en')) + div_end
image = '[![img](img/img-project.png)](https://github.com/Marcelo-Peres/dbt-snowflake-airflow)'

img = '''
<figure>
  <img src="img/img-project.png" alt="Example image" width="800" height="300">
</figure>
'''
# <figcaption>This is a caption for the image.</figcaption>

experiences = '## Work Experience'

apllos_title = '### ' + get_apllos_info(info_requested = 'title', idiom = 'en')
apllos_info = get_apllos_info(info_requested = 'info', idiom = 'en').strip()

apllos_p03_title = '### ' + get_apllos_project_03(info_requested = 'title', idiom = 'en')
apllos_p03_info = '\n'.join([data.strip() for data in get_apllos_project_03(info_requested = 'info', idiom = 'en').split('\n')])

apllos_p02_title = '### ' + get_apllos_project_02(info_requested = 'title', idiom = 'en')
apllos_p02_info = '\n'.join([data.strip() for data in get_apllos_project_02(info_requested = 'info', idiom = 'en').split('\n')])

apllos_p01_title = '### ' + get_apllos_project_01(info_requested = 'title', idiom = 'en')
apllos_p01_info = '\n'.join([data.strip() for data in get_apllos_project_01(info_requested = 'info', idiom = 'en').split('\n')])

a3data_title = '### ' + get_a3data_info(info_requested = 'title', idiom = 'en')
a3data_info = '\n'.join([data.strip() for data in get_a3data_info(info_requested = 'info', idiom = 'en').split('\n')])

a3data_p01_title = '### ' + get_a3data_project_01(info_requested = 'title', idiom = 'en')
a3data_p01_info = '\n'.join([data.strip() for data in get_a3data_project_01(info_requested = 'info', idiom = 'en').split('\n')])

via_consulting_title = '### ' + get_via_consulting_info(info_requested = 'title', idiom = 'en')
via_consulting_info = '\n'.join([data.strip() for data in get_via_consulting_info(info_requested = 'info', idiom = 'en').split('\n')])

via_consulting_p03_title = '### ' + get_via_consulting_project_03(info_requested = 'title', idiom = 'en')
via_consulting_p03_info = '\n'.join([data.strip() for data in get_via_consulting_project_03(info_requested = 'info', idiom = 'en').split('\n')])

via_consulting_p02_title = '### ' + get_via_consulting_project_02(info_requested = 'title', idiom = 'en')
via_consulting_p02_info = '\n'.join([data.strip() for data in get_via_consulting_project_02(info_requested = 'info', idiom = 'en').split('\n')])

via_consulting_p01_title = '### ' + get_via_consulting_project_01(info_requested = 'title', idiom = 'en')
via_consulting_p01_info = '\n'.join([data.strip() for data in get_via_consulting_project_01(info_requested = 'info', idiom = 'en').split('\n')])

bi4all_title = '### ' + get_bi4all_info(info_requested = 'title', idiom = 'en')
bi4all_info = '\n'.join([data.strip() for data in get_bi4all_info(info_requested = 'info', idiom = 'en').split('\n')])

bi4all_p01_title = '### ' + get_bi4all_project_01(info_requested = 'title', idiom = 'en')
bi4all_p01_info = '\n'.join([data.strip() for data in get_bi4all_project_01(info_requested = 'info', idiom = 'en').split('\n')])

clif_title = '### ' + get_clif_info(info_requested = 'title', idiom = 'en')
clif_info = '\n'.join([data.strip() for data in get_clif_info(info_requested = 'info', idiom = 'en').split('\n')])

clif_p01_title = '### ' + get_clif_project_01(info_requested = 'title', idiom = 'en')
clif_p01_info = '\n'.join([data.strip() for data in get_clif_project_01(info_requested = 'info', idiom = 'en').split('\n')])

result = '\n\n'.join([
    '#',
    name,
    persoanl_info,
    '---',
    introduction,
    '---',
    '[Github Project Example](https://github.com/Marcelo-Peres/dbt-snowflake-airflow)',
    img,
    '---',
    new_page,
    experiences,
    '---',
    apllos_title,
    apllos_info,
    '---',
    apllos_p03_title,
    apllos_p03_info,
    '---',
    apllos_p02_title,
    apllos_p02_info,
    '---',
    new_page,
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

def load_data_resume_us_for_pdf():
    # Add a section to the PDF from your Markdown file
    # Replace 'your_markdown_file.md' with the actual path to your MD file

    pdf.add_section(Section(result))

    # Optionally, set metadata for the PDF
    pdf.meta['title'] = 'My Resume'
    pdf.meta['author'] = 'Marcelo Peres'

    # Save the PDF to a file
    # Replace 'output.pdf' with your desired output filename
    return pdf.save('static/Marcelo_Peres_EN_Resume.pdf')