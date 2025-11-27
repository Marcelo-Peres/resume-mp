from markdown_pdf import MarkdownPdf, Section
from about.content import get_about_introduction
from experience.apllos import (
    get_apllos_info,
    get_apllos_current_project,
    get_apllos_gab_project,
    get_apllos_audlab_project
)
from experience.a3data import (
    get_a3data_info,
    get_a3data_stellantis_project
)
from experience.via_consulting import (
    get_via_consulting_info,
    get_via_consulting_gol_project,
    get_via_consulting_zendesk_project,
    get_via_consulting_unimed_project
)
from experience.bi4all import (
    get_bi4all_info,
    get_bi4all_bi_project
)
from experience.clif import (
    get_clif_info,
    get_clif_project
)

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

introduction = get_about_introduction()
image = '[![img](img/img-project.png)](https://github.com/Marcelo-Peres/dbt-snowflake-airflow)'

img = '''
<figure>
  <img src="img/img-project.png" alt="Example image" width="800" height="300">
</figure>
'''
# <figcaption>This is a caption for the image.</figcaption>

experiences = '## Work Experience'

aplos_title = '### ' + get_apllos_info('title')
aplos_info = get_apllos_info('info').strip()

apllos_current_title = '### ' + get_apllos_current_project('title')
apllos_current_info = '\n'.join([data.strip() for data in get_apllos_current_project('info').split('\n')])

apllos_gab_title = '### ' + get_apllos_gab_project('title')
apllos_gab_info = '\n'.join([data.strip() for data in get_apllos_gab_project('info').split('\n')])

apllos_audlab_title = '### ' + get_apllos_audlab_project('title')
apllos_audlab_info = '\n'.join([data.strip() for data in get_apllos_audlab_project('info').split('\n')])

a3data_title = '### ' + get_a3data_info('title')
a3data_info = '\n'.join([data.strip() for data in get_a3data_info('info').split('\n')])

a3data_stellantis_title = get_a3data_stellantis_project('title')
a3data_stellantis_info = '\n'.join([data.strip() for data in get_a3data_stellantis_project('info').split('\n')])

via_consulting_title = '### ' + get_via_consulting_info('title')
via_consulting_info = '\n'.join([data.strip() for data in get_via_consulting_info('info').split('\n')])

via_consulting_gol_title = '### ' + get_via_consulting_gol_project('title')
via_consulting_gol_info = '\n'.join([data.strip() for data in get_via_consulting_gol_project('info').split('\n')])

via_consulting_zendesk_title = '### ' + get_via_consulting_zendesk_project('title')
via_consulting_zendesk_info = '\n'.join([data.strip() for data in get_via_consulting_zendesk_project('info').split('\n')])

via_consulting_unimed_title = '### ' + get_via_consulting_unimed_project('title')
via_consulting_unimed_info = '\n'.join([data.strip() for data in get_via_consulting_unimed_project('info').split('\n')])

bi4all_title = '### ' + get_bi4all_info('title')
bi4all_info = '\n'.join([data.strip() for data in get_bi4all_info('info').split('\n')])

bi4all_bi_title = '### ' + get_bi4all_bi_project('title')
bi4all_bi_info = '\n'.join([data.strip() for data in get_bi4all_bi_project('info').split('\n')])

clif_title = '### ' + get_clif_info('title')
clif_info = '\n'.join([data.strip() for data in get_clif_info('info').split('\n')])

clif_project_title = '### ' + get_clif_project('title')
clif_project_info = '\n'.join([data.strip() for data in get_clif_project('info').split('\n')])

result = '\n\n'.join([
    '#',
    name,
    persoanl_info,
    '---',
    introduction,
    '---',
    '## Project Example',
    img,
    '---',
    new_page,
    experiences,
    '---',
    aplos_title,
    aplos_info,
    '---',
    apllos_current_title,
    apllos_current_info,
    '---',
    apllos_gab_title,
    apllos_gab_info,
    '---',
    new_page,
    '---',
    apllos_audlab_title,
    apllos_audlab_info,
    '---',
    a3data_title,
    '---',
    a3data_stellantis_info,
    '---',
    new_page,
    '---',
    via_consulting_title,
    via_consulting_info,
    '---',
    via_consulting_gol_title,
    via_consulting_gol_info,
    '---',
    via_consulting_zendesk_title,
    via_consulting_zendesk_info,
    '---',
    new_page,
    '---',
    via_consulting_unimed_title,
    via_consulting_unimed_info,
    '---',
    bi4all_title,
    bi4all_info,
    '---',
    bi4all_bi_title,
    '---',
    bi4all_bi_info,
    '---',
    new_page,
    '---',
    clif_title,
    clif_info,
    '---',
    clif_project_title,
    '---',
    clif_project_info
])

# Create a MarkdownPdf object
pdf = MarkdownPdf()

def load_data_for_pdf():
    # Add a section to the PDF from your Markdown file
    # Replace 'your_markdown_file.md' with the actual path to your MD file

    pdf.add_section(Section(result))

    # Optionally, set metadata for the PDF
    pdf.meta['title'] = 'My Resume'
    pdf.meta['author'] = 'Marcelo Peres'

    # Save the PDF to a file
    # Replace 'output.pdf' with your desired output filename
    return pdf.save('static/Marcelo_Peres_Resume.pdf')