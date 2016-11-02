--------------------------------------------------------
--  DDL for Table ACCOUNT
--------------------------------------------------------

  CREATE TABLE "DBUSER"."ACCOUNT" 
   (	"ID" NUMBER, 
	"CUSTOMER_ID" NUMBER, 
	"ACCOUNT_TYPE" VARCHAR2(20 BYTE), 
	"ACCOUNT_NUMBER" VARCHAR2(20 BYTE)
   )
--------------------------------------------------------
--  DDL for Table ADDRESS
--------------------------------------------------------

  CREATE TABLE "DBUSER"."ADDRESS" 
   (	"ID" NUMBER, 
	"ADDRESS_TYPE" VARCHAR2(20 BYTE), 
	"PRIMARY_ADDRESS_LINE" VARCHAR2(80 BYTE), 
	"SECONDARY_ADDRESS_LINE" VARCHAR2(80 BYTE), 
	"CITY_NAME" VARCHAR2(50 BYTE), 
	"STATE_ID" NUMBER, 
	"ZIP_CODE" VARCHAR2(10 BYTE), 
	"CUSTOMER_ID" NUMBER
   )
--------------------------------------------------------
--  DDL for Table COUNTRY
--------------------------------------------------------

  CREATE TABLE "DBUSER"."COUNTRY" 
   (	"ID" NUMBER, 
	"NAME" VARCHAR2(30 BYTE), 
	"CODE" VARCHAR2(3 BYTE)
   )
--------------------------------------------------------
--  DDL for Table STATE
--------------------------------------------------------

  CREATE TABLE "DBUSER"."STATE" 
   (	"ID" NUMBER, 
	"NAME" VARCHAR2(30 BYTE), 
	"CODE" VARCHAR2(2 BYTE), 
	"COUNTRY_ID" NUMBER
   )
