def flip(some_list):
    # 코드를 입력하세요.
    item = some_list[:1]
    if len(some_list) < 2:
        return some_list
    return flip(some_list[1:]) + item

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
