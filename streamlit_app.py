st.title("학교 시간표 프로그램")
st.write("아래에서 시간표를 입력하고, 저장된 시간표를 확인하세요.")
days = ["월", "화", "수", "목", "금"]
st.write("## 저장된 시간표")
import streamlit as st
import streamlit.components.v1 as components
import os

# NanumGothic-Regular.ttf 폰트 적용을 위한 CSS 삽입
font_path = os.path.join("fonts", "NanumGothic-Regular.ttf")
font_css = f"""
<style>
@font-face {{
    font-family: 'NanumGothic';
    src: url('{font_path}') format('truetype');
    font-weight: normal;
    font-style: normal;
}}
body, div, input, textarea, table, th, td {{
    font-family: 'NanumGothic', sans-serif !important;
}}
</style>
"""
components.html(font_css, height=0)

st.title("학교 시간표 프로그램")
st.write("아래에서 시간표를 입력하고, 저장된 시간표를 확인하세요.")

days = ["월", "화", "수", "목", "금"]
periods = [f"{i+1}교시" for i in range(7)]

if "timetable" not in st.session_state:
    st.session_state["timetable"] = {day: ["" for _ in periods] for day in days}

with st.form("timetable_form"):
    st.write("시간표 입력")
    timetable_input = {}
    for day in days:
        timetable_input[day] = []
        st.write(f"### {day}")
        cols = st.columns(len(periods))
        for i, col in enumerate(cols):
            subject = col.text_input(f"{day} {periods[i]}", value=st.session_state["timetable"][day][i], key=f"{day}_{i}")
            timetable_input[day].append(subject)
    submitted = st.form_submit_button("저장하기")
    if submitted:
        st.session_state["timetable"] = timetable_input
        st.success("시간표가 저장되었습니다!")

st.write("## 저장된 시간표")
for day in days:
    st.write(f"### {day}")
    st.table({"교시": periods, "과목": st.session_state["timetable"][day]})
