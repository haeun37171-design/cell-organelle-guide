import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="세포 소기관 안내 앱", page_icon="🔬", layout="centered"
)

# 제목 및 안내 문구
st.title("🔬 세포 소기관 기능 안내 앱")
st.write("랜덤으로 소기관을 뽑거나, 궁금한 소기관 이름을 직접 입력해 보세요!")

# 5가지 세포 소기관 및 기능 데이터
organelles = {
    "핵": {
        "emoji": "🧠",
        "function": "유전정보 저장 및 세포활동 조절",
    },
    "미토콘드리아": {
        "emoji": "⚡",
        "function": "세포활동에 필요한 에너지 생성",
    },
    "리보솜": {
        "emoji": "🏭",
        "function": "단백질을 합성",
    },
    "세포막": {
        "emoji": "🛡️",
        "function": "세포 안팎으로 물질이 드나드는 것을 조절",
    },
    "골지체": {
        "emoji": "📦",
        "function": "물질을 분류하고 운반",
    },
}

st.divider()

# 1. 랜덤 뽑기 기능
st.subheader("🎲 랜덤으로 알아보기")
if st.button("랜덤 세포 소기관 뽑기!", type="primary", use_container_width=True):
  chosen_name = random.choice(list(organelles.keys()))
  chosen_info = organelles[chosen_name]

  st.success(f"뽑힌 세포 소기관: **{chosen_name}**")
  st.markdown(f"### {chosen_info['emoji']} {chosen_name}")
  st.info(f"**기능:** {chosen_info['function']}")

st.divider()

# 2. 직접 입력하여 검색하기 기능
st.subheader("🔍 직접 입력해서 찾아보기")
user_input = st.text_input(
    "세포 소기관 이름을 입력하세요:", placeholder="예: 세포막"
)

if st.button("기능 확인하기", use_container_width=True):
  # 입력값 앞뒤 공백 제거
  clean_input = user_input.strip()

  if clean_input in organelles:
    info = organelles[clean_input]
    st.success(f"찾은 세포 소기관: **{clean_input}**")
    st.markdown(f"### {info['emoji']} {clean_input}")
    st.info(f"**기능:** {info['function']}")
  else:
    # 5개 소기관에 없을 경우 안내 메시지 출력
    st.warning(
        "해당 세포소기관은 아직 등록되어 있지 않습니다. 핵, 미토콘드리아,"
        " 리보솜, 세포막, 골지체 중 하나를 입력해 주세요!"
    )
