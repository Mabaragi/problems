-- 코드를 입력하세요
# chocolate vanilla mint_chocolate caramel white_chocolate peach strawberry
SELECT FLAVOR from FIRST_HALF where FLAVOR in ('peach', 'watermelon', 'mango', 'strawberry', 'melon', 'orange', 'pineapple') and TOTAL_ORDER > 3000 order by TOTAL_ORDER desc;