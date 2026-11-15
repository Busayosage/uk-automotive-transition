IF DB_ID(N'uk_automotive') IS NULL
    EXEC(N'CREATE DATABASE uk_automotive;');
GO

USE uk_automotive;
GO

SELECT DB_NAME() AS current_database;