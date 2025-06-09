import streamlit as st
import json

# ----------------------
# 1. 설정
# ----------------------
st.set_page_config(page_title="MBTI 기반 K-pop 추천기", layout="centered")

# ----------------------
# 2. JSON 데이터 불러오기
# ----------------------
@st.cache_data
def load_recommendations():
    with open("kpop_mbti_recommendations.json", "r", encoding="utf-8") as f:
        return json.load(f)

kpop_recommendations = load_recommendations()
mbti_types = list(kpop_recommendations.keys())

# ----------------------
# 3. UI: 선택
# ----------------------
st.markdown("<h1 style='text-align:center;'>🌸 MBTI로 알아보는 당신의 K-pop 🎶</h1>", unsafe_allow_html=True)

selected_mbti = st.selectbox("🧠 당신의 MBTI를 선택하세요", mbti_types)

start_year, end_year = st.slider(
    "📅 추천받고 싶은 노래의 연도 범위를 선택하세요",
    min_value=2005,
    max_value=2025,
    value=(2015, 2023)
)

# ----------------------
# 4. 추천 결과 출력
# ----------------------
if selected_mbti:
    songs = kpop_recommendations[selected_mbti]
    filtered_songs = [s for s in songs if start_year <= s["year"] <= end_year]

    if not filtered_songs:
        st.error("😢 해당 연도에 추천할 곡이 없어요. 연도를 바꿔보세요!")
    else:
        first_song = filtered_songs[0]
        theme_color = first_song.get("color", "#FFC0CB")  # 기본 연핑크

        # 배경색 설정
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

        st.subheader(f"🎧 {selected_mbti} 유형에게 어울리는 K-pop Top 5")

        for i, song in enumerate(filtered_songs[:5]):
            st.markdown(f"### {i+1}. {song['artist']} - *{song['title']}* ({song['year']})")
            st.markdown(f"💬 **의미**: _{song['meaning']}_")

            if i == 0:
                if "reason" in song:
                    st.markdown(f"🎯 **추천 이유**: _{song['reason']}_")
                if "youtube" in song:
                    st.video(song["youtube"])
