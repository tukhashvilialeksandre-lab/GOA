age = int(input("whrite your age"))
has_ticket = input("gaqvs bileti? ki/ara")

if age >= 16 and has_ticket == "ki":
    print("shegizliat gonisziebaze shesvla")
if age < 16 or has_ticket != "ki":
    print("gonisziebaze shesvla akrzalulia")