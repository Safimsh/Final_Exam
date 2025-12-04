# قائمة المنتجات (رقم المنتج: [الاسم، السعر])
products = {
    1: ["بطاطس", 5.0],
    2: ["شوكولاتة", 8.0],
    3: ["عصير", 4.5],
    4: ["بسكويت", 3.0],
    5: ["شيبس", 2.5]
}

# عرض المنتجات للمستخدم
print("قائمة المنتجات:")
for number, info in products.items():
    print(f"{number}. {info[0]} - سعره: {info[1]} ريال")

# طلب اختيار المستخدم
choice = int(input("\nيرجى إدخال رقم المنتج الذي ترغب بشرائه: "))

# التحقق من صحة الرقم
if choice not in products:
    print("يرجى إدخال رقم من قائمة المنتجات الظاهرة أمامك فقط")
else:
    name = products[choice][0]
    price = products[choice][1]
    tax = price * 0.15
    total = price + tax

    print(f"\nالمنتج: {name}")
    print(f"السعر شامل الضريبة (15%): {total} ريال")
