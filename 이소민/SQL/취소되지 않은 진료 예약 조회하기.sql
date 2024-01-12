-- 코드를 입력하세요
SELECT ap.APNT_NO, ap.PT_NAME, ap.PT_NO, ap.MCDP_CD, d.DR_NAME, ap.APNT_YMD
from DOCTOR d join 
(select a.APNT_YMD, a.APNT_NO, a.PT_NO, a.MCDP_CD, a.MDDR_ID,a.APNT_CNCL_YN,a.APNT_CNCL_YMD , p.PT_NAME, p.GEND_CD, p.AGE, p.TLNO from APPOINTMENT a join PATIENT p on a.PT_NO = p.PT_NO where APNT_YMD like '2022-04-13%' and MCDP_CD = 'CS' and APNT_CNCL_YN = 'N') ap 
on ap.MDDR_ID = d.DR_ID
order by 6