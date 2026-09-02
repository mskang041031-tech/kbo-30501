import streamlit as st
import random
import time

# ============================================================
# 1. Streamlit 페이지 기본 설정
# ============================================================

st.set_page_config(
    page_title="🔮 COSMIC KBO PREDICT",
    page_icon="🌌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# 2. 판타지 타이포그래피 & 아방가르드 코스믹 CSS
# ============================================================

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Noto+Sans+KR:wght@400;700;900&display=swap');

    [data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    .stApp {
        background: linear-gradient(135deg, #090014 0%, #15002b 25%, #2a004f 50%, #120033 75%, #03000a 100%) !important;
        background-attachment: fixed !important;
        color: #e6f2ff !important;
        font-family: 'Noto Sans KR', sans-serif;
    }

    .fantasy-title {
        font-family: 'Cinzel Decorative', 'Noto Sans KR', cursive, serif;
        font-size: 3rem !important;
        font-weight: 900;
        text-align: center;
        letter-spacing: 2px;
        background: linear-gradient(180deg, #e1ff75 0%, #00f0ff 45%, #0040ff 85%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(3px 4px 0px #ff007f) drop-shadow(0px 0px 18px rgba(0, 240, 255, 0.8));
        margin-bottom: 0.2rem;
    }

    .fantasy-subtitle {
        text-align: center;
        font-size: 1rem;
        color: #00ffff;
        opacity: 0.85;
        margin-bottom: 2rem;
        letter-spacing: 1px;
    }

    /* 우주의 기운 클릭 스태킹 카드 */
    .energy-card {
        background: rgba(255, 255, 255, 0.05);
        border: 2px dashed rgba(255, 0, 127, 0.6);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 0 20px rgba(138, 43, 226, 0.4);
    }

    .energy-level-title {
        font-family: 'Cinzel Decorative', 'Noto Sans KR', sans-serif;
        font-size: 1.8rem;
        font-weight: 900;
        color: #ff007f;
        text-shadow: 0 0 10px #ff007f, 0 0 20px #00ffff;
        margin-bottom: 0.5rem;
    }

    .cosmic-card {
        background: rgba(255, 255, 255, 0.06);
        border: 2px solid rgba(0, 240, 255, 0.5);
        box-shadow: 0 0 30px rgba(255, 0, 127, 0.3), inset 0 0 20px rgba(0, 255, 255, 0.2);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(12px);
        text-align: center;
    }

    .crystal-ball-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 3rem 1rem;
        margin: 2rem 0;
        background: rgba(12, 0, 25, 0.85);
        border-radius: 25px;
        border: 2px solid rgba(255, 0, 127, 0.6);
        box-shadow: 0 0 60px rgba(138, 43, 226, 0.8);
    }

    .glowing-orb {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        background: radial-gradient(circle at 35% 35%, #ffffff, #ff00a0 40%, #00ffff 75%, #0a001a 100%);
        box-shadow: 0 0 40px #ff007f, 0 0 80px #00ffff, inset 0 0 30px #ffffff;
        animation: pulseOrb 1.5s infinite alternate, spinOrb 5s linear infinite;
        margin-bottom: 1.8rem;
    }

    @keyframes pulseOrb {
        0% { transform: scale(0.95); box-shadow: 0 0 30px #ff007f, 0 0 60px #00ffff; }
        100% { transform: scale(1.15); box-shadow: 0 0 60px #ff00a0, 0 0 110px #00ffff; }
    }

    @keyframes spinOrb {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }

    .oracle-text {
        font-family: 'Cinzel Decorative', 'Noto Sans KR', sans-serif;
        font-size: 1.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #e1ff75, #00ffff, #ff007f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: glowText 1.2s ease-in-out infinite alternate;
        text-align: center;
    }

    @keyframes glowText {
        from { opacity: 0.6; }
        to { opacity: 1; }
    }

    [data-testid="stMetricValue"] {
        color: #00ffff !important;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# 3. 우주의 기운 16단계 설정
# ============================================================

COSMIC_LEVELS = [
    {"level": 1, "clicks": 0, "title": "🌱 티끌 같은 미풍의 기운", "desc": "우주의 아주 작은 미풍만이 살랑입니다."},
    {"level": 2, "clicks": 3, "title": "🍃 바람의 기운", "desc": "바람의 파동이 야구장 스탠드를 감쌉니다."},
    {"level": 3, "clicks": 7, "title": "💧 이슬의 기운", "desc": "새벽녘의 차분한 기운이 선수들에게 깃듭니다."},
    {"level": 4, "clicks": 12, "title": "🪨 대지의 기운", "desc": "그라운드 흙 아래 단단한 기운이 꿈틀거립니다."},
    {"level": 5, "clicks": 18, "title": "🔥 대기권 전열의 기운", "desc": "대기권의 열기가 구단의 승부욕을 불태웁니다."},
    {"level": 6, "clicks": 25, "title": "🌙 달빛의 기운", "desc": "은은한 달빛이 승리의 궤적을 비춥니다."},
    {"level": 7, "clicks": 33, "title": "☀️ 태양 광륜의 기운", "desc": "강렬한 태양 광선이 승리의 불꽃을 피웁니다."},
    {"level": 8, "clicks": 42, "title": "🪐 행성 직렬의 기운", "desc": "수성·금성·화성이 일렬로 서며 거대한 끌림을 만듭니다."},
    {"level": 9, "clicks": 52, "title": "⭐ 별자리의 공명", "desc": "수놓아진 성좌들이 승리의 별을 완성해 갑니다."},
    {"level": 10, "clicks": 63, "title": "☄️ 유성우의 파동", "desc": "하늘에서 쏟아지는 유성우가 홈런의 궤적을 그립니다."},
    {"level": 11, "clicks": 75, "title": "🌌 성운의 집속", "desc": "빛나는 가스 성운이 팀 전력을 극대화합니다."},
    {"level": 12, "clicks": 88, "title": "🌠 초신성 폭발의 기운", "desc": "한 해 전체를 뒤흔들 초신성의 폭발력이 모입니다."},
    {"level": 13, "clicks": 102, "title": "💫 은하 소용돌이의 기운", "desc": "거대한 은하수가 구단의 운명을 높은 곳으로 끌어올립니다."},
    {"level": 14, "clicks": 117, "title": "🕳️ 블랙홀 중력의 기운", "desc": "상대 팀의 모든 승운을 흡수하는 강력한 중력이 형성됩니다."},
    {"level": 15, "clicks": 133, "title": "👑 코스믹 엠페러의 기운", "desc": "우주의 질서를 재편하는 제왕의 기운이 강림합니다."},
    {"level": 16, "clicks": 150, "title": "💥 빅뱅(Big Bang) 창조주의 기운", "desc": "우주 창조급 신화! 무조건적인 우승의 운명이 확정됩니다."}
]

# Session State 초기화 (클릭 수 유지)
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

def get_current_cosmic_level(clicks):
    current = COSMIC_LEVELS[0]
    for lvl in COSMIC_LEVELS:
        if clicks >= lvl["clicks"]:
            current = lvl
        else:
            break
    return current

current_level_info = get_current_cosmic_level(st.session_state.click_count)

# ============================================================
# 4. 헤더 및 컨트롤
# ============================================================

st.markdown('<div class="fantasy-title">COSMIC KBO PREDICT</div>', unsafe_allow_html=True)
st.markdown('<div class="fantasy-subtitle">🌌 은하수의 코스믹 파동과 당신의 기운으로 미래 KBO 시즌의 운명을 예언합니다.</div>', unsafe_allow_html=True)

st.divider()

# 시즌(연도) 및 팀 선택
col_season, col_team = st.columns([1, 1])

with col_season:
    # 2027 시즌부터 선택 가능
    seasons = [f"{year} 시즌" for year in range(2027, 2101)]
    selected_season_str = st.selectbox("📅 예언받을 시즌 선택", options=seasons)
    selected_year = int(selected_season_str.split()[0])

with col_team:
    teams_list = ["LG 트윈스", "KIA 타이거즈", "삼성 라이온즈", "KT 위즈", "두산 베어스", 
                  "SSG 랜더스", "롯데 자이언츠", "한화 이글스", "NC 다이노스", "키움 히어로즈"]
    selected_team_name = st.selectbox("🔍 예언받을 팀 선택", options=teams_list)

# ============================================================
# 5. 우주의 기운 클릭 인터랙션 창
# ============================================================

st.markdown('<div class="energy-card">', unsafe_allow_html=True)
st.markdown(f'<div class="energy-level-title">{current_level_info["title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#00ffff; font-size:1.1rem;">현재 모은 우주의 기운: <b>{st.session_state.click_count}</b> 파동 (단계: {current_level_info["level"]} / 16)</p>', unsafe_allow_html=True)
st.markdown(f'<p style="opacity:0.8; font-size:0.9rem;">"{current_level_info["desc"]}"</p>', unsafe_allow_html=True)

btn_col1, btn_col2 = st.columns([2, 1])
with btn_col1:
    if st.button("✨ 클릭하여 우주의 기운 모으기!", use_container_width=True):
        st.session_state.click_count += 1
        st.rerun()

with btn_col2:
    if st.button("🔄 기운 초기화", use_container_width=True):
        st.session_state.click_count = 0
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

predict_button = st.button("🔮 모은 기운으로 미래 운명 예언받기", use_container_width=True)

# ============================================================
# 6. 예언 데이터 생성 엔진 (기운 단계에 따른 순위 보정 적용)
# ============================================================

def generate_season_rankings(year, target_team_name, cosmic_lvl):
    base_teams = [
        "LG 트윈스", "KIA 타이거즈", "삼성 라이온즈", "KT 위즈", "두산 베어스",
        "SSG 랜더스", "롯데 자이언츠", "한화 이글스", "NC 다이노스", "키움 히어로즈"
    ]

    # 시드 고정 (연도 기반)
    rng = random.Random(year)
    shuffled_teams = base_teams.copy()
    rng.shuffle(shuffled_teams)

    # 타겟 팀 원래 순위 찾기
    orig_rank = shuffled_teams.index(target_team_name) + 1

    # 기운 단계(1~16)에 따른 순위 상승 보정 계산
    # cosmic_lvl이 높을수록 최고 1위까지 순위 상승
    rank_boost = int((cosmic_lvl - 1) * (orig_rank - 1) / 15.0)
    final_target_rank = max(1, orig_rank - rank_boost)

    # 순위 재배치
    shuffled_teams.remove(target_team_name)
    shuffled_teams.insert(final_target_rank - 1, target_team_name)

    teams_data = {}
    total_games = 144

    for rank, name in enumerate(shuffled_teams, start=1):
        wins = max(10, int(total_games * (0.63 - (rank * 0.028))))
        draws = rng.randint(0, 3)
        losses = total_games - wins - draws

        win_rate = f"{(wins / (wins + losses)):.3f}"
        gb = f"{(rank - 1) * 2.5:.1f}"

        # 성적 지표 설정 (기운이 대폭 모였을 경우 프리미엄 수치 반영)
        era_base = 3.20 + (rank * 0.18)
        bat_base = 0.290 - (rank * 0.005)

        if name == target_team_name and cosmic_lvl >= 12:
            era_base -= 0.30
            bat_base += 0.015

        teams_data[name] = {
            "name": name,
            "rank": rank,
            "games": total_games,
            "wins": wins,
            "losses": losses,
            "draws": draws,
            "win_rate": win_rate,
            "games_behind": gb,
            "streak": f"{rng.randint(2, 6)}승" if rank <= 3 else (f"{rng.randint(1, 3)}승" if rank <= 5 else f"{rng.randint(1, 4)}패"),
            "era": f"{max(2.50, era_base):.2f}",
            "batting_avg": f"{min(0.330, bat_base):.3f}"
        }

    return teams_data

# ============================================================
# 7. 애니메이션 연출 및 예언 결과 출력
# ============================================================

if predict_button:
    cosmic_level = current_level_info["level"]
    current_teams = generate_season_rankings(selected_year, selected_team_name, cosmic_level)
    team = current_teams[selected_team_name]

    # 기운 단계에 따라 로딩 시간(3초 ~ 10초) 동적 조정
    loading_seconds = max(3, min(10, int(2.5 + (cosmic_level * 0.5))))
    
    loading_placeholder = st.empty()

    phrases = [
        "🌌 은하수의 코스믹 파동을 감지하고 있습니다...",
        f"✨ {current_level_info['title']}이(가) 수정구슬에 공명합니다!",
        "🔮 시공간의 궤적을 넘어 최종 시즌 결과를 불러오는 중...",
        "⚡ 별들의 배치가 완성되어 가고 있습니다...",
        "💥 축적된 우주의 기운이 운명을 폭발적으로 재편합니다!"
    ]

    for i in range(loading_seconds):
        phrase = phrases[i % len(phrases)]
        progress_percent = int(((i + 1) / loading_seconds) * 100)
        
        # 기운 단계가 높을수록 글로우 이펙트 강조
        glow_size = 30 + (cosmic_level * 3)
        
        loading_placeholder.markdown(f"""
            <div class="crystal-ball-container" style="box-shadow: 0 0 {glow_size}px rgba(255, 0, 127, 0.9);">
                <div class="glowing-orb" style="transform: scale({1.0 + (cosmic_level * 0.01)});"></div>
                <div class="oracle-text">{phrase}</div>
                <p style="margin-top: 1rem; color: #00ffff; font-size: 1rem; font-weight: bold;">
                    코스믹 공명률 {progress_percent}% ({i + 1}/{loading_seconds}초)
                </p>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1.0)

    loading_placeholder.empty()

    # 결과 출력
    st.markdown(f"""
        <div class="cosmic-card">
            <h2 style="margin:0; color:#00ffff; font-family:'Noto Sans KR';">🔮 {team['name']} - {selected_year} 시즌 최종 예언</h2>
            <p style="font-size:1.1rem; opacity:0.9; margin-top:5px;">적용된 기운: <b style="color:#ff007f;">{current_level_info['title']}</b> (단계 {cosmic_level})</p>
            <h1 style="font-size:3.2rem; margin: 15px 0;">최종 예상 순위: {team['rank']}위</h1>
            <p style="font-size:1.3rem; font-weight:600;">{team['wins']}승 {team['draws']}무 {team['losses']}패 (승률 {team['win_rate']})</p>
        </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🌌 세부 시즌 지표", "🍂 가을야구 운명"])

    with tab1:
        c1, c2, c3 = st.columns(3)
        c1.metric("총 소화 경기수", f"{team['games']}경기")
        c2.metric("1위와 게임차", f"{team['games_behind']}경기")
        c3.metric("시즌 최종 기운", team["streak"])

        st.markdown("---")
        ca, cb = st.columns(2)
        ca.metric("예상 팀 평균자책점(ERA)", team["era"])
        cb.metric("예상 팀 타율", team["batting_avg"])

    with tab2:
        # 순위에 따른 가을야구 진출 확률 계산
        prob = max(5, min(99, 100 - (team['rank'] - 1) * 11))
        
        st.markdown("##### 🔮 포스트시즌 진출 예언 확률")
        st.progress(prob / 100)
        st.metric("진출 확률", f"{prob}%")
        
        if prob >= 80:
            st.success("✨ 하늘과 우주의 기운이 우승과 포스트시즌 평정을 강력하게 암시합니다!")
        elif prob >= 40:
            st.warning("⚡ 치열한 가을야구 경계선에서 운명이 뜨겁게 요동치고 있습니다.")
        else:
            st.error("🌌 이번 시즌은 우주의 기운이 다소 부족하여 다음을 기약해야 합니다.")

else:
    st.info("👆 상단에서 **시즌**과 **팀**을 선택하고, **'클릭하여 우주의 기운 모으기'** 버튼을 누른 후 예언을 요청해보세요!")
