SHOW TABLES LIKE 'your_table_name';

SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_SCHEMA = 'your_database_name' 
AND TABLE_NAME = 'your_table_name';

SELECT EXISTS (
    SELECT 1 
    FROM information_schema.tables 
    WHERE table_name = 'your_table_name'
);

IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'your_table_name')
    PRINT 'Table exists';
ELSE
    PRINT 'Table does not exist';

SELECT name 
FROM sqlite_master 
WHERE type='table' AND name='your_table_name';

