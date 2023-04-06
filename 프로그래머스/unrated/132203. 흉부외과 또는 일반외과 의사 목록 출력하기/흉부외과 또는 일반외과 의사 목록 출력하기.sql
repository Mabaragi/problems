-- 코드를 입력하세요

# 이름 ,id 진료과, 고용일자
# 고용일자 내림차순 이름 오름차순
# cs이거나 gs인


SELECT DR_NAME, DR_ID, MCDP_CD, SUBSTRING(HIRE_YMD,1, 10) from DOCTOR where MCDP_CD in ('CS', 'GS') order by HIRE_YMD desc, DR_NAME