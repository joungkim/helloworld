import numpy as np
import altair as alt  #차트 만듦
import pandas as pd
import streamlit as st

st.header("st.write")

#예제1
st.write("Hello, * WOrld!* : sunglasses")

#예제2
st.write(1234)

#예제3
df = pd.DataFrame({
    "첫 번째 컬럼":[1,2,3,4],
    "두 번째 컬럼":[10,20,30,40]
})
st.write(df)

#예제4
st.write("아래는 DataFrame입니다.",df,"위는 dateframe입니다.")

#예제5
df2 = pd.DataFrame(
    np.random.randn(200,3),   #200행, 3열
    columns=['a','b','c']
)
c = alt.Chart(df2).mark_circle().encode(    #mark_circle() 원 형태의 마커 사용해 산점도
    #encode() 함수를 사용하여 각 마커의 속성을 지정함.
    x = 'a',y = 'b',size='c', color = 'c', tooltip=['a','b','c']
    #c는 마커의 크기와 색성을 지정함
    #tooltip은 마우스를 올렸을 때 해당 값들이 표시되도록 함.
)
st.write(c)