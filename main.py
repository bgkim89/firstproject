import streamlit as st
import random

# ----------------------
# 1. 설정
# ----------------------
st.set_page_config(page_title="MBTI 기반 K-pop 추천기", layout="centered")

# ----------------------
# 2. 데이터: MBTI별 K-pop 추천곡
# ----------------------
kpop_recommendations = {
    "INFP": [
        {
            "title": "Love Poem",
            "artist": "아이유 (IU)",
            "year": 2019,
            "meaning": "아픔 속 누군가에게 따뜻한 위로가 되고 싶은 마음을 담은 곡.",
            "youtube": "https://www.youtube.com/watch?v=0-q1KafFCLU",
            "color": "#FFDEE9"  # 연핑크
        },
        {
            "title": "Spring Day",
            "artist": "방탄소년단 (BTS)",
            "year": 2017,
            "meaning": "그리움과 기다림을 표현한 따뜻한 감성의 명곡."
        },
        {
            "title": "Palette",
            "artist": "아이유 (feat. G-DRAGON)",
            "year": 2017,
            "meaning": "성장하면서 자아를 찾아가는 과정을 담담하게 그린 노래."
        },
        {
            "title": "8",
            "artist": "아이유 & SUGA",
            "year": 2020,
            "meaning": "잃어버린 소중한 기억에 대한 회상을 전하는 감성적인 곡."
        },
        {
            "title": "Lonely",
            "artist": "종현 (Jonghyun)",
            "year": 2017,
            "meaning": "외로움에 대한 깊은 공감과 이해를 노래한 곡."
        }
    ],
    # 필요한 경우 다른 MBTI 유형도 추가 가능
}

# ----------------------
# 3. UI
# ----------------------
st.markdown("<h1 style='text-align:center;'>🎀 MBTI로 알아보는 당신의 K-pop 💖</h1>", unsafe_allow_html=True)

mbti_types = list(kpop_recommendations.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요", mbti_types)

start_year, end_year = st.slider(
    "🎧 추천받고 싶은 노래의 연도 범위를 선택하세요",
    min_value=2005,
    max_value=2025,
    value=(2015, 2023)
)

# ----------------------
# 4. 추천 결과
# ----------------------
if selected_mbti:
    songs = kpop_recommendations[selected_mbti]
    filtered_songs = [s for s in songs if start_year <= s["year"] <= end_year]

    if not filtered_songs:
        st.error("😢 해당 연도에 추천할 곡이 없어요. 연도를 조정해 주세요!")
    else:
        # 배경 색상 적용
        theme_color = filtered_songs[0].get("color", "#FFC0CB")  # 기본 연핑크
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

        st.subheader(f"🌟 {selected_mbti} 유형에게 어울리는 K-pop Top 5!")
        for i, song in enumerate(filtered_songs[:5]):
            st.markdown(f"### {i+1}. {song['artist']} - *{song['title']}* ({song['year']})")
            st.markdown(f"💬 _{song['meaning']}_")
            if i == 0 and "youtube" in song:
                st.video(song["youtube"])
