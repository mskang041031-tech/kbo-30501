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
# 2. KBO 10개 구단 시그니처 Glowing 컬러 맵핑
# ============================================================

TEAM_COLORS = {
    "LG 트윈스": {"main": "#C3002F", "sub": "#FF4D6D"},
    "KIA 타이거즈": {"main": "#EA0029", "sub": "#FF4D4D"},
    "삼성 라이온즈": {"main": "#0066FF", "sub": "#00D8FF"},
    "KT 위즈": {"main": "#FF003B", "sub": "#FF6680"},
    "두산 베어스": {"main": "#1A49C8", "sub": "#5C85FF"},
    "SSG 랜더스": {"main": "#CE0E2D", "sub": "#FF3355"},
    "롯데 자이언츠": {"main": "#003399", "sub": "#DC042B"},
    "한화 이글스": {"main": "#FF6600", "sub": "#FFAA00"},
    "NC 다이노스": {"main": "#0072CE", "sub": "#E3A300"},
    "키움 히어로즈": {"main": "#820024", "sub": "#FF2A6D"}
}

# 헤더 및 팀 선택 UI
st.markdown('<div class="fantasy-title">COSMIC KBO PREDICT</div>', unsafe_allow_html=True)
st.markdown('<div class="fantasy-subtitle">🌌 은하수의 코스믹 파동과 당신의 기운으로 미래 KBO 시즌의 운명을 예언합니다.</div>', unsafe_allow_html=True)

st.divider()

col_season, col_team = st.columns([1, 1])

with col_season:
    seasons = [f"{year} 시즌" for year in range(2027, 2101)]
    selected_season_str = st.selectbox("📅 예언받을 시즌 선택", options=seasons)
    selected_year = int(selected_season_str.split()[0])

with col_team:
    teams_list = list(TEAM_COLORS.keys())
    selected_team_name = st.selectbox("🔍 예언받을 팀 선택", options=teams_list)

current_team_color = TEAM_COLORS[selected_team_name]["main"]
current_team_sub_color = TEAM_COLORS[selected_team_name]["sub"]

# ============================================================
# 3. 팀별 동적 CSS & 가시성 대폭 개선 폰트 스타일
# ============================================================

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Noto+Sans+KR:wght@500;700;900&display=swap');

    :root {{
        --team-glow: {current_team_color};
        --team-sub-glow: {current_team_sub_color};
    }}

    [data-testid="stSidebar"], [data-testid="collapsedControl"] {{
        display: none !important;
    }}

    .stApp {{
        background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%) !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
        font-family: 'Noto Sans KR', sans-serif;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: 
            radial-gradient(circle at 20% 30%, rgba(255, 0, 127, 0.15) 0%, transparent 40%),
            radial-gradient(circle at 80% 70%, var(--team-glow) 0.2, transparent 45%),
            radial-gradient(circle at 50% 50%, rgba(138, 43, 226, 0.15) 0%, transparent 60%);
        pointer-events: none !important;
        z-index: -1 !important;
        animation: galaxyMove 20s ease-in-out infinite alternate;
    }}

    [data-testid="stMainBlockContainer"] {{
        position: relative;
        z-index: 1 !important;
    }}

    /* === 폰트 가시성 강화 스타일 === */
    p, span, label, div {{
        color: #ffffff !important;
        text-shadow: 0 1px 3px rgba(0, 0, 0, 0.95) !important;
        font-weight: 600;
        letter-spacing: -0.3px;
    }}

    .fantasy-title {{
        font-family: 'Cinzel Decorative', 'Noto Sans KR', cursive, serif;
        font-size: 3.2rem !important;
        font-weight: 900;
        text-align: center;
        letter-spacing: 2px;
        background: linear-gradient(180deg, #ffffff 0%, var(--team-sub-glow) 50%, var(--team-glow) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 0px 18px var(--team-glow));
        margin-bottom: 0.2rem;
    }}

    .fantasy-subtitle {{
        text-align: center;
        font-size: 1.05rem;
        color: #ffffff !important;
        font-weight: 700;
        margin-bottom: 1.5rem;
        letter-spacing: 0.5px;
        text-shadow: 0 0 12px var(--team-glow), 0 2px 4px #000000 !important;
    }}

    /* 표준 카드 */
    .standard-energy-card {{
        background: rgba(8, 2, 20, 0.92);
        border: 3px solid var(--team-glow);
        border-radius: 24px;
        padding: 1.8rem 1.5rem;
        text-align: center;
        margin: 1.2rem 0 1.8rem 0;
        box-shadow: 0 0 35px var(--team-glow), inset 0 0 25px var(--team-sub-glow);
        backdrop-filter: blur(12px);
        min-height: 240px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }}

    /* 피버타임 불꽃 특수 카드 */
    .fever-energy-card {{
        background: rgba(30, 0, 0, 0.95) !important;
        border: 3px solid #ff3300 !important;
        box-shadow: 0 0 55px #ff3300, inset 0 0 35px #ff9900 !important;
        animation: feverGlow 0.6s infinite alternate;
    }}

    @keyframes feverGlow {{
        0% {{ box-shadow: 0 0 35px #ff3300, inset 0 0 20px #ff9900; }}
        100% {{ box-shadow: 0 0 65px #ff6600, inset 0 0 40px #ffcc00; }}
    }}

    /* 피버타임 프로그레스 바 영역 */
    .fever-bar-container {{
        width: 100%;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        height: 14px;
        margin-bottom: 1rem;
        overflow: hidden;
        border: 1px solid #ff6600;
    }}

    .fever-bar-fill {{
        height: 100%;
        background: linear-gradient(90deg, #ff0000, #ff9900, #ffff00);
        box-shadow: 0 0 10px #ff6600;
        transition: width 0.1s linear;
    }}

    .energy-label-tag {{
        font-size: 1.05rem;
        color: #ffffff !important;
        letter-spacing: 1px;
        margin-bottom: 0.6rem;
        font-weight: 800;
        background: rgba(0, 0, 0, 0.6);
        padding: 5px 14px;
        border-radius: 12px;
        display: inline-block;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .energy-level-name {{
        font-family: 'Noto Sans KR', sans-serif !important;
        font-size: 2.1rem;
        font-weight: 900;
        color: #ffffff !important;
        text-shadow: 0 0 12px var(--team-glow), 0 0 24px var(--team-sub-glow), 0 2px 5px #000000 !important;
    }}

    .fever-text-title {{
        font-size: 2.3rem;
        font-weight: 900;
        color: #ffff00 !important;
        text-shadow: 0 0 15px #ff3300, 0 0 30px #ff0000, 0 2px 4px #000000 !important;
        animation: pulseText 0.3s infinite alternate;
    }}

    @keyframes pulseText {{
        0% {{ transform: scale(0.98); }}
        100% {{ transform: scale(1.04); }}
    }}

    /* Metric 가시성 수정 */
    [data-testid="stMetricValue"] {{
        color: #ffffff !important;
        font-size: 2.2rem !important;
        font-weight: 900 !important;
        text-shadow: 0 0 14px var(--team-glow), 0 2px 6px #000000 !important;
    }}
    
    [data-testid="stMetricLabel"] {{
        color: #f0f6ff !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        text-shadow: 0 1px 3px #000000 !important;
    }}

    .stSelectbox label {{
        color: #ffffff !important;
        font-size: 1.15rem !important;
        font-weight: 800 !important;
        text-shadow: 0 0 10px var(--team-glow), 0 2px 4px #000000 !important;
    }}
    </style>
""", unsafe_allow_html=True)

# ============================================================
# 4. 우주의 기운 16단계 & 세션 상태 관리
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

current_time = time.time()

# 세션 상태 관리
if "click_count" not in st.session_state:
    st.session_state.click_count = 0
if "fever_counter" not in st.session_state:
    st.session_state.fever_counter = 0  # 60스택 측정 카운터
if "is_fever" not in st.session_state:
    st.session_state.is_fever = False
if "fever_end_time" not in st.session_state:
    st.session_state.fever_end_time = 0
if "last_click_time" not in st.session_state:
    st.session_state.last_click_time = current_time
if "predict_result" not in st.session_state:
    st.session_state.predict_result = None

# 피버타임 만료 판정
if st.session_state.is_fever and current_time >= st.session_state.fever_end_time:
    st.session_state.is_fever = False
    st.session_state.fever_counter = 0  # 종료 후 0부터 다시 카운트

# 방치 시 자연 감쇠 (피버타임 중에는 감쇠 없음)
if not st.session_state.is_fever:
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
# 5. 예언 데이터 생성 엔진
# ============================================================

def generate_season_rankings(year, target_team_name, cosmic_lvl):
    base_teams = list(TEAM_COLORS.keys())

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
# 6. 클릭 창 & 불꽃 이펙트 보드
# ============================================================

mega_card_placeholder = st.empty()

if st.session_state.predict_result is None:
    with mega_card_placeholder.container():
        # 피버타임 상태일 때의 UI 연출
        if st.session_state.is_fever:
            remaining_time = max(0.0, st.session_state.fever_end_time - current_time)
            progress_percent = (remaining_time / 9.0) * 100

            st.markdown(f"""
                <div class="standard-energy-card fever-energy-card">
                    <div class="fever-bar-container">
                        <div class="fever-bar-fill" style="width: {progress_percent}%;"></div>
                    </div>
                    <div class="energy-label-tag" style="border-color:#ff6600; color:#ffcc00 !important;">
                        🔥 FEVER TIME (3배 속도 충전 중!) - 남은시간 {remaining_time:.1f}초
                    </div>
                    <div class="fever-text-title">🔥 코스믹 피버 스퍼트!! 🔥</div>
                    <div style="font-size:1.1rem; color:#ffffff; margin-top:8px; font-weight:700;">
                        현재 기운: {st.session_state.click_count} 스택 ({current_level_info["title"]})
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            # 일반 상태 UI 연출
            st.markdown(f"""
                <div class="standard-energy-card">
                    <div class="energy-label-tag">
                        적용된 우주의 기운 ({st.session_state.click_count} 스택) | 피버 게이지: {st.session_state.fever_counter}/60
                    </div>
                    <div class="energy-level-name">{current_level_info["title"]}</div>
                </div>
            """, unsafe_allow_html=True)

# 버튼 영역
btn_col1, btn_col2 = st.columns([2, 1])

with btn_col1:
    click_label = "🔥 피버 파워 클릭!! (+3)" if st.session_state.is_fever else "⚡ 클릭하여 우주의 기운 모으기!"
    if st.button(click_label, use_container_width=True):
        st.session_state.predict_result = None
        st.session_state.last_click_time = time.time()

        if st.session_state.is_fever:
            # 피버타임 중에는 3배 상향 조정
            st.session_state.click_count = min(500, st.session_state.click_count + 3)
        else:
            # 일반 클릭 (+1)
            st.session_state.click_count = min(500, st.session_state.click_count + 1)
            st.session_state.fever_counter += 1

            # 60스택 달성 시 피버타임 돌입 (9초 유지)
            if st.session_state.fever_counter >= 60:
                st.session_state.is_fever = True
                st.session_state.fever_end_time = time.time() + 9.0
                st.session_state.fever_counter = 0

        st.rerun()

with btn_col2:
    if st.button("🔄 기운 초기화", use_container_width=True):
        st.session_state.click_count = 0
        st.session_state.fever_counter = 0
        st.session_state.is_fever = False
        st.session_state.predict_result = None
        st.session_state.last_click_time = time.time()
        st.rerun()

predict_button = st.button("🔮 모은 기운으로 미래 운명 예언받기", use_container_width=True)

# ============================================================
# 7. 예언 연출 및 결과 출력
# ============================================================

if predict_button:
    cosmic_level = current_level_info["level"]
    current_teams = generate_season_rankings(selected_year, selected_team_name, cosmic_level)
    team = current_teams[selected_team_name]

    loading_seconds = max(2, min(5, int(1.5 + (cosmic_level * 0.25))))

    for i in range(loading_seconds * 5):
        base_size = 70 + (cosmic_level * 8)
        pulse = (i % 4) * (2 + cosmic_level // 2)
        size = base_size + pulse

        glow_main = 15 + (cosmic_level * 4)
        glow_outer = 30 + (cosmic_level * 8)

        pulse_speed = max(0.1, 0.6 - (cosmic_level * 0.03))
        spin_speed = max(0.4, 2.5 - (cosmic_level * 0.12))

        mega_card_placeholder.markdown(f"""
            <div class="standard-energy-card">
                <div class="epic-stage">
                    <div class="shockwave-ring" style="
                        width: {size}px;
                        height: {size}px;
                        border-width: {2 + cosmic_level // 3}px;
                        animation-duration: {pulse_speed}s;
                        box-shadow: 0 0 {glow_main}px var(--team-glow);
                    "></div>
                    <div class="hyper-orb" style="
                        width: {size}px;
                        height: {size}px;
                        box-shadow: 0 0 {glow_main}px var(--team-glow), 0 0 {glow_outer}px var(--team-sub-glow), inset 0 0 {glow_main}px #ffffff;
                        animation-duration: {pulse_speed}s, {spin_speed}s;
                    "></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(0.12)

    st.session_state.predict_result = {
        "team": team,
        "year": selected_year,
        "level": cosmic_level
    }
    st.rerun()

# 예언 결과 카드 출력
if st.session_state.predict_result is not None:
    res = st.session_state.predict_result
    team = res["team"]
    
    with mega_card_placeholder.container():
        st.markdown(f"""
            <div class="standard-energy-card">
                <h2 style="margin:0; color:#ffffff; font-family:'Noto Sans KR'; font-weight:800; text-shadow:0 0 10px var(--team-glow);">🔮 {team['name']} - {res['year']} 시즌 최종 예언</h2>
                <h1 style="font-size:3.2rem; margin: 15px 0; color:#ffffff; font-family:'Cinzel Decorative'; filter: drop-shadow(0 0 16px var(--team-glow));">최종 예상 순위: {team['rank']}위</h1>
                <p style="font-size:1.35rem; font-weight:800; color:#ffffff;">{team['wins']}승 {team['draws']}무 {team['losses']}패 (승률 {team['win_rate']})</p>
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

# 수행평가 안내
st.markdown("---")
with st.expander("ℹ️ COSMIC PREDICT 알고리즘 및 기술 사양"):
    st.markdown("""
    * **개발 언어 및 프레임워크:** Python 3.10+, Streamlit
    * **주요 기능:**
      * 피버타임(Fever Time) 메커니즘: 60스택 달성 시 9초간 불꽃 이펙트 및 스택 3배 보너스 부스트
      * CSS Variables (`--team-glow`) 기반 10개 구단 고유 상징색 수용 스타일 엔진
      * 실시간 CSS Progress-Bar 애니메이션을 활용한 피버타임 타이머 UI
      * Noto Sans KR 900 기반 고가시성 텍스트 섀도 기법 적용
    """)
