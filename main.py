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
            "youtube": "https://www.youtube.com/watch?v=0bt8w3c9HgQ",
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
            "youtube": "https://www.youtube.com/watch?v=R2_B27m8L5g",
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
            "youtube": "https://www.youtube.com/watch?v=kTGa2v3s4qw",
            "color": "#FFD700",
            "emoji": "🎤"
        },
        {"title": "No", "artist": "CLC", "year": 2019, "meaning": "타인의 시선에 휘둘리지 않는 자기 확신."},
        {"title": "Fire", "artist": "BTS", "year": 2016, "meaning": "열정적으로 앞으로 나아감."},
        {"title": "Wannabe", "artist": "ITZY", "year": 2020, "meaning": "있는 그대로의 나를 사랑하자."},
        {"title": "Kill This Love", "artist": "BLACKPINK", "year": 2019, "meaning": "단호한 결단력."}
    ],
    "ENTP": [
        {
            "title": "DDU-DU DDU-DU",
            "artist": "BLACKPINK",
            "year": 2018,
            "meaning": "자유롭고 대담한 매력을 과시하는 곡.",
            "reason": "ENTP의 독창적이고 도전적인 에너지를 잘 나타내요.",
            "youtube": "https://www.youtube.com/watch?v=IHNzOHi8sJs",
            "color": "#FF6347",
            "emoji": "💥"
        },
        {"title": "Gee", "artist": "Girls' Generation", "year": 2009, "meaning": "풋풋한 사랑의 설렘과 발랄함."},
        {"title": "I AM", "artist": "IVE", "year": 2023, "meaning": "자신감 넘치는 자기 선언."},
        {"title": "Not Today", "artist": "BTS", "year": 2017, "meaning": "포기하지 않는 강한 의지."},
        {"title": "Nxde", "artist": "(G)I-DLE", "year": 2022, "meaning": "사회적 편견에 맞서는 당당함."}
    ],
    "INFP": [
        {
            "title": "Love Poem",
            "artist": "IU",
            "year": 2019,
            "meaning": "상처받은 이들에게 건네는 따뜻한 위로.",
            "reason": "INFP의 깊은 감성과 공감 능력에 잘 어울리는 곡이에요.",
            "youtube": "https://www.youtube.com/watch?v=DokQyNlO17Q",
            "color": "#FFC0CB",
            "emoji": "🌸"
        },
        {"title": "Spring Day", "artist": "BTS", "year": 2017, "meaning": "그리움과 기다림."},
        {"title": "Through the Night", "artist": "IU", "year": 2017, "meaning": "조용히 전하는 사랑."},
        {"title": "Palette", "artist": "IU ft. G-Dragon", "year": 2017, "meaning": "나를 이해하는 성장."},
        {"title": "Lonely", "artist": "Jonghyun", "year": 2017, "meaning": "우울함과 외로움을 담담하게."}
    ],
    "INFJ": [
        {
            "title": "Fake Love",
            "artist": "BTS",
            "year": 2018,
            "meaning": "진실되지 못한 사랑에 대한 고뇌.",
            "reason": "INFJ의 이상주의적이고 복잡한 내면을 표현해요.",
            "youtube": "https://www.youtube.com/watch?v=RPyvK3Wb108",
            "color": "#9370DB",
            "emoji": "💔"
        },
        {"title": "Eight", "artist": "IU ft. SUGA", "year": 2020, "meaning": "청춘의 방황과 성장."},
        {"title": "Home", "artist": "BTS", "year": 2019, "meaning": "안식처를 찾는 마음."},
        {"title": "Butterfly", "artist": "BTS", "year": 2015, "meaning": "불안정한 아름다움."},
        {"title": "Lullaby", "artist": "GOT7", "year": 2018, "meaning": "감미로운 위로."}
    ],
    "ENFJ": [
        {
            "title": "Permission to Dance",
            "artist": "BTS",
            "year": 2021,
            "meaning": "모두가 함께 즐기며 춤출 수 있는 희망의 메시지.",
            "reason": "ENFJ의 따뜻하고 포용적인 리더십을 잘 나타내요.",
            "youtube": "https://www.youtube.com/watch?v=C7MoP_Qf-d0",
            "color": "#87CEEB",
            "emoji": "🕺"
        },
        {"title": "Boy With Luv", "artist": "BTS ft. Halsey", "year": 2019, "meaning": "작은 것에서 행복을 찾는 사랑."},
        {"title": "Pretty U", "artist": "SEVENTEEN", "year": 2016, "meaning": "사랑하는 사람에게 전하는 솔직한 마음."},
        {"title": "Shine", "artist": "PENTAGON", "year": 2018, "meaning": "사랑을 포기하지 않는 긍정적인 메시지."},
        {"title": "Feel Special", "artist": "TWICE", "year": 2019, "meaning": "힘든 순간에도 특별함을 느끼게 해주는 존재."}
    ],
    "ENFP": [
        {
            "title": "Euphoria",
            "artist": "Jungkook (BTS)",
            "year": 2018,
            "meaning": "벅차오르는 행복감과 사랑의 순간.",
            "reason": "ENFP의 활기차고 긍정적인 에너지를 잘 표현해요.",
            "youtube": "https://www.youtube.com/watch?v=kX0vO4vlFgQ",
            "color": "#FFDAB9",
            "emoji": "✨"
        },
        {"title": "IDOL", "artist": "BTS", "year": 2018, "meaning": "진정한 나를 사랑하고 즐기는 자존감."},
        {"title": "Very Nice", "artist": "SEVENTEEN", "year": 2016, "meaning": "행복한 순간의 축제."},
        {"title": "Feel Good (SECRET CODE)", "artist": "fromis_9", "year": 2020, "meaning": "새로운 시작의 설렘."},
        {"title": "Power Up", "artist": "Red Velvet", "year": 2018, "meaning": "상큼하고 활기찬 여름 에너지."}
    ],
    "ISTJ": [
        {
            "title": "Good Day",
            "artist": "IU",
            "year": 2010,
            "meaning": "좋은 날을 기다리며 설렘을 표현하는 곡.",
            "reason": "ISTJ의 꾸준함과 일상 속 소박한 행복을 추구하는 면모와 어울려요.",
            "youtube": "https://www.youtube.com/watch?v=jeJ8v5WfJtQ",
            "color": "#ADD8E6",
            "emoji": "🕰️"
        },
        {"title": "Work", "artist": "ATEEZ", "year": 2023, "meaning": "목표를 향해 끊임없이 노력하는 모습."},
        {"title": "Don't Leave Me", "artist": "BTS", "year": 2018, "meaning": "변치 않는 믿음과 기다림."},
        {"title": "Regular", "artist": "NCT 127", "year": 2018, "meaning": "규칙적인 삶 속에서 특별함을 찾음."},
        {"title": "Some", "artist": "Bolbbalgan4", "year": 2017, "meaning": "썸 타는 관계의 미묘한 긴장감."}
    ],
    "ISFJ": [
        {
            "title": "For You",
            "artist": "BTS",
            "year": 2015,
            "meaning": "멀리 떨어져 있는 사람에게 전하는 따뜻한 마음.",
            "reason": "ISFJ의 배려심 깊고 헌신적인 성격을 잘 보여줘요.",
            "youtube": "https://www.youtube.com/watch?v=A_2b_X1Jb2c",
            "color": "#FFE4B5",
            "emoji": "💖"
        },
        {"title": "Answer: Love Myself", "artist": "BTS", "year": 2018, "meaning": "진정한 나를 사랑하는 과정."},
        {"title": "Hold My Hand", "artist": "IU", "year": 2011, "meaning": "곁에 있어주는 사람에게 보내는 고마움."},
        {"title": "To My Youth", "artist": "BTS", "year": 2020, "meaning": "힘들었던 청춘에게 보내는 위로."},
        {"title": "Miracles in December", "artist": "EXO", "year": 2013, "meaning": "기적 같은 사랑의 순간."}
    ],
    "ESTJ": [
        {
            "title": "ON",
            "artist": "BTS",
            "year": 2020,
            "meaning": "고난과 역경에도 굴하지 않고 나아가는 의지.",
            "reason": "ESTJ의 책임감 강하고 추진력 있는 모습을 잘 표현해요.",
            "youtube": "https://www.youtube.com/watch?v=mPVDGOjBQWI",
            "color": "#FFA07A",
            "emoji": "💪"
        },
        {"title": "Gashina", "artist": "Sunmi", "year": 2017, "meaning": "주체적이고 강렬한 매력."},
        {"title": "Hard Carry", "artist": "GOT7", "year": 2016, "meaning": "어려움을 이겨내는 강한 의지."},
        {"title": "Boomerang", "artist": "Wanna One", "year": 2018, "meaning": "돌아오는 사랑에 대한 자신감."},
        {"title": "Crazy", "artist": "4minute", "year": 2015, "meaning": "자신감 넘치는 파워풀한 에너지."}
    ],
    "ESFJ": [
        {
            "title": "Dynamite",
            "artist": "BTS",
            "year": 2020,
            "meaning": "긍정적인 에너지로 모두에게 행복을 전하는 곡.",
            "reason": "ESFJ의 사교적이고 밝은 성격을 잘 보여줘요.",
            "youtube": "https://www.youtube.com/watch?v=gdZLi9oWNZg",
            "color": "#FFFACD",
            "emoji": "🥳"
        },
        {"title": "Cheer Up", "artist": "TWICE", "year": 2016, "meaning": "친구를 응원하는 밝은 메시지."},
        {"title": "Spring Up", "artist": "ASTRO", "year": 2016, "meaning": "새로운 시작의 설렘과 희망."},
        {"title": "Go Go", "artist": "BTS", "year": 2017, "meaning": "현재를 즐기며 YOLO 라이프를 추구."},
        {"title": "What is Love?", "artist": "TWICE", "year": 2018, "meaning": "사랑에 대한 궁금증과 설렘."}
    ],
    "ISTP": [
        {
            "title": "Danger",
            "artist": "BTS",
            "year": 2014,
            "meaning": "위험하고 예측 불가능한 사랑에 대한 경고.",
            "reason": "ISTP의 독립적이고 현실적인 성향에 어울려요.",
            "youtube": "https://www.youtube.com/watch?v=4wN1R_w7x90",
            "color": "#C0C0C0",
            "emoji": "🚧"
        },
        {"title": "Rough", "artist": "GFRIEND", "year": 2016, "meaning": "어려움을 극복하고 성장하는 과정."},
        {"title": "Blood Sweat & Tears", "artist": "BTS", "year": 2016, "meaning": "유혹에 대한 갈등과 성숙."},
        {"title": "Savage", "artist": "aespa", "year": 2021, "meaning": "강렬하고 독창적인 자기 주장."},
        {"title": "Bad Boy", "artist": "Red Velvet", "year": 2018, "meaning": "위험한 사랑에 대한 매혹."}
    ],
    "ISFP": [
        {
            "title": "Still With You",
            "artist": "Jungkook (BTS)",
            "year": 2020,
            "meaning": "사랑하는 사람과의 영원한 함께함을 소망하는 곡.",
            "reason": "ISFP의 예술적이고 온화한 감성에 잘 맞아요.",
            "youtube": "https://www.youtube.com/watch?v=A8eR2R-sO08",
            "color": "#FAEBD7",
            "emoji": "🌷"
        },
        {"title": "Sweet Night", "artist": "V (BTS)", "year": 2020, "meaning": "따뜻하고 위로를 주는 밤."},
        {"title": "Eight (IU)", "artist": "IU ft. SUGA", "year": 2020, "meaning": "청춘의 방황과 성장 (재추천이지만 의미 있음)."},
        {"title": "Starry Night", "artist": "MAMAMOO", "year": 2018, "meaning": "아름다운 밤하늘처럼 빛나는 사랑."},
        {"title": "Serendipity", "artist": "Jimin (BTS)", "year": 2017, "meaning": "운명적인 만남의 아름다움."}
    ],
    "ESTP": [
        {
            "title": "IDOL",
            "artist": "BTS",
            "year": 2018,
            "meaning": "자신을 사랑하고 즐기는 당당한 모습.",
            "reason": "ESTP의 즉흥적이고 활동적인 면모와 어울려요.",
            "youtube": "https://www.youtube.com/watch?v=pBuZEGYXA6E",
            "color": "#FF4500",
            "emoji": "😎"
        },
        {"title": "Fantastic Baby", "artist": "BIGBANG", "year": 2012, "meaning": "자유롭고 열정적인 분위기."},
        {"title": "Hip", "artist": "MAMAMOO", "year": 2019, "meaning": "자신만의 스타일을 고수하는 당당함."},
        {"title": "Left & Right", "artist": "SEVENTEEN", "year": 2020, "meaning": "긍정적인 에너지로 앞만 보고 나아감."},
        {"title": "Rollin'", "artist": "Brave Girls", "year": 2017, "meaning": "중독성 있는 리듬으로 즐거움을 선사."}
    ],
    "ESFP": [
        {
            "title": "Boy With Luv",
            "artist": "BTS ft. Halsey",
            "year": 2019,
            "meaning": "사랑으로 인해 작은 것들도 특별해지는 순간.",
            "reason": "ESFP의 낙천적이고 유쾌한 성격에 잘 맞아요.",
            "youtube": "https://www.youtube.com/watch?v=XsX3g3yCdkE",
            "color": "#FFB6C1",
            "emoji": "😊"
        },
        {"title": "Red Flavor", "artist": "Red Velvet", "year": 2017, "meaning": "상큼하고 발랄한 여름의 즐거움."},
        {"title": "Dalla Dalla", "artist": "ITZY", "year": 2019, "meaning": "세상의 시선에 아랑곳하지 않는 자기 확신."},
        {"title": "AS IF IT'S YOUR LAST", "artist": "BLACKPINK", "year": 2017, "meaning": "후회 없이 사랑하는 열정적인 마음."},
        {"title": "DDU-DU DDU-DU (BLACKPINK)", "artist": "BLACKPINK", "year": 2018, "meaning": "자신감 넘치는 매력 발산 (재추천)."}
    ],
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
        bg_color = top_song.get("color", "#FFF0F5")  # 기본 배경색 설정
        emoji = top_song.get("emoji", "🎶")  # 기본 이모지 설정

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
