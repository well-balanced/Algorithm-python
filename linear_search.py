"""
element in some_list와 같이 in 키워드를 사용하는 건 안 됩니다. 선형 탐색에 대한 이해를 테스트하는 과제이기 때문에, 반드시 반복문을 사용해서 해결해 주셔야 합니다.
자동 채점 과제이기 때문에, 문제의 조건에 정확히 따라주시기 바랍니다. 띄어쓰기도 일치해야 합니다.
힌트를 최대한 보지 않고, 스스로의 힘으로 푸시는 것이 좋습니다. 만약 도저히 모르겠다면, 최소한의 힌트만 참고해주세요!
"""
def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
    return None

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
