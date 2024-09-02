#Import des modules
import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



#Titre et preheader
st.title('Bienvenu(e) sur le site web de Amal')


#import de données
choix_dataframe = st.selectbox("choisis un dataset", sns.get_dataset_names())
data = sns.load_dataset(choix_dataframe)

st.write(data)


axe_x = st.selectbox("choisis la colonne x", data.columns)

axe_y = st.selectbox("choisis la colonne y", data.columns)


graphique = st.selectbox("choisis le type de graphique", ["bar_chart","scatter_chart","line_chart","area_chart"])


if graphique=="bar_chart":
    st.bar_chart(data,x=axe_x,y=axe_y)
    
if graphique=="scatter_chart":
    st.scatter_chart(data,x=axe_x,y=axe_y)
    
if graphique=="line_chart":
    st.line_chart(data,x=axe_x,y=axe_y)
    
if graphique=="area_chart"  :
    st.area_chart(data,x=axe_x,y=axe_y)

matrice_corr=st.checkbox("Afficher la matrice de corrélation")

if matrice_corr:
    sns.heatmap(data.select_dtypes(include=["number"]).corr())
    st.pyplot(plt.gcf())