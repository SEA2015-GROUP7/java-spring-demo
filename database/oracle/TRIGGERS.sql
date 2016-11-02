--------------------------------------------------------
--  DDL for Trigger ACCOUNT_PK_TRIG
--------------------------------------------------------

  CREATE OR REPLACE TRIGGER "DBUSER"."ACCOUNT_PK_TRIG" 
   before insert on "ACCOUNT" 
   for each row 
begin  
   if inserting then 
      if :NEW."ID" is null then 
         select SPRING_SEQ.nextval into :NEW."ID" from dual; 
      end if; 
   end if; 
end;
ALTER TRIGGER "DBUSER"."ACCOUNT_PK_TRIG" ENABLE
--------------------------------------------------------
--  DDL for Trigger ADDRESS_PK_TRIG
--------------------------------------------------------

  CREATE OR REPLACE TRIGGER "DBUSER"."ADDRESS_PK_TRIG" 
   before insert on "ADDRESS" 
   for each row 
begin  
   if inserting then 
      if :NEW."ID" is null then 
         select SPRING_SEQ.nextval into :NEW."ID" from dual; 
      end if; 
   end if; 
end;
ALTER TRIGGER "DBUSER"."ADDRESS_PK_TRIG" ENABLE
--------------------------------------------------------
--  DDL for Trigger CUSTOMER_PK_TRIG
--------------------------------------------------------

  CREATE OR REPLACE TRIGGER "DBUSER"."CUSTOMER_PK_TRIG" 
   before insert on "CUSTOMER" 
   for each row 
begin  
   if inserting then 
      if :NEW."ID" is null then 
         select SPRING_SEQ.nextval into :NEW."ID" from dual; 
      end if; 
   end if; 
end;
ALTER TRIGGER "DBUSER"."CUSTOMER_PK_TRIG" ENABLE
--------------------------------------------------------
--  DDL for Trigger STATE_TRIGGER
--------------------------------------------------------

  CREATE OR REPLACE TRIGGER "DBUSER"."STATE_TRIGGER" 
   before insert on "STATE" 
   for each row 
begin  
   if inserting then 
      if :NEW."ID" is null then 
         select SPRING_SEQ.nextval into :NEW."ID" from dual; 
      end if; 
   end if; 
end;
ALTER TRIGGER "DBUSER"."STATE_TRIGGER" ENABLE
