import streamlit as st

st.title("학과별 시간표 프로그램")
st.write("학과를 선택하고, 시간표를 입력 및 저장하세요.")

departments = ["국어과", "수학과", "영어과", "과학과", "사회과"]
days = ["월", "화", "수", "목", "금"]
periods = [f"{i+1}교시" for i in range(7)]

selected_dept = st.selectbox("학과 선택", departments)

if "dept_timetable" not in st.session_state:
	st.session_state["dept_timetable"] = {dept: {day: ["" for _ in periods] for day in days} for dept in departments}

with st.form("dept_timetable_form"):
	st.write(f"{selected_dept} 시간표 입력")
	timetable_input = {}
	for day in days:
		timetable_input[day] = []
		st.write(f"### {day}")
		cols = st.columns(len(periods))
		for i, col in enumerate(cols):
			subject = col.text_input(f"{day} {periods[i]}", value=st.session_state["dept_timetable"][selected_dept][day][i], key=f"{selected_dept}_{day}_{i}")
			timetable_input[day].append(subject)
	submitted = st.form_submit_button("저장하기")
	if submitted:
		st.session_state["dept_timetable"][selected_dept] = timetable_input
		st.success(f"{selected_dept} 시간표가 저장되었습니다!")

st.write(f"## {selected_dept} 저장된 시간표")
for day in days:
	st.write(f"### {day}")
	st.table({"교시": periods, "과목": st.session_state["dept_timetable"][selected_dept][day]})
