import streamlit as st

# ----------------------
# 1. 데이터 정의 (MBTI별 추천곡 5개, 1순위에 유튜브/색상/이모지 포함)
# ----------------------
kpop_data = {
    "INTJ": [
        {
            "title": "Black Swan",
            "artist": "BTS",
            "year": 2020,
            "meaning": "예술가의 공허함과 자아 탐구를 표현한 곡.",
            "reason": "INTJ의 깊은 내면과 예술적 통찰에 잘 어울려요.",
            "youtube": "https://www.youtube.com/watch?v=0lapF4DQPKQ",
            "color": "#A9A9F5",
            "emoji": "🦢"
        },
        {"title": "Odd Eye", "artist": "Dreamcatcher", "year": 2021, "meaning": "현실과 이상 사이의 진실 탐구."},
        {"title": "Eclipse", "artist": "Moonbyul", "year": 2020, "meaning": "자기 안의 그림자와 마주함."},
        {"title": "Déjà-Boo", "artist": "Jonghyun ft. Zion.T", "year": 2015, "meaning": "반복되는 감정 속에서 느끼는 익숙함."},
        {"title": "Beautiful Liar", "artist": "VIXX LR", "year": 2015, "meaning": "자신을 숨기는 슬픔."}
    ],
    "INTP": [
        {
            "title": "Blue & Grey",
            "artist": "BTS",
            "year": 2020,
            "meaning": "우울함과 외로움을 섬세하게 표현한 곡.",
            "reason": "INTP의 고요한 내면세계를 잘 표현해요.",
            "youtube": "https://www.youtube.com/watch?v=lgpPmy8Zqy4",
            "color": "#B0E0E6",
            "emoji": "🌫️"
        },
        {"title": "Moon", "artist": "Jin (BTS)", "year": 2020, "meaning": "지켜주는 존재의 헌신."},
        {"title": "Sorry", "artist": "The Rose", "year": 2018, "meaning": "감성적인 사과와 후회."},
        {"title": "I’m Fine", "artist": "BTS", "year": 2018, "meaning": "괜찮은 척하는 마음."},
        {"title": "MAGO", "artist": "GFRIEND", "year": 2020, "meaning": "자기 확신과 당당함."}
    ],
    "ENTJ": [
        {
            "title": "MIC Drop",
            "artist": "BTS",
            "year": 2017,
            "meaning": "자신감과 리더십의 상징적인 곡.",
            "reason": "ENTJ의 카리스마와 목표지향적 성격을 대변해요.",
            "youtube": "https://www.youtube.com/watch?v=kTlv5_Bs8aw",
            "color": "#FFD700",
            "emoji": "🎤"
        },
        {"title": "No", "artist": "CLC", "year": 2019, "meaning": "타인의 시선에 휘둘리지 않는 자기 확신."},
        {"title": "Fire", "artist": "BTS", "year": 2016, "meaning": "열정적으로 앞으로 나아감."},
        {"title": "Wannabe", "artist": "ITZY", "year": 2020, "meaning": "있는 그대로의 나를 사랑하자."},
        {"title": "Kill This Love", "artist": "BLACKPINK", "year": 2019, "meaning": "단호한 결단력."}
    ],
    "INFP": [
        {
            "title": "Love Poem",
            "artist": "IU",
            "year": 2019,
            "meaning": "상처받은 이들에게 건네는 따뜻한 위로.",
            "reason": "INFP의 깊은 감성과 공감 능력에 잘 어울리는 곡이에요.",
            "youtube": "https://www.youtube.com/watch?v=N_q8N-m9fVU",
            "color": "#FFC0CB",
            "emoji": "🌸"
        },
        {"title": "Spring Day", "artist": "BTS", "year": 2017, "meaning": "그리움과 기다림."},
        {"title": "Through the Night", "artist": "IU", "year": 2017, "meaning": "조용히 전하는 사랑."},
        {"title": "Palette", "artist": "IU ft. G-Dragon", "year": 2017, "meaning": "나를 이해하는 성장."},
        {"title": "Lonely", "artist": "Jonghyun", "year": 2017, "meaning": "우울함과 외로움을 담담하게."}
    ],
    # 나머지 MBTI (ENFP, INFJ, ENFJ, ISTJ, etc)도 동일한 방식으로 여기에 추가 가능
}

mbti_list = list(kpop_data.keys())

# ----------------------
# 2. Streamlit App UI
# ----------------------
st.set_page_config(page_title="MBTI 기반 K-pop 추천기", layout="centered")

st.markdown("<h1 style='text-align:center;'>💖 MBTI로 알아보는 K-pop 추천 💿</h1>", unsafe_allow_html=True)

selected_mbti = st.selectbox("🧠 MBTI를 선택하세요", mbti_list)
start_year, end_year = st.slider("📅 연도 범위를 설정하세요", 2000, 2025, (2015, 2023))

if selected_mbti:
    songs = kpop_data[selected_mbti]
    filtered = [s for s in songs if start_year <= s["year"] <= end_year]

    if not filtered:
        st.warning("😢 해당 연도 범위에 맞는 곡이 없어요.")
    else:
        top_song = filtered[0]
        bg_color = top_song.get("color", "#FFF0F5")
        emoji = top_song.get("emoji", "🎶")

        st.markdown(f"""
            <style>
                .stApp {{
                    background-color: {bg_color};
                    font-family: 'Nanum Gothic', sans-serif;
                }}
            </style>
        """, unsafe_allow_html=True)

        st.markdown(f"<h2>{emoji} {selected_mbti} 유형을 위한 K-pop 추천</h2>", unsafe_allow_html=True)

        for i, song in enumerate(filtered[:5]):
            st.markdown(f"### {i+1}. {song['artist']} - *{song['title']}* ({song['year']})")
            st.markdown(f"🎵 **가사 의미**: _{song['meaning']}_")
            if i == 0:
                if "reason" in song:
                    st.markdown(f"💡 **추천 이유**: _{song['reason']}_")
                if "youtube" in song:
                    st.video(song["youtube"])
