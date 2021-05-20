import pyupbit

access = "kMmjoM9SK71NxDmltgq3QYrRsMZTfxrRmeu3aXmW"          # 본인 값으로 변경
secret = "PFZ8OdknpdpamKHrJCiqXZbkweZJnMQ3Mx82zRJy"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

print(pyupbit.get_tickers())
