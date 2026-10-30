"""9주차 과제: 수업에서 배운 Streamlit 기본 예제.

실행: python -m streamlit run streamlit_app.py
"""

import streamlit as st
import pandas as pd
import numpy as np


# 1. 웹 화면에 제목과 설명을 표시한다.
st.title("간단한 Streamlit 예제")
st.write("데이터와 그래프를 보여주는 예제입니다.")

# 2. 수업 예제와 같이 20행 3열의 무작위 데이터를 만든다.
#    A, B, C는 실제 통계 자료가 아닌 연습용 데이터이다.
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"],
)

# 3. 각 열의 값을 선 그래프로 표시한다.
st.line_chart(data)
