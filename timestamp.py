from datetime import datetime

def show_timestamp():
    now = datetime.now()

    print("\n🕒 Current Time")
    print(f"Date & Time : {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Unix Timestamp: {int(now.timestamp())}")

def convert_timestamp(ts):
    dt = datetime.fromtimestamp(ts)

    print("\n📅 Converted Time")
    print(dt.strftime("%Y-%m-%d %H:%M:%S"))
