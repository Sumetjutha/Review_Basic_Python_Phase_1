### Assignment 10 : หาผลรวมตัวเลข (ปรับเงื่อนไข)

##################################################################################
'''

'''
# จะออกจาก loop เมื่อมันเป็น false
sum = 0

while sum!=100:
    number = int(input("ป้อนตัวเลขของคุณ : "))
    sum+=number # บวกเลขที่ป้อนไปในแต่ละรอบ
    print("ผลรวม = ",sum)

print("End")
##################################################################################

##################################################################################
sum_1 = 0

while sum_1<100:
    number = int(input("ป้อนตัวเลขของคุณ : "))
    sum_1+=number # บวกเลขที่ป้อนไปในแต่ละรอบ
    print("ผลรวม = ",sum_1)
    ## จะออกจาก loop เมื่อมันเป็น false

print("End")
##################################################################################

##################################################################################
sum_1 = 0

while True:
    number = int(input("ป้อนตัวเลขของคุณ : "))
    sum_1+=number # บวกเลขที่ป้อนไปในแต่ละรอบ
    if sum_1>=100:
        break
    print("ผลรวม = ",sum_1)
    ## จะออกจาก loop เมื่อมันเป็น false

print("End")
##################################################################################