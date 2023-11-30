def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        if city.lower() in cache:
            answer+=1
            cache.remove(city.lower())
            cache.append(city.lower())
        else:
            answer+=5
            if len(cache) <cacheSize:
                cache.append(city.lower())
            else:
                cache.append(city.lower())
                cache.pop(0)
    return answer

# 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
# cache hit일 경우 실행시간은 1이다.
# cache miss일 경우 실행시간은 5이다.

# Cache Hit : CPU 가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우
# Cache Miss : CPU 가 참조하고자 하는 메모리가 캐시에 존재하지 않을 경우

cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(	3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))