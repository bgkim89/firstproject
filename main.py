import streamlit as st

# 앱 제목
st.title("🎬 MBTI 기반 수학·과학 명작 영화 추천기")
st.markdown("당신의 성격 유형에 꼭 맞는 과학/수학 영화 한 편, 골라드릴게요!")

# MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI 별 추천 영화 데이터
mbti_movies = {
    "INTJ": {
        "title": "인터스텔라",
        "desc": "복잡한 물리 이론과 우주 탐사를 결합한 미래지향적 이야기.",
        "field": "천체물리학, 상대성 이론",
        "youtube": "https://www.youtube.com/watch?v=zSWdZVtXT7E"
    },
    "INTP": {
        "title": "굿 윌 헌팅",
        "desc": "내성적이지만 천재적인 수학 능력을 지닌 청년의 성장 이야기.",
        "field": "수학, 심리학",
        "youtube": "https://www.youtube.com/watch?v=PaZVjZEFkRs"
    },
    "ENTJ": {
        "title": "소셜 네트워크",
        "desc": "논리와 추진력으로 세상을 바꾼 창업자의 전략적 이야기.",
        "field": "IT, 창업, 알고리즘",
        "youtube": "https://www.youtube.com/watch?v=lB95KLmpLR4"
    },
    "ENTP": {
        "title": "인셉션",
        "desc": "창의적인 아이디어와 논리적 세계관이 뒤섞인 꿈의 해석.",
        "field": "신경과학, 인지심리",
        "youtube": "https://www.youtube.com/watch?v=YoHD9XEInc0"
    },
    "INFJ": {
        "title": "콘택트",
        "desc": "외계 생명체와의 접촉 속에서 과학과 철학의 경계를 탐구.",
        "field": "천문학, 철학",
        "youtube": "https://www.youtube.com/watch?v=TRcZavGpt5A"
    },
    "INFP": {
        "title": "어바웃 타임",
        "desc": "시간여행이라는 소재를 통해 삶과 감정을 성찰하는 이야기.",
        "field": "시간 개념, 인생철학",
        "youtube": "https://www.youtube.com/watch?v=T7A810duHvw"
    },
    "ENFJ": {
        "title": "히든 피겨스",
        "desc": "NASA에서 활약한 흑인 여성 수학자들의 감동 실화.",
        "field": "수학, 천문학, 사회정의",
        "youtube": "https://www.youtube.com/watch?v=RK8xHq6dfAo"
    },
    "ENFP": {
        "title": "마션",
        "desc": "화성에 홀로 남겨졌지만 긍정과 창의성으로 과학을 극복하다.",
        "field": "생명과학, 엔지니어링",
        "youtube": "https://www.youtube.com/watch?v=ej3ioOneTy8"
    },
    "ISTJ": {
        "title": "이미테이션 게임",
        "desc": "전쟁 중 기계적 분석과 끈기로 암호를 해독한 실화.",
        "field": "컴퓨터 과학, 논리",
        "youtube": "https://www.youtube.com/watch?v=S5CjKEFb-sM"
    },
    "ISFJ": {
        "title": "히든 피겨스",
        "desc": "묵묵히 헌신한 여성들의 수학적 기여와 팀워크.",
        "field": "수학, 조직 내 기여",
        "youtube": "https://www.youtube.com/watch?v=RK8xHq6dfAo"
    },
    "ESTJ": {
        "title": "체르노빌",
        "desc": "사실과 원칙 중심의 위기 대응과 과학적 진실 파헤치기.",
        "field": "원자력공학, 시스템 분석",
        "youtube": "https://www.youtube.com/watch?v=s9APLXM9Ei8"
    },
    "ESFJ": {
        "title": "빅 히어로",
        "desc": "따뜻한 마음과 과학 기술이 어우러진 힐링 로봇 이야기.",
        "field": "로봇공학, 팀워크",
        "youtube": "https://www.youtube.com/watch?v=z3biFxZIJOQ"
    },
    "ISTP": {
        "title": "그래비티",
        "desc": "냉정한 이성과 기술적 대응으로 생존을 극복하는 이야기.",
        "field": "우주공학, 생존기술",
        "youtube": "https://www.youtube.com/watch?v=OiTiKOy59o4"
    },
    "ISFP": {
        "title": "월-E",
        "desc": "감성과 환경 메시지를 지닌 로봇의 과학적 판타지.",
        "field": "지구과학, 환경공학",
        "youtube": "https://www.youtube.com/watch?v=alIq_wG9FNk"
    },
    "ESTP": {
        "title": "아이언맨",
        "desc": "즉흥적이지만 천재적인 발명가의 액션과 과학 이야기.",
        "field": "기계공학, 에너지",
        "youtube": "https://www.youtube.com/watch?v=8ugaeA-nMTc"
    },
    "ESFP": {
        "title": "백 투 더 퓨처",
        "desc": "유쾌하고 모험적인 성격에 딱 맞는 시간 여행 이야기.",
        "field": "물리학, 시간 개념",
        "youtube": "https://www.youtube.com/watch?v=qvsgGtivCgs"
    }
}

# 사용자 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

# 결과 출력
if selected_mbti:
    movie = mbti_movies[selected_mbti]
    st.subheader(f"🎥 {selected_mbti} 유형을 위한 추천 영화: {movie['title']}")
    st.markdown(f"**관련 분야:** {movie['field']}")
    st.write(movie["desc"])
    st.video(movie["youtube"])
