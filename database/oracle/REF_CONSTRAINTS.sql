--------------------------------------------------------
--  Ref Constraints for Table ADDRESS
--------------------------------------------------------

  ALTER TABLE "DBUSER"."ADDRESS" ADD CONSTRAINT "ADDRESS_CUST_FK2" FOREIGN KEY ("CUSTOMER_ID")
	  REFERENCES "DBUSER"."CUSTOMER" ("ID") ENABLE
  ALTER TABLE "DBUSER"."ADDRESS" ADD CONSTRAINT "ADDRESS_STATE_FK1" FOREIGN KEY ("STATE_ID")
	  REFERENCES "DBUSER"."STATE" ("ID") ENABLE
--------------------------------------------------------
--  Ref Constraints for Table STATE
--------------------------------------------------------

  ALTER TABLE "DBUSER"."STATE" ADD CONSTRAINT "STATE_COUNTRY_FK1" FOREIGN KEY ("COUNTRY_ID")
	  REFERENCES "DBUSER"."COUNTRY" ("ID") ENABLE
