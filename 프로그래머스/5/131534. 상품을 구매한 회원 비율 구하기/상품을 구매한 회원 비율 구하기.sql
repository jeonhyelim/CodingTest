SELECT 
    YEAR(SALES_DATE) AS "YEAR",
    MONTH(SALES_DATE) AS "MONTH",
    COUNT(DISTINCT USER_ID) AS "PURCHASED_USERS", #중복되지않은 user_id 수
    ROUND(
          COUNT(DISTINCT USER_ID) / (SELECT COUNT(*) 
                                      FROM USER_INFO
                                      WHERE YEAR(JOINED) = 2021) 
          , 1) AS "PURCHASED_RATIO" 
FROM ONLINE_SALE
WHERE USER_ID IN (SELECT USER_ID
                  FROM USER_INFO
                  WHERE YEAR(JOINED) = 2021)
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;