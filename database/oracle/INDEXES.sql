--------------------------------------------------------
--  DDL for Index ACCOUNT_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "DBUSER"."ACCOUNT_PK" ON "DBUSER"."ACCOUNT" ("ID")
--------------------------------------------------------
--  DDL for Index ACCOUNT_UK1
--------------------------------------------------------

  CREATE UNIQUE INDEX "DBUSER"."ACCOUNT_UK1" ON "DBUSER"."ACCOUNT" ("ACCOUNT_NUMBER")
--------------------------------------------------------
--  DDL for Index ADDRESS_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "DBUSER"."ADDRESS_PK" ON "DBUSER"."ADDRESS" ("ID")
--------------------------------------------------------
--  DDL for Index ADDRESS_UK1
--------------------------------------------------------

  CREATE UNIQUE INDEX "DBUSER"."ADDRESS_UK1" ON "DBUSER"."ADDRESS" ("ADDRESS_TYPE", "CUSTOMER_ID")
--------------------------------------------------------
--  DDL for Index CUSTOMER_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "DBUSER"."CUSTOMER_PK" ON "DBUSER"."CUSTOMER" ("ID")
--------------------------------------------------------
--  DDL for Index CUSTOMER_UK1
--------------------------------------------------------

  CREATE UNIQUE INDEX "DBUSER"."CUSTOMER_UK1" ON "DBUSER"."CUSTOMER" ("USER_NAME")
--------------------------------------------------------
--  DDL for Index STATE_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "DBUSER"."STATE_PK" ON "DBUSER"."STATE" ("ID")
--------------------------------------------------------
--  DDL for Index COUNTRY_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "DBUSER"."COUNTRY_PK" ON "DBUSER"."COUNTRY" ("ID")
