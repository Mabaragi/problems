-- 코드를 입력하세요
# 환자이름 ,번호, 성별, 나이, 전화번호를 조회 
# 12세 이하인 여자
# 정렬 : 나이 내림차순, 이름 오름차순
# 전화번호가 없는경우 'NONE'으로 출력
# ALTER TLNO SET DEFAULT 'NONE';
SELECT PT_NAME
, PT_NO
, GEND_CD
, AGE
, ifnull(TLNO,'NONE') AS TLNO 
from PATIENT 
where AGE <= 12 and GEND_CD in ('W') 
order by AGE desc, PT_NAME;