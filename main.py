import streamlit as st

# MBTI별 영화 추천 딕셔너리
mbti_movies = {
    'INTJ': {
        'title': '인터스텔라',
        'desc': '전략적 사고와 깊은 이론물리학이 결합된 우주 탐사 이야기.',
        'field': '이론 물리학',
        'youtube': 'https://www.youtube.com/watch?v=zSWdZVtXT7E'
    },
    'INTP': {
        'title': '굿 윌 헌팅',
        'desc': '천재적인 수학 능력을 가진 청년의 감정적 성장과 탐구.',
        'field': '수학',
        'youtube': 'https://www.youtube.com/watch?v=PaZVjZEFkRs'
    },
    'ENFP': {
        'title': '마션',
        'desc': '유쾌하고 낙천적인 태도로 화성에서 생존하는 과학자.',
        'field': '생명과학, 화학, 엔지니어링',
        'youtube': 'https://www.youtube.com/watch?v=ej3ioOneTy8'
    },
    # ... 다른 유형도 추가 가능
}

# 제목
st.title("🎬 MBTI 기반 수학/과학 영화 추천기")

# MBTI 입력 받기
mbti = st.selectbox("당신의 MBTI는 무엇인가요?", list(mbti_movies.keys()))

# 추천 결과 출력
if mbti:
    movie = mbti_movies[mbti]
    st.subheader(f"📽 추천 영화: {movie['title']}")
    st.markdown(f"**분야:** {movie['field']}")
    st.write(movie['desc'])
    st.video(movie['youtube'])
