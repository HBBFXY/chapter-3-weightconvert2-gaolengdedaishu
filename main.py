# 在这个文件里编写代码
# 假设当前在地球上的体重（千克）
initial_weight = 60
# 每年体重增长（千克）
yearly_gain = 0.5
# 月球上体重是地球上的比例
moon_ratio = 0.165

print("未来10年地球和月球上的体重变化：")
for year in range(1, 11):
    # 计算地球上当年的体重
    earth_weight = initial_weight + yearly_gain * year
    # 计算月球上当年的体重
    moon_weight = earth_weight * moon_ratio
    print(f"第{year}年：地球上体重 {earth_weight:.2f}kg，月球上体重 {moon_weight:.2f}kg")
