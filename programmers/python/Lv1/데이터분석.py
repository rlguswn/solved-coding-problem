# 6시42분

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]] # 코드번호, 제조일(연월일), 최대수량, 현재수량
ext = "date" # 뽑아낼 정보의 기준
val_ext = 20300501 # 뽑아낼 정보의 기준값(기준보다 작은 데이터만 추출)
sort_by = "remain" # 정렬 기준

def solution(data, ext, val_ext, sort_by):
    criteria = {"code":0, "date":1, "maximum":2, "remain":3}
    answer = [value for value in data if value[criteria[ext]] < val_ext]
    answer.sort(key = lambda x:x[criteria[sort_by]])

    return answer

print(solution(data, ext, val_ext, sort_by))