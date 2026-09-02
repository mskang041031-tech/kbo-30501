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
# 2. 가시성 강화 폰트 & 웅장한 아방가르드 코스믹 CSS
# ============================================================

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Noto+Sans+KR:wght@500;700;900&display=swap');

    [data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none !important;
    }

    /* 가시성을 개선한 메인 배경 */
    .stApp {
        background: linear-gradient(135deg, #05000c 0%, #120024 25%, #220042 50%, #0d0026 75%, #020008 100%) !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* 가시성 개선: 일반 텍스트 및 라벨 강제 흰색 적용 */
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
        margin-bottom: 2rem;
        letter-spacing: 1px;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.8);
    }

    /* 우주의 기운 클릭 카드 */
    .energy-card {
        background: rgba(15, 5, 30, 0.75);
        border: 2px solid #ff007f;
        border-radius: 20px;
        padding: 1.8rem;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 0 30px rgba(255, 0, 127, 0.5), inset 0 0 15px rgba(0, 255, 255, 0.3);
        backdrop-filter: blur(10px);
    }

    .energy-level-title {
        font-family: 'Cinzel Decorative', 'Noto Sans KR', sans-serif;
        font-size: 2rem;
        font-weight: 900;
        color: #ff3399 !important;
        text-shadow: 0 0 12px #ff007f, 0 0 25px #00ffff;
        margin-bottom: 0.5rem;
    }

    .cosmic-card {
        background: rgba(10, 15, 35, 0.85);
        border: 2px solid #00ffff;
        box-shadow: 0 0 40px rgba(0, 240, 255, 0.4), inset 0 0 25px rgba(255, 0, 127, 0.3);
        border-radius: 20px;
        padding: 2.2rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(15px);
        text-align: center;
    }

    /* 텍스트 없는 극적 이펙트 전용 컨테이너 */
    .epic-stage {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 5rem 1rem;
        margin: 2rem 0;
        background: radial-gradient(circle, rgba(30, 0, 60, 0.95) 0%, rgba(2, 0, 8, 0.98) 100%);
        border-radius: 30px;
        border: 2px solid #00ffff;
        box-shadow: 0 0 80px rgba(255, 0, 127, 0.9);
        overflow: hidden;
        position: relative;
    }

    /* 초화려 섬광 충격파 이펙트 */
    .hyper-orb {
        position: relative;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #ffffff, #ff00a0 35%, #00ffff 70%, #000000 100%);
        box-shadow: 0 0 50px #ff007f, 0 0 100px #00ffff, inset 0 0 40px #ffffff;
        animation: hyperPulse 0.4s infinite alternate, hyperSpin 2s linear infinite;
    }

    .shockwave-ring {
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 4px solid rgba(0, 255, 255, 0.8);
        box-shadow: 0 0 30px #00ffff;
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
        0% { transform: scale(0.6); opacity: 1; }
        100% { transform: scale(2.2); opacity: 0; }
    }

    /* Streamlit 요소 가시성 수정 */
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
# 3. 우주의 기운 16단계 (상향된 스택 기준)
# ============================================================

COSMIC_LEVELS = [
    {"level": 1,  "clicks": 0,   "title": "🌱 티끌 같은 미풍의 기운", "desc": "미약한 차원의 울림이 감지됩니다."},
    {"level": 2,  "clicks": 10,  "title": "🍃 대기권 바람의 기운", "desc": "대기의 파동이 야구장을 감쌉니다."},
    {"level": 3,  "clicks": 25,  "title": "💧 심해 이슬의 기운", "desc": "깊은 정적이 승리의 응축을 준비합니다."},
    {"level": 4,  "clicks": 45,  "title": "🪨 대지 공명의 기운", "desc": "그라운드 지각 아래 거대한 기운이 꿈틀거립니다."},
    {"level": 5,  "clicks": 70,  "title": "🔥 마그마 전열의 기운", "desc": "뜨거운 승부욕이 구단 전체를 감쌉니다."},
    {"level": 6,  "clicks": 100, "title": "🌙 인력 달빛의 기운", "desc": "달의 중력이 승리의 궤적을 끌어당깁니다."},
    {"level": 7,  "clicks": 135, "title": "☀️ 태양 플레어의 기운", "desc": "강렬한 수소 폭발의 열기가 승운을 불태웁니다."},
    {"level": 8,  "clicks": 175, "title": "🪐 행성 직렬의 정렬", "desc": "수성·금성·화성이 완벽한 직렬을 이룹니다."},
    {"level": 9,  "clicks": 220, "title": "⭐ 성좌 별자리의 공명", "desc": "천상의 별자리들이 승리의 좌표를 찍습니다."},
    {"level": 10, "clicks": 270, "title": "☄️ 유성우 폭풍의 파동", "desc": "하늘에서 쏟아지는 유성이 홈런을 그립니다."},
    {"level": 11, "clicks": 320, "title": "🌌 발광 성운의 집속", "desc": "아름다운 성운 가스가 전력을 극대화합니다."},
    {"level": 12, "clicks": 370, "title": "🌠 초신성 폭발의 기운", "desc": "한 해를 뒤흔들 초신성의 파동이 분출됩니다."},
    {"level": 13, "clicks": 410, "title": "💫 소용돌이 은하의 기운", "desc": "거대한 은하수가 구단의 운명을 소용돌이칩니다."},
    {"level": 14, "clicks": 440, "title": "🕳️ 블랙홀 중력의 파형", "desc": "상대 팀의 승운을 모조리 흡수하는 중력장입니다."},
    {"level": 15, "clicks": 470, "title": "👑 코스믹 엠페러의 지배", "desc": "우주의 질서를 새로 쓰는 절대자의 기운입니다."},
    {"level": 16, "clicks": 500, "title": "💥 빅뱅(Big Bang) 창조주의 정점", "desc": "우주 창조급 신화! 완벽한 우승의 운명이 확정됩니다."}
]

# State 초기화
current_time = time.time()
if "click_count" not in st.session_state:
    st.session_state.click_count = 0
if "last_click_time" not in st.session_state:
    st.session_state.last_click_time = current_time

# ============================================================
# 4. 시간 경과 감쇠(쿨다운) 및 연타 가속 로직
# ============================================================

time_passed = current_time - st.session_state.last_click_time

# 2초 이상 클릭이 없으면 방치된 시간에 따라 기운 감소
if time_passed > 2.0 and st.session_state.click_count > 0:
    decay_amount = int((time_passed - 2.0) * 8)  # 초당 8스택씩 감소
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
# 5. 헤더 및 컨트롤
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
# 6. 우주의 기운 클릭 창
# ============================================================

st.markdown('<div class="energy-card">', unsafe_allow_html=True)
st.markdown(f'<div class="energy-level-title">{current_level_info["title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#00ffff; font-size:1.2rem; font-weight:700;">현재 누적 기운: <b style="font-size:1.6rem; color:#ff007f;">{st.session_state.click_count}</b> / 500 (단계: {current_level_info["level"]} / 16)</p>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#e0e0e0; font-size:0.95rem;">"{current_level_info["desc"]}"</p>', unsafe_allow_html=True)

btn_col1, btn_col2 = st.columns([2, 1])

with btn_col1:
    if st.button("⚡ 연타하여 우주의 기운 모으기! (쉬면 감소)", use_container_width=True):
        now = time.time()
        interval = now - st.session_state.last_click_time
        
        # 광속 연타 보너스: 클릭 간격이 짧을수록 더 높은 기운을 가산
        if interval < 0.20:
            boost = 5
        elif interval < 0.35:
            boost = 3
        else:
            boost = 1

        st.session_state.click_count = min(500, st.session_state.click_count + boost)
        st.session_state.last_click_time = now
        st.rerun()

with btn_col2:
    if st.button("🔄 기운 초기화", use_container_width=True):
        st.session_state.click_count = 0
        st.session_state.last_click_time = time.time()
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

predict_button = st.button("🔮 모은 기운으로 미래 운명 예언받기", use_container_width=True)

# ============================================================
# 7. 예언 데이터 생성 엔진
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

    # 기운 단계(1~16)에 따라 순위 대폭 보정
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
# 8. 텍스트 없는 화려한 광폭 애니메이션 연출 및 결과
# ============================================================

if predict_button:
    cosmic_level = current_level_info["level"]
    current_teams = generate_season_rankings(selected_year, selected_team_name, cosmic_level)
    team = current_teams[selected_team_name]

    # 단계에 비례하는 연출 시간 (3초 ~ 10초)
    loading_seconds = max(3, min(10, int(2.5 + (cosmic_level * 0.5))))
    
    stage_placeholder = st.empty()

    # 텍스트 없이 수구슬이 거대해지고 번쩍이는 이펙트 연출
    for i in range(loading_seconds * 10):
        # 구슬 크기 및 광채 동적 계산
        base_size = 100 + (cosmic_level * 6)
        pulse = (i % 5) * 4
        size = base_size + pulse
        
        stage_placeholder.markdown(f"""
            <div class="epic-stage">
                <div class="shockwave-ring" style="animation-duration: {max(0.2, 0.9 - cosmic_level * 0.04)}s;"></div>
                <div class="hyper-orb" style="width: {size}px; height: {size}px;"></div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(0.1)

    stage_placeholder.empty()

    # 결과 카드 출력
    st.markdown(f"""
        <div class="cosmic-card">
            <h2 style="margin:0; color:#00ffff; font-family:'Noto Sans KR'; font-weight:800;">🔮 {team['name']} - {selected_year} 시즌 최종 예언</h2>
            <p style="font-size:1.15rem; opacity:0.95; margin-top:8px; color:#ffffff;">적용된 우주의 기운: <b style="color:#ff007f; font-size:1.3rem;">{current_level_info['title']}</b> (단계 {cosmic_level})</p>
            <h1 style="font-size:3.5rem; margin: 15px 0; color:#00ffff; font-family:'Cinzel Decorative'; filter: drop-shadow(0 0 10px #ff007f);">최종 예상 순위: {team['rank']}위</h1>
            <p style="font-size:1.35rem; font-weight:700; color:#ffffff;">{team['wins']}승 {team['draws']}무 {team['losses']}패 (승률 {team['win_rate']})</p>
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

else:
    st.info("👆 상단에서 **시즌**과 **팀**을 선택하고, **'연타하여 우주의 기운 모으기'** 버튼을 빠르게 연타하여 예언을 요청해보세요!")
