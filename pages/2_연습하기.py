import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib as plt
st.title("2.연습하기")
#팽귄데이터 불러와서 산점도만들기
penguins = sns.load_dataset("penguins")
st.write(penguins)

#seaborn 으로 산점도
sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=penguins)
st.pyplot(plt.gcf())

