def is_leap_year(Y):
    if Y % 4 == 0 and Y % 100 != 0:
        return True
    elif Y % 4 == 0 and Y % 400 == 0:
        return True
    return False

def is_validate(Y:int, M:int, D: int) -> bool:
    leap_year = is_leap_year(Y)
    is_validate = True  

    # 30일 이하인 달 확인
    if M == 2:
        if leap_year and D > 29:
            return False
        elif not leap_year and D > 28:
            return False
    if M in(4, 6, 9, 11) and D == 31:
        return False

    return True

Y, M, D = map(int, input().split())
if is_validate(Y, M, D):
    if M in (3, 4, 5):
        print("Spring")
    elif M in (6, 7, 8):
        print("Summer")
    elif M in (9, 10, 11):
        print("Fall")
    else:
        print("Winter")
else:
    print(-1)