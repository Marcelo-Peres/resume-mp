import streamlit as st
import pandas as pd
import json, ast

st.title('PostgreSQL Data Viewer')

# Establish connection using Streamlit's connection API
conn = st.connection('postgresql', type='sql')

# Define your SQL query
query = 'select * from ccm_cg.vw_ctcg06_app'

# Execute the query and load data into a Pandas DataFrame
try:
    df = conn.query(query, ttl='10m') # Cache for 10 minutes
    df['ref_item_z07'] = df.ref_item_z07.apply(lambda x: json.dumps(x, indent = 2, ensure_ascii = False))
    df['ref_item_601'] = df.ref_item_601.apply(lambda x: json.dumps(x, indent = 2, ensure_ascii = False))
    
    lines = df.shape[0]
    columns = df.shape[1]

    grp = ( df.groupby('ano_mes').agg(
            quantidade = ('hash_id', 'size'),
            total = ('valor_z07', 'sum'))
        .reset_index())

    grp['total'] = (    grp.total.map('$ {:,.2f}'.format)
                        .str.replace('.', '#')
                        .str.replace(',', '.')
                        .str.replace('#', ',')
    )

    st.success('Data loaded successfully!')
    st.text(f'Total de {lines} linha(s) e {columns} coluna(s) carregada(s)!')
    st.dataframe(df) # Display the DataFrame in Streamlit
    st.dataframe(grp) # Display the DataFrame in Streamlit
except Exception as e:
    st.error(f'Error connecting to database or fetching data: {e}')