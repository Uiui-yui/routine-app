import streamlit as st
from datetime import datetime, timedelta

st.title("🌙 睡眠ルーティン逆算アプリ")

leaving_time_str = st.time_input("🏠 家を出る時間を入力してください", value=datetime.strptime("08:00", "%H:%M").time())

leaving_datetime = datetime.combine(datetime.today(), leaving_time_str)

wake_up_time = leaving_datetime - timedelta(hours=1)
sleep_time = wake_up_time - timedelta(hours=7, minutes=30)
bed_time = sleep_time - timedelta(minutes=30)
finish_work_time = bed_time - timedelta(hours=2)

st.subheader("⏰ 逆算結果")

st.markdown(f"""
- 🔚 **作業終了時間**：{finish_work_time.strftime('%H:%M')}
- 🛏 **ベッドに入る時間**：{bed_time.strftime('%H:%M')}
- 😴 **入眠時間**：{sleep_time.strftime('%H:%M')}
- ⏰ **起きる時間**：{wake_up_time.strftime('%H:%M')}
- 🚪 **家を出る時間**：{leaving_datetime.strftime('%H:%M')}
""")
