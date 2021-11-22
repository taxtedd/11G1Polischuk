UPDATE users SET registration_date = SUBSTR(registration_date, 7, 4) || '-' || SUBSTR(registration_date, 4, 2) || '-' ||SUBSTR(registration_date, 1, 2);

SELECT email,registration_date AS 'Registration date' FROM users
WHERE registration_date IN (SELECT max(registration_date) FROM users);

SELECT SUBSTR(birth_date, 1, 4)  AS 'Birth date' FROM users GROUP BY SUBSTR(birth_date, 1, 4);

SELECT  COUNT(*)  AS 'Total items' FROM products;

SELECT ((SUBSTR(CURRENT_DATE,1,4)-SUBSTR(birth_date,1,4))-(SUBSTR(CURRENT_DATE,6,5)<SUBSTR(birth_date,6,5))) AS 'Age' FROM users;

SELECT AVG((SUBSTR(CURRENT_DATE,1,4)-SUBSTR(birth_date,1,4))-(SUBSTR(CURRENT_DATE,6,5)<SUBSTR(birth_date,6,5))) AS 'Age' FROM users
WHERE SUBSTR(registration_date,9,2)<=SUBSTR(CURRENT_DATE,9,2) AND ((SUBSTR(CURRENT_DATE,1,4)-SUBSTR(registration_date,1,4))*12+(SUBSTR(CURRENT_DATE,6,2)-SUBSTR(registration_date,6,2)))<=2 OR
SUBSTR(registration_date,9,2)>SUBSTR(CURRENT_DATE,9,2) AND ((SUBSTR(CURRENT_DATE,1,4)-SUBSTR(registration_date,1,4))*12+(SUBSTR(CURRENT_DATE,6,2)-SUBSTR(registration_date,6,2)))<=3;