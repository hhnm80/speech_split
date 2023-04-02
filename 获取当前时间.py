from datetime import datetime
print(datetime.now())   # 获取当前日期时间
print(datetime.today()) # 获取当前时间
print(datetime.utcnow())    # 获取当前的格林尼治时间

print("我靠"+str(datetime.utcnow()))