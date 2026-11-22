price = float(input("sheiyvanet productis fasi"))
is_member = input("xar klubis wevri? ki/ara ")

if price > 100 or is_member == "ki":
    print("tqven gekutvnit fasdakleba!")
if price <= 100 and is_member != "ki":
    print("tqven fasdaklebva ar gekutvnit")