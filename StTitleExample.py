from ApiInformationLoadImage import st_title
import streamlit as st
st_title()
style = """
       <style>.css-k0sv6k { height: 1.875rem;}</style>
       """
st.markdown(style, unsafe_allow_html=True)


import streamlit as st

st.title('st.title demo', 'sttitle')
for i in range(1, 5):
    st.write('Display text in title formatting')
st.title(body='i am message body', anchor='I_am_anchor')
for j in range(1, 5):
    st.write('st.title(body, anchor) ')
st.markdown('----')

st.markdown('<h1> I am html h1 tag</h1>', unsafe_allow_html=True)
for k in range(1,5):
    st.write('st.title demo')
st.title("st.title is equivalent to html h1 tag")
for l in range(1, 5):
    st.write('hope you understood st.title')

st.markdown('[Top](#sttitle)', unsafe_allow_html=True)
st.markdown('[Jump to I_am_anchor](#I_am_anchor)', unsafe_allow_html=True)
st.markdown('----')
st.title('Thank You')

st.title('Share and Advice')
