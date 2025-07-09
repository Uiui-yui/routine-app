import streamlit as st
import datetime

st.set_page_config(page_title="ルーティン計算アプリ", page_icon="🛌")

st.title("睡眠ルーティーン逆算アプリ")

# 入力：家を出たい時間
leave_time = st.time_input("家を出たい時間を入力してください", value=datetime.time(8, 0))

# 時刻計算に必要な所要時間（すべて時間＋分）
st.markdown("---")

st.subheader("所要時間の設定")

wake_h = st.number_input("起床〜家を出るまで：時間", min_value=0, max_value=12, value=1)
wake_m = st.number_input("起床〜家を出るまで：分", min_value=0, max_value=59, value=0)

sleep_h = st.number_input("入眠〜起床：時間", min_value=0, max_value=12, value=7)
sleep_m = st.number_input("入眠〜起床：分", min_value=0, max_value=59, value=30)

bed_h = st.number_input("就寝〜入眠：時間", min_value=0, max_value=3, value=0)
bed_m = st.number_input("就寝〜入眠：分", min_value=0, max_value=59, value=30)

work_h = st.number_input("作業終了〜就寝：時間", min_value=0, max_value=6, value=2)
work_m = st.number_input("作業終了〜就寝：分", min_value=0, max_value=59, value=0)

# 分単位に変換
wake_to_leave = wake_h * 60 + wake_m
sleep_duration = sleep_h * 60 + sleep_m
bed_to_sleep = bed_h * 60 + bed_m
work_to_bed = work_h * 60 + work_m

# 時刻の逆算計算
leave_dt = datetime.datetime.combine(datetime.date.today(), leave_time)
wake_time = leave_dt - datetime.timedelta(minutes=wake_to_leave)
sleep_time = wake_time - datetime.timedelta(minutes=sleep_duration)
bed_time = sleep_time - datetime.timedelta(minutes=bed_to_sleep)
work_finish_time = bed_time - datetime.timedelta(minutes=work_to_bed)

# 結果表示（順番を修正済み、すべて時刻表示に統一）
st.subheader("今日のルーティーン")
st.error(f"作業終了時間：{work_finish_time.strftime('%H:%M')}")
st.warning(f"就寝時間：{bed_time.strftime('%H:%M')}")
st.success(f"入眠時間：{sleep_time.strftime('%H:%M')}")
st.info(f"起きる時間：{wake_time.strftime('%H:%M')}")