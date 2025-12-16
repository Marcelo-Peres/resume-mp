# ------ Personal Resume App (Advanced with placeholders) ------
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from streamlit_option_menu import option_menu

from make_resume_us_in_pdf import load_data_resume_us_for_pdf
from make_resume_br_in_pdf import load_data_resume_for_pdf

from plotly import graph_objects as go

from about.content import get_about_introduction
from img.img import get_mp_img, get_mp_git, get_mp_linkedin
from skills.content import get_skills_info

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

from education.content import get_education_info

div_ini = '<div style="text-align: justify;">'
div_end = '</div>'
# Sidebar for navigation
with st.sidebar:
    origem_selected = option_menu(
        menu_title = 'Select Language',
        options = ['English US', 'Português BR'],
        icons = ['globe', 'globe'],
        menu_icon = 'cast',
        default_index = 0,
        styles = {
            #"container": {"padding": "0!important", "background-color": "#f0f2f6"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#d3daddab"},
            "nav-link-selected": {"background-color": "#d3daddab"}
        }
    )
if origem_selected == 'English US':
    idiom_idioma = 'en'
    options = ['About', 'Skills', 'Experience', 'Education', 'Contact', 'Resume']
    subtitle = 'Big Data Engineer'
    title_menu = 'Navigation'
    introduction = get_about_introduction('en')
    habilidades_skills = 'Skills Overview'
    experience_experiencia = 'Experience'
    job_trabalho = 'Current Job'
    previous_antes_job_trabalho = 'Previous Jobs'
    education_educacao = 'Education'
    education_educacao_ref = '<< Get in Touch >>'

elif origem_selected == 'Português BR':
    idiom_idioma = 'br'
    options = ['Sobre', 'Habilidades', 'Experiência', 'Formação', 'Contato', 'Currículo']
    subtitle = 'Engenheiro de Big Data'
    title_menu = 'Menu'
    introduction = get_about_introduction('br')
    habilidades_skills = 'Habilidades Demonstradas'
    experience_experiencia = 'Experiência'
    job_trabalho = 'Trabalho Atual'
    previous_antes_job_trabalho = 'Trabalhos Anteriores'
    education_educacao = 'Educação'
    education_educacao_ref = '<< Mantenha Contato >>'

with st.sidebar:
    selected = option_menu(
        menu_title = title_menu,
        options = options,
        icons = ['person', 'book', 'briefcase', 'clipboard-fill', 'envelope', 'file-earmark-person-fill'],
        menu_icon = 'cast',
        default_index = 0,
        styles = {
            #"container": {"padding": "0!important", "background-color": "#f0f2f6"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#d3daddab"},
            "nav-link-selected": {"background-color": "#d3daddab"}
        }
    )


# Header with name and title
st.title('Marcelo Peres')
st.subheader(subtitle)

if selected == options[0]:
    st.image(get_mp_img(), width = 400)
    st.write('\n', unsafe_allow_html = True)
    st.write(div_ini + introduction[0] + div_end, unsafe_allow_html = True)
    st.write('\n', unsafe_allow_html = True)
    st.write(div_ini + introduction[1] + div_end, unsafe_allow_html = True)
    st.write('\n', unsafe_allow_html = True)
    st.write(div_ini + introduction[2] + div_end, unsafe_allow_html = True)
    st.write('\n', unsafe_allow_html = True)
    st.write(div_ini + introduction[3] + div_end, unsafe_allow_html = True)
    st.write('\n', unsafe_allow_html = True)
    st.write(div_ini + introduction[4] + div_end, unsafe_allow_html = True)

elif selected == options[1]:
    # Title
    center_ini = '''<h1 style='text-align: center;'>'''
    center_end = '</h1>'
    title_info = habilidades_skills
    st.markdown(
    f"<h1 style='text-align: center;'> 🔎 {habilidades_skills} </h1>",
    unsafe_allow_html=True
    )

    skills_info_ = list(get_skills_info().keys())
    skills_values_ = list(get_skills_info().values())

    fig = go.Figure(go.Funnel(
        y = skills_info_,
        x = skills_values_,
        textposition = 'inside',
        texttemplate = "%{label}-> %{percentInitial:.0%}",
        # textinfo = 'percent initial',
        textfont = dict(size = 80, color = 'black'),
        marker = {
            'color': ['deepskyblue', 'lightsalmon', 'tan', 'teal', 'silver', 'white'],
            'line': {'color': ['wheat', 'wheat', 'blue', 'wheat', 'wheat']}},
        connector = {
            'line': {'color': 'royalblue', 'dash': 'dot', 'width': 3}
        }
    ))

    # Display in Streamlit
    fig.update_yaxes(visible = False)
    st.plotly_chart(fig, use_container_width = True)

elif selected == options[2]:
    # Title
    st.header(experience_experiencia)
    st.subheader(job_trabalho)
    # Apllos
    with st.expander(get_apllos_info(info_requested = 'title', idiom = idiom_idioma)):
        st.write(get_apllos_info(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)
        # Audlab Project
        with st.expander(get_apllos_project_03(info_requested = 'title', idiom = idiom_idioma)):
            st.write(get_apllos_project_03(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)
        # Gab Project
        with st.expander(get_apllos_project_02(info_requested = 'title', idiom = idiom_idioma)):
            st.write(get_apllos_project_02(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)
        # Audlab Project
        with st.expander(get_apllos_project_01(info_requested = 'title', idiom = idiom_idioma)):
            st.write(get_apllos_project_01(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)

    st.subheader(previous_antes_job_trabalho)
    with st.expander(get_a3data_info(info_requested = 'title', idiom = idiom_idioma)):
        st.write(get_a3data_info(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)
        # Stellantis #
        with st.expander(get_a3data_project_01(info_requested = 'title', idiom = idiom_idioma)):
            st.write(get_a3data_project_01(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)
    
    # Via Consulting 
    with st.expander(get_via_consulting_info(info_requested = 'title', idiom = idiom_idioma)):
        st.write(get_via_consulting_info(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)
        # Gol Project
        with st.expander(get_via_consulting_project_03(info_requested = 'title', idiom = idiom_idioma)):
            st.write(get_via_consulting_project_03(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)
        # Zendesk'
        with st.expander(get_via_consulting_project_02(info_requested = 'title', idiom = idiom_idioma)):
            st.write(get_via_consulting_project_02(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)
        # Unimed
        with st.expander(get_via_consulting_project_01(info_requested = 'title', idiom = idiom_idioma)):
            st.write(get_via_consulting_project_01(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)
    
    # BI4ALL
    with st.expander(get_bi4all_info(info_requested = 'title', idiom = idiom_idioma)):
        st.write(get_bi4all_info(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)
        # BI in AWS
        with st.expander(get_bi4all_project_01(info_requested = 'title', idiom = idiom_idioma)):
            st.write(get_bi4all_project_01(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)

    # CLIF
    with st.expander(get_clif_info(info_requested = 'title', idiom = idiom_idioma)):
        st.write(get_clif_info(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)
        # BI in AWS
        with st.expander(get_clif_project_01(info_requested = 'title', idiom = idiom_idioma)):
            st.write(get_clif_project_01(info_requested = 'info', idiom = idiom_idioma), unsafe_allow_html = True)


elif selected == options[3]:
    st.header(education_educacao)
    st.write(get_education_info(idiom = idiom_idioma), unsafe_allow_html = True)

elif selected == options[4]:
    st.subheader(education_educacao_ref)
    
    col1, col2 = st.columns([0.2,2], vertical_alignment = 'center', gap = 'small')
    with col1:
        st.markdown('#### 📱')
        st.markdown('#### :mailbox_with_mail:')
    
    with col2:
        st.subheader('+ 55 (47) 9 9677-2099')
        st.subheader('brmarcelo.peres@gmail.com')
    
    col1, col2 = st.columns([0.2,2], vertical_alignment = 'center')
    with col1:
        st.image(get_mp_git(), width = 30)
        st.image(get_mp_linkedin(), width = 30)
    
    with col2:
        # st.markdown('##### https://github.com/Marcelo-Peres')
        url_repo = 'https://github.com/Marcelo-Peres?tab=repositories'
        url_linkedin = 'https://www.linkedin.com/in/marcelo-peres-de/'
        if origem_selected == 'Português BR':
            st.link_button('Acesse meus Projetos!', url_repo, width = 400)
            st.link_button('Acesse meu Perfil!', url_linkedin, width = 400)
        else:
            st.link_button('Go to my Projects!', url_repo, width = 400)
            st.link_button('Go to my Profile!', url_linkedin, width = 400)
    
elif selected == options[5]:
    if origem_selected == 'English US':
        
        try:
            load_data_resume_us_for_pdf()
        except:
            pass
        
        pdf_path = 'static/Marcelo_Peres_EN_Resume.pdf'
        
        with open(pdf_path, 'rb') as f:
            st.download_button(
                label = '⬇️ Download this Resume in PDF',
                data = f,
                file_name = 'Marcelo_Peres_EN_Resume.pdf',
                mime = 'application/pdf'
            )

        pdf_viewer(pdf_path, height = 1000, width = 700)

        # Custom Resume
        # try:
        #     load_data_resume_us_custom_for_pdf()
        # except:
        #     pass
        
        # pdf_path = 'static/Marcelo_Peres_EN_US_Resume.pdf'
        
        # with open(pdf_path, 'rb') as f:
        #     st.download_button(
        #         label = '⬇️ Download this Resume in PDF',
        #         data = f,
        #         file_name = 'Marcelo_Peres_EN_US_Resume.pdf',
        #         mime = 'application/pdf'
        #     )

        # pdf_viewer(pdf_path, height = 1000, width = 700)

    elif origem_selected == 'Português BR':
        try:
            load_data_resume_for_pdf()
        except:
            pass
        
        pdf_path = 'static/Marcelo_Peres_CV.pdf'
        
        with open(pdf_path, 'rb') as f:
            st.download_button(
                label = '⬇️ Download this Resume in PDF',
                data = f,
                file_name = 'Marcelo_Peres_CV.pdf',
                mime = 'application/pdf'
            )

        pdf_viewer(pdf_path, height = 1000, width = 700)
