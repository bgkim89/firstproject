import streamlit as st
import json

# 데이터 로드
with open("kpop_mbti_recommendations.json", "r", encoding="utf-8") as f:
    kpop_recommendations = json.load(f)

# 페이지 설정
st.set_page_config(page_title="MBTI 기반 K-pop 추천기", layout="centered")

# 제목
st.markdown("<h1 style='text-align:center;'>\U0001F496 MBTI로 알아보는 당신의 K-pop 추천 \U0001F496</h1>", unsafe_allow_html=True)

# MBTI 선택
mbti_types = list(kpop_recommendations.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요:", mbti_types)

# 연도 범위 선택
start_year, end_year = st.slider(
    "🎧 추천받고 싶은 노래의 연도 범위를 선택하세요",
    min_value=2005,
    max_value=2025,
    value=(2015, 2023)
)

# 추천곡 필터링 및 출력
if selected_mbti:
    songs = kpop_recommendations.get(selected_mbti, [])
    filtered_songs = [s for s in songs if start_year <= s["year"] <= end_year]

    if not filtered_songs:
        st.error("😢 해당 연도에 추천할 곡이 없어요. 연도를 조정해 주세요!")
    else:
        # 배경색 적용
        theme_color = filtered_songs[0].get("color", "#FFC0CB")
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-color: {theme_color};
                font-family: 'Nanum Gothic', sans-serif;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        # 추천 결과 출력
        st.subheader(f"\U0001F31F {selected_mbti} 유형에게 어울리는 K-pop Top 5!")
        for i, song in enumerate(filtered_songs[:5]):
            st.markdown(f"### {i+1}. {song['artist']} - *{song['title']}* ({song['year']})")
            st.markdown(f"💬 _{song['meaning']}_")
            if i == 0:
                if "reason" in song:
                    st.info(f"\U0001F4D6 1순위 이유: {song['reason']}")
                if "youtube" in song:
                    st.video(song["youtube"])
