import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="미디어 사용 습관 자가진단", page_icon="📱")
st.title("📱 미디어 사용 습관 자가진단")
st.write(
    "이름과 나이를 입력하고, 각 미디어 매체별 하루 평균 사용시간을 입력해 주세요."
)

# 미디어 매체 리스트 한정
media_list = ["유튜브", "틱톡", "인스타", "트위터", "넷플릭스"]


# 2. 결과 분석 및 출력 함수 (def 사용)
def analyze_media_habit(user_name, user_age, usage_data):
  # 입력받은 사용시간 총합 계산
  total_hours = sum(usage_data.values())

  st.divider()
  st.subheader("📊 검사 결과")

  # 가장 많이 사용한 미디어 매체 찾기 (모두 0시간일 경우 예외 처리)
  if total_hours == 0:
    st.info(
        f"**{user_name}** 님({user_age}세)은 미디어를 전혀 사용하지 않으시네요!"
    )
  else:
    # 사용시간이 가장 큰 매체 추출
    most_used_media = max(usage_data, key=usage_data.get)
    st.info(
        f"**{user_name}** 님의 나이대({user_age}세)에서 가장 많이 사용하는"
        f" 미디어 매체는 **{most_used_media}** 입니다."
    )

  # 3시간 이상 여부에 따른 중독 판별 (if문 사용)
  if total_hours >= 3.0:
    st.error(
        f"검사 결과 **{user_name}**님은 미디어 중독이 **맞습니다.** (총"
        f" 사용시간: {total_hours:.1f}시간)"
    )
    st.warning("미디어 사용을 줄여보세요.")
  else:
    st.success(
        f"검사 결과 **{user_name}**님은 미디어 중독이 **아닙니다.** (총"
        f" 사용시간: {total_hours:.1f}시간)"
    )
    st.balloons()
    st.write("잘 하고 계시네요!")


# 3. 기본 정보 입력 (이름, 나이)
col1, col2 = st.columns(2)
with col1:
  name = st.text_input("이름을 입력하세요", placeholder="예: 홍길동")
with col2:
  age = st.number_input("나이를 입력하세요", min_value=1, max_value=120, value=16)

st.subheader("⏱️ 매체별 하루 사용시간 (시간 단위)")

# 4. for문을 사용해 각 미디어 매체당 사용시간 반복 입력받기
usage_dict = {}  # 매체별 시간을 저장할 딕셔너리
for media in media_list:
  hours = st.number_input(
      f"**{media}**의 하루 사용시간은 얼마나 되나요?",
      min_value=0.0,
      max_value=24.0,
      value=0.0,
      step=0.5,
      key=media,
  )
  usage_dict[media] = hours  # 예: {"유튜브": 2.0, "틱톡": 1.5, ...}

# 5. 버튼 클릭 시 결과 실행
if st.button("🔍 검사 결과 확인하기", use_container_width=True):
  if name.strip() == "":
    st.warning("이름을 먼저 입력해 주세요!")
  else:
    analyze_media_habit(name, age, usage_dict)
