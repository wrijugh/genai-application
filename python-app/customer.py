import streamlit as st
import customerlib as cl

st.title('Customer Information - v2')

st.write('Enter your customer infomation below:')

organizationName = st.text_input('Organization Name')

if st.button('Ask me about the Organization'):
    response = cl.get_org_details(organizationName)
    st.write(response)