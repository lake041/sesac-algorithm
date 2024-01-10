
select to_char(sales_date, 'yyyy'),
    concat( replace(substr(to_char(sales_date, 'MM'),0,1), '0', '') ,substr(to_char(sales_date, 'MM'),2)),
    COUNT(distinct(user_id)), 
    round(COUNT(distinct(user_id))/ (select count(user_id)
                                    from user_info
                                    where to_char(joined, 'yyyy') = '2021'), 1)
from online_sale
where user_id in
        (select user_id
        from user_info
        where to_char(joined, 'yyyy') = '2021')
group by to_char(sales_date, 'yyyy'), to_char(sales_date, 'MM')
order by to_char(sales_date, 'yyyy'),substr(to_char(sales_date, 'MM'),2)


SELECT TO_CHAR(SALES_DATE, 'YYYY') AS YEAR
, TO_NUMBER(TO_CHAR(SALES_DATE, 'MM')) AS MONTH
, COUNT(DISTINCT(USER_ID)) AS PUCHASED_USERS
, ROUND(COUNT(DISTINCT(USER_ID)) / (SELECT COUNT(USER_ID)
                                    FROM USER_INFO 
                                    WHERE TO_CHAR(JOINED, 'YYYY') = '2021'), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE
WHERE USER_ID IN (SELECT USER_ID
                  FROM USER_INFO 
                  WHERE TO_CHAR(JOINED, 'YYYY') = '2021')
GROUP BY TO_CHAR(SALES_DATE, 'YYYY') , TO_CHAR(SALES_DATE, 'MM')
ORDER BY YEAR, MONTH;