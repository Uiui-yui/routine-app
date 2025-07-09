import streamlit as st
import datetime

st.set_page_config(page_title="ルーティン計算アプリ", page_icon="🛌")

st.title("🌙睡眠時間管理アプリ")

# 家を出る時間（入力）
leave_time = st.time_input("家を出る時間を入力", value=datetime.time(8, 0))

# 各所要時間（時間＋分）で入力
wake_h = st.number_input("起床〜出発：時間", min_value=0, max_value=12, value=1)
wake_m = st.number_input("起床〜出発：分", min_value=0, max_value=59, value=0)

sleep_h = st.number_input("睡眠時間：時間", min_value=0, max_value=12, value=7)
sleep_m = st.number_input("睡眠時間：分", min_value=0, max_value=59, value=30)

bed_h = st.number_input("就寝〜入眠：時間", min_value=0, max_value=3, value=0)
bed_m = st.number_input("就寝〜入眠：分", min_value=0, max_value=59, value=30)

work_h = st.number_input("作業終了〜就寝：時間", min_value=0, max_value=6, value=2)
work_m = st.number_input("作業終了〜就寝：分", min_value=0, max_value=59, value=0)

# 分単位に変換
wake_to_leave = wake_h * 60 + wake_m
sleep_duration = sleep_h * 60 + sleep_m
bed_to_sleep = bed_h * 60 + bed_m
work_to_bed = work_h * 60 + work_m

# 時刻計算
leave_dt = datetime.datetime.combine(datetime.date.today(), leave_time)
wake_time = leave_dt - datetime.timedelta(minutes=wake_to_leave)
sleep_time = wake_time - datetime.timedelta(minutes=sleep_duration)
bed_time = sleep_time - datetime.timedelta(minutes=bed_to_sleep)
work_finish_time = bed_time - datetime.timedelta(minutes=work_to_bed)

# 結果表示（先に表示）
st.subheader("今日のルーティーン")
st.info(f"起きる時間：{wake_time.strftime('%H:%M')}")
st.success(f"入眠時間(眠りに入る)：{sleep_time.strftime('%H:%M')}")
st.warning(f"就寝時間（ベッドに入る）：{bed_time.strftime('%H:%M')}")
st.error(f"作業終了時間：{work_finish_time.strftime('%H:%M')}")

# 改行（大きめ）
st.markdown("---")

# 入力セクションの見出し
st.subheader("⚙️所要時間の設定")