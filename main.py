import streamlit as st
import streamlit.components.v1 as components
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
# 2. 레이어 최적화 은하수 배경 & 코스믹 판타지 CSS
# ============================================================

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Noto+Sans+KR:wght@500;700;900&display=swap');

    [data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    /* 은하수 배경 설정 */
    .stApp {
        background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%) !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
        font-family: 'Noto Sans KR', sans-serif;
    }

    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: 
            radial-gradient(circle at 20% 30%, rgba(255, 0, 127, 0.2) 0%, transparent 40%),
            radial-gradient(circle at 80% 70%, rgba(0, 255, 255, 0.22) 0%, transparent 45%),
            radial-gradient(circle at 50% 50%, rgba(138, 43, 226, 0.15) 0%, transparent 60%);
        pointer-events: none !important;
        z-index: -1 !important;
        animation: galaxyMove 20s ease-in-out infinite alternate;
    }

    [data-testid="stMainBlockContainer"] {
        position: relative;
        z-index: 1 !important;
    }

    @keyframes galaxyMove {
        0% { transform: scale(1) rotate(0deg); }
        100% { transform: scale(1.15) rotate(3deg); }
    }

    p, span, label, div {
        color: #f0f6ff !important;
        text-shadow: 0px 1px 3px rgba(0, 0, 0, 0.9);
    }

    .fantasy-title {
        font-family: 'Cinzel Decorative', 'Noto Sans KR', cursive, serif;
        font-size: 3.2rem !important;
        font-weight: 900;
        text-align: center;
        letter-spacing: 2px;
        background: linear-gradient(180deg, #f4ffb0 0%, #00ffff 45%, #0055ff 85%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(3px 4px 0px #ff007f) drop-shadow(0px 0px 22px rgba(0, 240, 255, 0.9));
        margin-bottom: 0.2rem;
    }

    .fantasy-subtitle {
        text-align: center;
        font-size: 1.05rem;
        color: #00ffff !important;
        font-weight: 700;
        margin-bottom: 1.5rem;
        letter-spacing: 1px;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.8);
    }

    /* 클릭 창 (표준 크기) */
    .standard-energy-card {
        background: rgba(12, 4, 28, 0.88);
        border: 3px solid #00ffff;
        border-radius: 24px;
        padding: 2rem 1.5rem;
        text-align: center;
        margin: 1.2rem 0 1.8rem 0;
        box-shadow: 0 0 35px rgba(255, 0, 127, 0.6), inset 0 0 25px rgba(0, 255, 255, 0.3);
        backdrop-filter: blur(12px);
        min-height: 240px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transition: all 0.3s ease;
    }

    .standard-energy-card:hover {
        box-shadow: 0 0 50px rgba(0, 255, 255, 0.85), inset 0 0 35px rgba(255, 0, 127, 0.5);
        border-color: #ff007f;
    }

    .energy-label-tag {
        font-size: 1rem;
        color: #88ccff !important;
        letter-spacing: 2px;
        margin-bottom: 0.8rem;
        font-weight: 700;
    }

    .energy-level-name {
        font-family: 'Cinzel Decorative', 'Noto Sans KR', sans-serif;
        font-size: 2.2rem;
        font-weight: 900;
        color: #ff3399 !important;
        text-shadow: 0 0 16px #ff007f, 0 0 30px #00ffff;
    }

    /* 이펙트 오비트 무대 */
    .epic-stage {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2.5rem 1rem;
        width: 100%;
        overflow: hidden;
        position: relative;
    }

    .hyper-orb {
        position: relative;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #ffffff, #ff00a0 35%, #00ffff 70%, #000000 100%);
        animation: hyperPulse 0.4s infinite alternate, hyperSpin 2s linear infinite;
    }

    .shockwave-ring {
        position: absolute;
        border-radius: 50%;
        border: 3px solid rgba(0, 255, 255, 0.8);
        animation: shockwave 0.8s infinite ease-out;
    }

    @keyframes hyperPulse {
        0% { transform: scale(0.92); filter: brightness(1.2) hue-rotate(0deg); }
        100% { transform: scale(1.22); filter: brightness(2.5) hue-rotate(180deg); }
    }

    @keyframes hyperSpin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    @keyframes shockwave {
        0% { transform: scale(0.4); opacity: 1; }
        100% { transform: scale(2.2); opacity: 0; }
    }

    [data-testid="stMetricValue"] {
        color: #00ffff !important;
        font-size: 2.2rem !important;
        font-weight: 900 !important;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.7);
    }
    
    [data-testid="stMetricLabel"] {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
    }

    .stSelectbox label {
        color: #00ffff !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# 3. 우주의 기운 16단계 (500 스택 기준)
# ============================================================

COSMIC_LEVELS = [
    {"level": 1,  "clicks": 0,   "title": "🌱 티끌 같은 미풍의 기운"},
    {"level": 2,  "clicks": 10,  "title": "🍃 대기권 바람의 기운"},
    {"level": 3,  "clicks": 25,  "title": "💧 심해 이슬의 기운"},
    {"level": 4,  "clicks": 45,  "title": "🪨 대지 공명의 기운"},
    {"level": 5,  "clicks": 70,  "title": "🔥 마그마 전열의 기운"},
    {"level": 6,  "clicks": 100, "title": "🌙 인력 달빛의 기운"},
    {"level": 7,  "clicks": 135, "title": "☀️ 태양 플레어의 기운"},
    {"level": 8,  "clicks": 175, "title": "🪐 행성 직렬의 정렬"},
    {"level": 9,  "clicks": 220, "title": "⭐ 성좌 별자리의 공명"},
    {"level": 10, "clicks": 270, "title": "☄️ 유성우 폭풍의 파동"},
    {"level": 11, "clicks": 320, "title": "🌌 발광 성운의 집속"},
    {"level": 12, "clicks": 370, "title": "🌠 초신성 폭발의 기운"},
    {"level": 13, "clicks": 410, "title": "💫 소용돌이 은하의 기운"},
    {"level": 14, "clicks": 440, "title": "🕳️ 블랙홀 중력의 파형"},
    {"level": 15, "clicks": 470, "title": "👑 코스믹 엠페러의 지배"},
    {"level": 16, "clicks": 500, "title": "💥 빅뱅(Big Bang) 창조주의 정점"}
]

# Session State 안전한 초기화
current_time = time.time()
if "click_count" not in st.session_state:
    st.session_state.click_count = 0
if "last_click_time" not in st.session_state:
    st.session_state.last_click_time = current_time
if "predict_result" not in st.session_state:
    st.session_state.predict_result = None

# [개선된 감쇠 로직] 마지막 클릭 후 2.5초 이상 방치 시 차감
time_passed = current_time - st.session_state.last_click_time
if time_passed > 2.5 and st.session_state.click_count > 0:
    decay_amount = int((time_passed - 2.5) * 6)
    st.session_state.click_count = max(0, st.session_state.click_count - decay_amount)
    st.session_state.last_click_time = current_time

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

col_season, col_team = st.columns([1, 1])

with col_season:
    seasons = [f"{year} 시즌" for year in range(2027, 2101)]
    selected_season_str = st.selectbox("📅 예언받을 시즌 선택", options=seasons)
    selected_year = int(selected_season_str.split()[0])

with col_team:
    teams_list = ["LG 트윈스", "KIA 타이거즈", "삼성 라이온즈", "KT 위즈", "두산 베어스", 
                  "SSG 랜더스", "롯데 자이언츠", "한화 이글스", "NC 다이노스", "키움 히어로즈"]
    selected_team_name = st.selectbox("🔍 예언받을 팀 선택", options=teams_list)

# ============================================================
# 5. 예언 데이터 생성 엔진
# ============================================================

def generate_season_rankings(year, target_team_name, cosmic_lvl):
    base_teams = [
        "LG 트윈스", "KIA 타이거즈", "삼성 라이온즈", "KT 위즈", "두산 베어스",
        "SSG 랜더스", "롯데 자이언츠", "한화 이글스", "NC 다이노스", "키움 히어로즈"
    ]

    rng = random.Random(year)
    shuffled_teams = base_teams.copy()
    rng.shuffle(shuffled_teams)

    orig_rank = shuffled_teams.index(target_team_name) + 1

    rank_boost = int((cosmic_lvl - 1) * (orig_rank - 1) / 15.0)
    final_target_rank = max(1, orig_rank - rank_boost)

    shuffled_teams.remove(target_team_name)
    shuffled_teams.insert(final_target_rank - 1, target_team_name)

    teams_data = {}
    total_games = 144

    for rank, name in enumerate(shuffled_teams, start=1):
        wins = max(10, int(total_games * (0.64 - (rank * 0.028))))
        draws = rng.randint(0, 3)
        losses = total_games - wins - draws

        win_rate = f"{(wins / (wins + losses)):.3f}"
        gb = f"{(rank - 1) * 2.5:.1f}"

        era_base = 3.20 + (rank * 0.18)
        bat_base = 0.290 - (rank * 0.005)

        if name == target_team_name and cosmic_lvl >= 10:
            era_base -= 0.40
            bat_base += 0.020

        teams_data[name] = {
            "name": name,
            "rank": rank,
            "games": total_games,
            "wins": wins,
            "losses": losses,
            "draws": draws,
            "win_rate": win_rate,
            "games_behind": gb,
            "streak": f"{rng.randint(2, 8)}승" if rank <= 3 else (f"{rng.randint(1, 3)}승" if rank <= 5 else f"{rng.randint(1, 4)}패"),
            "era": f"{max(2.20, era_base):.2f}",
            "batting_avg": f"{min(0.340, bat_base):.3f}"
        }

    return teams_data

# ============================================================
# 6. 클릭 창 & 예언 결과 통합 보드
# ============================================================

mega_card_placeholder = st.empty()

# 클릭 창 (결과 출력이 없을 때)
if st.session_state.predict_result is None:
    with mega_card_placeholder.container():
        st.markdown(f"""
            <div class="standard-energy-card">
                <div class="energy-label-tag">적용된 우주의 기운 ({st.session_state.click_count} 스택)</div>
                <div class="energy-level-name">{current_level_info["title"]}</div>
            </div>
        """, unsafe_allow_html=True)

btn_col1, btn_col2 = st.columns([2, 1])

with btn_col1:
    if st.button("⚡ 클릭하여 우주의 기운 모으기!", use_container_width=True):
        st.session_state.predict_result = None
        st.session_state.click_count = min(500, st.session_state.click_count + 1)
        st.session_state.last_click_time = time.time()
        st.rerun()

with btn_col2:
    if st.button("🔄 기운 초기화", use_container_width=True):
        st.session_state.click_count = 0
        st.session_state.predict_result = None
        st.session_state.last_click_time = time.time()
        st.rerun()

predict_button = st.button("🔮 모은 기운으로 미래 운명 예언받기", use_container_width=True)

# ============================================================
# 7. 이펙트 차등 연출 및 예언 결과 출력
# ============================================================

if predict_button:
    cosmic_level = current_level_info["level"]
    current_teams = generate_season_rankings(selected_year, selected_team_name, cosmic_level)
    team = current_teams[selected_team_name]

    # 로딩 애니메이션 프레임 축소 (UI 병목 해소)
    loading_seconds = max(2, min(5, int(1.5 + (cosmic_level * 0.25))))

    for i in range(loading_seconds * 5):
        base_size = 70 + (cosmic_level * 8)
        pulse = (i % 4) * (2 + cosmic_level // 2)
        size = base_size + pulse

        glow_main = 15 + (cosmic_level * 4)
        glow_outer = 30 + (cosmic_level * 8)

        pulse_speed = max(0.1, 0.6 - (cosmic_level * 0.03))
        spin_speed = max(0.4, 2.5 - (cosmic_level * 0.12))
        hue_shift = (i * 30 * cosmic_level) % 360

        shockwave_speed = max(0.2, 1.0 - (cosmic_level * 0.05))

        mega_card_placeholder.markdown(f"""
            <div class="standard-energy-card">
                <div class="epic-stage">
                    <div class="shockwave-ring" style="
                        width: {size}px;
                        height: {size}px;
                        border-width: {2 + cosmic_level // 3}px;
                        animation-duration: {shockwave_speed}s;
                        box-shadow: 0 0 {glow_main}px #00ffff;
                    "></div>
                    <div class="hyper-orb" style="
                        width: {size}px;
                        height: {size}px;
                        box-shadow: 0 0 {glow_main}px #ff007f, 0 0 {glow_outer}px #00ffff, inset 0 0 {glow_main}px #ffffff;
                        animation-duration: {pulse_speed}s, {spin_speed}s;
                        filter: brightness({1.0 + cosmic_level * 0.12}) hue-rotate({hue_shift}deg);
                    "></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(0.15)

    st.session_state.predict_result = {
        "team": team,
        "year": selected_year,
        "level": cosmic_level
    }
    st.rerun()

# 예언 결과 출력
if st.session_state.predict_result is not None:
    res = st.session_state.predict_result
    team = res["team"]
    
    with mega_card_placeholder.container():
        st.markdown(f"""
            <div class="standard-energy-card">
                <h2 style="margin:0; color:#00ffff; font-family:'Noto Sans KR'; font-weight:800;">🔮 {team['name']} - {res['year']} 시즌 최종 예언</h2>
                <h1 style="font-size:3.2rem; margin: 15px 0; color:#00ffff; font-family:'Cinzel Decorative'; filter: drop-shadow(0 0 12px #ff007f);">최종 예상 순위: {team['rank']}위</h1>
                <p style="font-size:1.3rem; font-weight:700; color:#ffffff;">{team['wins']}승 {team['draws']}무 {team['losses']}패 (승률 {team['win_rate']})</p>
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
        prob = max(5, min(99, 100 - (team['rank'] - 1) * 11))
        
        st.markdown("##### 🔮 포스트시즌 진출 예언 확률")
        st.progress(prob / 100)
        st.metric("진출 확률", f"{prob}%")
        
        if prob >= 80:
            st.success("✨ 하늘과 우주의 기운이 우승과 포스트시즌 평정을 강력하게 암시합니다!")
        elif prob >= 40:
            st.warning("⚡ 치열한 가을야구 경계선에서 운명이 뜨겁게 요동치고 있습니다.")
        else:
            st.error("🌌 이번 시즌은 우주의 기운이 부족하여 다음을 기약해야 합니다.")
