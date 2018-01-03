# encoding: UTF-8
"""交易时间设置"""

# key: 合约前缀
# value: ["开盘时间", "收盘时间"]
TRADING_TIME = {
    "T":  ["09:15:00", "15:15:00"],  # 十年国债
    "rb": ["21:00:00", "15:00:00"],  # 螺纹钢
    "j":  ["21:00:00", "15:00:00"],  # 焦炭
    "hc": ["21:00:00", "15:00:00"]   # 热卷
}

# wind会推数据的无效时间
ERROR_TIME = {
    "rb": [("23:00:00", "23:59:00"), ("00:00:00", "03:00:00")],
    "j":  [("23:30:00", "23:59:00"), ("00:00:00", "03:00:00")],
    "hc": [("23:00:00", "23:59:00"), ("00:00:00", "03:00:00")],
}