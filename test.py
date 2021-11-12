import pyupbit

access = "8ixfm7xHrFYFWlExV7DcbN2WmLHW7x1cabFqGrxI"          # 본인 값으로 변경
secret = "p6mxG8wBJ2oDtj34Ig7AjB5en7TbTfO7qe4i9B0O"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-AXS"))     # KRW-AXS 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회