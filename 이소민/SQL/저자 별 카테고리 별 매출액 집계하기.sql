-- 코드를 입력하세요
select a.author_id, author_name, category, sum(total_sales)
from author a join 
(select b.book_id, category,author_id, price * sales as total_sales
from book b join (SELECT book_id, sum(sales) as sales from BOOK_SALES 
                    where SALES_DATE like '2022-01%'
                    group by book_id) s 
on b.book_id = s.book_id) bs
on a.author_id = bs.author_id
group by author_id, category
order by 1, 3 desc