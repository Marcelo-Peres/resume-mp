# ------ Personal Resume App (Advanced with placeholders) ------
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from markdown_pdf import MarkdownPdf, Section
from streamlit_option_menu import option_menu
from make_resume_in_pdf import load_data_for_pdf
from plotly import graph_objects as go

from about.content import get_about_introduction
from img.img import get_mp_img, get_mp_git, get_mp_linkedin
from skills.content import get_skills_info

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

from education.content import get_education_info

# Sidebar for navigation

with st.sidebar:
    selected = option_menu(
        menu_title = 'Navigation',
        options = ['About', 'Skills', 'Experience', 'Education', 'Contact', 'Resume'],
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
st.subheader('Big Data Engineer')

if selected == 'About':
    st.image(get_mp_img(), width = 400)
    st.write('\n', unsafe_allow_html = True)
    st.write(get_about_introduction('p1'), unsafe_allow_html = True)
    st.write('\n', unsafe_allow_html = True)
    st.write(get_about_introduction('p2'), unsafe_allow_html = True)
    st.write('\n', unsafe_allow_html = True)
    st.write(get_about_introduction('p3'), unsafe_allow_html = True)
    st.write('\n', unsafe_allow_html = True)
    st.write(get_about_introduction('p4'), unsafe_allow_html = True)
    st.write('\n', unsafe_allow_html = True)
    st.write(get_about_introduction('p5'), unsafe_allow_html = True)

elif selected == 'Skills':
    # Title
    center_ini = '''<h1 style='text-align: center;'>'''
    center_end = '</h1>'
    title_info = 'Skills Overview'
    st.markdown(
    "<h1 style='text-align: center;'> 🔎 Skills Overview </h1>",
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

elif selected == 'Experience':
    st.header('Work Experience')
    
    st.subheader('Current Job')
    # Aplos
    with st.expander(get_apllos_info('title')):
        st.write(get_apllos_info('info'), unsafe_allow_html = True)
        # Audlab Project
        with st.expander(get_apllos_current_project('title')):
            st.write(get_apllos_current_project('info'), unsafe_allow_html = True)
        # Gab Project
        with st.expander(get_apllos_gab_project('title')):
            st.write(get_apllos_gab_project('info'), unsafe_allow_html = True)
        # Audlab Project
        with st.expander(get_apllos_audlab_project('title')):
            st.write(get_apllos_audlab_project('info'), unsafe_allow_html = True)

    st.subheader('Previous Jobs')
    with st.expander(get_a3data_info('title')):
        st.write(get_a3data_info('info'), unsafe_allow_html = True)
        # Stellantis #
        with st.expander(get_a3data_stellantis_project('title')):
            st.write(get_a3data_stellantis_project('info'), unsafe_allow_html = True)
    
    # Via Consulting 
    with st.expander(get_via_consulting_info('title')):
        st.write(get_via_consulting_info('info'), unsafe_allow_html = True)
        # Gol Project
        with st.expander(get_via_consulting_gol_project('title')):
            st.write(get_via_consulting_gol_project('info'), unsafe_allow_html = True)
        # Zendesk'
        with st.expander(get_via_consulting_zendesk_project('title')):
            st.write(get_via_consulting_zendesk_project('info'), unsafe_allow_html = True)
        # Unimed
        with st.expander(get_via_consulting_unimed_project('title')):
            st.write(get_via_consulting_unimed_project('info'), unsafe_allow_html = True)
    
    # BI4ALL
    with st.expander(get_bi4all_info('title')):
        st.write(get_bi4all_info('info'), unsafe_allow_html = True)
        # BI in AWS
        with st.expander(get_bi4all_bi_project('title')):
            st.write(get_bi4all_bi_project('info'), unsafe_allow_html = True)

    # CLIF
    with st.expander(get_clif_info('title')):
        st.write(get_clif_info('info'), unsafe_allow_html = True)
        # BI in AWS
        with st.expander(get_clif_project('title')):
            st.write(get_clif_project('info'), unsafe_allow_html = True)


elif selected == 'Education':
    st.header('Education')
    st.write(get_education_info())

elif selected == 'Contact':
    st.subheader('<< Get in Touch >>')
    
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
        st.link_button('Go to my Projects!', url_repo, width = 400)
        st.link_button('Go to my Profile!', url_linkedin, width = 400)
    
elif selected == 'Resume':
    try:
        load_data_for_pdf()
    except:
        pass
    
    pdf_path = 'static/Marcelo_Peres_Resume.pdf'
    
    with open(pdf_path, 'rb') as f:
        st.download_button(
            label = '⬇️ Download this Resume in PDF',
            data = f,
            file_name = 'Marcelo_Peres_Resume.pdf',
            mime = 'application/pdf'
        )
    
    pdf_viewer(pdf_path, height = 1000, width = 700)
