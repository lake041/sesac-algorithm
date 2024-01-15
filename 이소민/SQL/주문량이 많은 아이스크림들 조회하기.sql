-- 코드를 입력하세요
SELECT f.flavor
from FIRST_HALF f join (select flavor, sum(total_order) as total_order from july group by flavor) j
on f.FLAVOR = j.FLAVOR
group by flavor
order by sum(f.total_order+j.total_order) desc limit 3