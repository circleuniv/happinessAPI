import streamlit as st
import pandas as pd
import plotly.express as px

def draw_figure(content,x_select,y_select):
    #x_label=st.session_state['x-set'].lower()
    x_label=x_select.lower()
    x_data=content[x_label].tolist()

    #y_label=st.session_state['y-set'].lower()
    y_label = y_select.lower()
    y_data = content[y_label].tolist()

    figure=px.scatter(x=x_data,y=y_data,labels={'x':x_select,'y':y_select})
    return figure

st.title('In Search for Happiness')
content=pd.read_csv('happy.csv')
chooses=content.columns.tolist()[1:]
chooses=[x.title() for x in chooses]

x_select=st.selectbox(label='Select the data for the X-axis',
                          options=chooses)
y_select=st.selectbox(label='Select the data for the Y-axis',
                          options=chooses)
st.subheader(f'{x_select} and {y_select}')

chart=st.plotly_chart(draw_figure(content,x_select,y_select))
