import json

# 데이터 예시: 16개의 MBTI별 K-pop 추천곡 5개씩, 1순위는 유튜브 링크와 배경색, 추천 이유 포함

kpop_recommendations = {
    "INTJ": [
        {
            "title": "Black Swan",
            "artist": "BTS",
            "year": 2020,
            "meaning": "내면의 공허함과 예술가로서의 정체성에 대한 고민을 담은 곡.",
            "youtube": "https://www.youtube.com/watch?v=0lapF4DQPKQ",
            "color": "#B0C4DE",
            "reason": "INTJ의 깊은 자기 성찰과 예술적 감수성에 가장 어울리는 곡이기 때문입니다."
        },
        {
            "title": "Odd Eye",
            "artist": "Dreamcatcher",
            "year": 2021,
            "meaning": "이상향을 향한 갈망과 현실의 충돌을 표현한 곡."
        },
        {
            "title": "Eclipse",
            "artist": "Moonbyul",
            "year": 2020,
            "meaning": "어둠 속에서 진짜 자아를 찾는 여정을 그린 곡."
        },
        {
            "title": "Déjà-Boo",
            "artist": "Jonghyun & Zion.T",
            "year": 2015,
            "meaning": "감각적인 분위기 속에 숨겨진 반복되는 감정의 패턴."
        },
        {
            "title": "Beautiful Liar",
            "artist": "VIXX LR",
            "year": 2015,
            "meaning": "자신의 진심을 숨기려는 이중적인 감정을 담은 곡."
        }
    ],
    "INTP": [
        {
            "title": "Blue & Grey",
            "artist": "BTS",
            "year": 2020,
            "meaning": "감정의 무채색 풍경을 섬세하게 표현한 곡.",
            "youtube": "https://www.youtube.com/watch?v=lgpPmy8Zqy4",
            "color": "#AFCBFF",
            "reason": "INTP의 내면에 존재하는 슬픔과 철학적 고뇌를 정제된 언어로 표현한 곡이기 때문입니다."
        },
        {
            "title": "Moon",
            "artist": "Jin (BTS)",
            "year": 2020,
            "meaning": "세상을 바라보는 독특한 시선과 헌신의 아름다움."
        },
        {
            "title": "MAGO",
            "artist": "GFRIEND",
            "year": 2020,
            "meaning": "자기 확신과 개성에 대한 당당한 표현."
        },
        {
            "title": "Sorry",
            "artist": "The Rose",
            "year": 2018,
            "meaning": "감정을 숨기지 않고 전하는 아날로그 감성의 고백."
        },
        {
            "title": "I’m Fine",
            "artist": "BTS",
            "year": 2018,
            "meaning": "겉으로는 괜찮은 척하면서도 내면의 혼란을 느끼는 감정선."
        }
    ],
    # 생략된 나머지 14개의 MBTI 데이터를 계속 추가하는 방식입니다...
}

# 저장
file_path = "/mnt/data/kpop_mbti_recommendations.json"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(kpop_recommendations, f, ensure_ascii=False, indent=2)

file_path
