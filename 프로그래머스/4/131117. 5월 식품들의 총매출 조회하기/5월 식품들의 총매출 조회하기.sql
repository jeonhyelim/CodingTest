-- 코드를 입력하세요
SELECT O.PRODUCT_ID, P.PRODUCT_NAME, SUM(O.AMOUNT * P.PRICE) AS TOTAL_SALES

FROM FOOD_PRODUCT AS P
JOIN FOOD_ORDER AS O ON P.PRODUCT_ID = O.PRODUCT_ID

WHERE O.PRODUCE_DATE LIKE '2022-05%'
GROUP BY PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID
