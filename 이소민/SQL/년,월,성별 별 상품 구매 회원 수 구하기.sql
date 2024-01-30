-- 코드를 입력하세요
select year(SALES_DATE) as year, month(SALES_DATE) as month, gender, count(distinct(o.user_id)) as users
from USER_INFO u join ONLINE_SALE o
on u.USER_ID = o.USER_ID
where u.GENDER is not null
group by month, gender
order by 1,2,3