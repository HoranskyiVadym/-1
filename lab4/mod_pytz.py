import pytz
from datetime import datetime

def test_pytz():
    kyiv_tz = pytz.timezone("Europe/Kyiv")
    kyiv_time = datetime.now(kyiv_tz)
    print(f"[Pytz] Поточний час у Києві: {kyiv_time.strftime('%Y-%m-%d %H:%M:%S')}")