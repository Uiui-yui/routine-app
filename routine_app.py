import streamlit as st
import datetime

st.set_page_config(page_title="ルーティン計算アプリ", page_icon="🛌")

st.title("🛌 睡眠ルーティン逆算アプリ")

# 家を出る時間（入力）
leave_time = st.time_input("🚶‍♀️ 家を出る時間を入力してください", value=datetime.time(8, 0))

# 各所要時間（調整可能、デフォルトあり）
wake_to_leave = st.number_input("🕒 起床から家を出るまでの時間（分）", value=60, step=5)
sleep_duration = st.number_input("💤 睡眠時間（分）", value=450, step=15)  # 7.5h = 450min
bed_to_sleep = st.number_input("🌙 就寝から入眠までの時間（分）", value=30, step=5)
work_to_bed = st.number_input("🧑‍💻 作業終了から就寝までの時間（分）", value=120, step=10)

# 計算
leave_dt = datetime.datetime.combine(datetime.date.today(), leave_time)

# 各段階を逆算
wake_time = leave_dt - datetime.timedelta(minutes=wake_to_leave)
sleep_time = wake_time - datetime.timedelta(minutes=sleep_duration)
bed_time = sleep_time - datetime.timedelta(minutes=bed_to_sleep)
work_finish_time = bed_time - datetime.timedelta(minutes=work_to_bed)

# 結果表示
st.subheader("⏰ あなたの理想ルーティン")
st.info(f"✅ 起きる時間：{wake_time.strftime('%H:%M')}")
st.success(f"🛌 入眠時間：{sleep_time.strftime('%H:%M')}")
st.warning(f"🌙 就寝時間（ベッドに入る）：{bed_time.strftime('%H:%M')}")
st.error(f"🧑‍💻 作業終了時間：{work_finish_time.strftime('%H:%M')}")