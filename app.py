import streamlit as st

st.title("10주차 스트림릿 연습")
st.info('안녕하세요, 소개페이지')
st.error('에러창인데 빨간 박스')
st.success('성공창인데 초록박스')
st.warning('경고창인데 노란 박스')
st.header('메인페이지')
st.subheader('그다음 중제목')
st.write('모든 내용 다 쓰기 가능')
st.markdown('이것은 **텍스트** 쓰기')
st.latex("ax^2+bx+c=0")
st.code("print('hello teachers')")
st.write("---")

st.image("image1.jpg",width=200)
st.image("https://th.bing.com/th/id/OIP.yqlsA1zExCrzvjn9pOIwHwHaJ9?w=131&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3")
st.video("https://youtu.be/dwsL-knwfQM?si=aUauxPD9HPKSeUIt")

st.link_button("데스모스 행렬 계산기 바로가기","https://www.desmos.com/matrix?lang=ko")
st.components.v1.iframe("https://www.desmos.com/matrix?lang=ko",
                        height=500)

