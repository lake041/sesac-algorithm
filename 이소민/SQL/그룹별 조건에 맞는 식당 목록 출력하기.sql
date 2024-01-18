select m.member_name, r.review_text, date_format(r.review_date, '%Y-%m-%d')
from member_profile m join rest_review r on m.member_id = r.member_id
where m.member_id in 
(select member_id from (select count(*) as num, member_id from rest_review group by member_id) as m_num where num = (select max(num) from (select count(*) as num, member_id from rest_review group by member_id) as m_num))
order by r.review_date, r.review_text