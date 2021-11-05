/*
 SQL for survey exacts database
*/


drop table if exists labels;
drop table if exists answers3;
drop table if exists surveys;


CREATE TABLE surveys (
	id INTEGER NOT NULL,
	name VARCHAR(255),
	PRIMARY KEY (id)
);

CREATE TABLE answers3 (
	answer_id INTEGER NOT NULL,
	survey INTEGER,
	respondentid INTEGER,
	organization INTEGER,
	statinternal_1 INTEGER,
	statinternal_2 INTEGER,
	statinternal_3 INTEGER,
	statinternal_4 INTEGER,
	statinternal_5 INTEGER,
	statinternal_6 INTEGER,
	statinternal_7 INTEGER,
	statinternal_8 INTEGER,
	statinternal_9 INTEGER,
	statinternal_10 INTEGER,
	statinternal_11 INTEGER,
	statinternal_12 INTEGER,
	statinternal_13 INTEGER,
	statinternal_14 INTEGER,
	statinternal_15 INTEGER,
	statinternal_16 INTEGER,
	statinternal_17 INTEGER,
	statinternal_18 INTEGER,
	statinternal_19 INTEGER,
	statinternal_20 INTEGER,
	created TIMESTAMP,
	modified TIMESTAMP,
	closetime TIMESTAMP,
	starttime TIMESTAMP,
	difftime NUMERIC,
	responsecollectsessions INTEGER,
	numberofreturnedmail INTEGER,
	importgroup INTEGER,
	distributionschedule VARCHAR,
	email VARCHAR,
	digitaldistributionstatus VARCHAR,
	digitaldistributionerrormessage VARCHAR,
	risikovurdering INTEGER,
	anbefalinger INTEGER,
	hast_revurdering INTEGER,
	nyviden INTEGER,
	opmaerksomhedsniveau INTEGER,
	overhold_fremover INTEGER,
	andrebilister INTEGER,
	uddyb_evaluering TEXTrm ,
	situation1 INTEGER,
	strategi1 INTEGER,
	situation2 INTEGER,
	strategi2 INTEGER,
	situation3 INTEGER,
	strategi3 INTEGER,
	strategi_tekstfelt TEXT,
	strategimail INTEGER,
	strategireminder INTEGER,
	email_strategi VARCHAR(255),
	slutkommentar_1b TEXT,
	id VARCHAR(50),
	gr VARCHAR(1),
	s INTEGER,
	statcompletion_1 INTEGER,
	statcompletion_2 INTEGER,
	statcompletion_3 INTEGER,
	statcreation_1 INTEGER,
	statcreation_2 INTEGER,
	statcreation_3 INTEGER,
	statcreation_4 INTEGER,
	statcreation_5 INTEGER,
	statcreation_6 INTEGER,
	statcreation_7 INTEGER,
	statdistribution_1 INTEGER,
	statdistribution_2 INTEGER,
	statdistribution_3 INTEGER,
	statdistribution_4 INTEGER,
	statdistribution_5 INTEGER,
	statsource_1 INTEGER,
	statsource_2 INTEGER,
	statsource_3 INTEGER,
	statsource_4 INTEGER,
	statsource_5 INTEGER,
	statsource_6 INTEGER,
	statcollect_1 INTEGER,
	statcollect_2 INTEGER,
	statcollect_3 INTEGER,
	statcollect_4 INTEGER,
	statoverall_1 INTEGER,
	statoverall_2 INTEGER,
	statoverall_3 INTEGER,
	statoverall_4 INTEGER,
	statoverall_5 INTEGER,
	strategi_mail_send_first TIMESTAMP,
	strategi_mail_send_first_failed TIMESTAMP,
	strategi_mail_send_second TIMESTAMP,
	strategi_mail_send_second_failed TIMESTAMP,
	PRIMARY KEY (answer_id),
	FOREIGN KEY(survey) REFERENCES surveys (id)
);


CREATE TABLE labels (
	id INTEGER NOT NULL,
	organization INTEGER,
	survey_id INTEGER,
	field_name VARCHAR NOT NULL,
	field_value INTEGER NOT NULL,
	field_text VARCHAR(255) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE (field_name, field_value),
	FOREIGN KEY(survey_id) REFERENCES surveys (id)
);



/*
create view strategi_mailings
as
SELECT
respondentid,
julianday(datetime('now'))-julianday(closetime) as days_since,
closetime,
datetime('now') as today,
l1.field_text as situation1_text,
l2.field_text as situation2_text,
l3.field_text as situation3_text,
ls1.field_text as strategi1_text,
ls2.field_text as strategi2_text,
ls3.field_text as strategi3_text,
 email_strategi
from
answers3 a
LEFT JOIN labels l1 on (a.situation1 = l1.field_value and l1.field_name = 'situation1')
LEFT JOIN labels l2 on (a.situation2 = l2.field_value and l2.field_name = 'situation2')
LEFT JOIN labels l3 on (a.situation3 = l3.field_value and l3.field_name = 'situation3')
LEFT JOIN labels ls1 on (a.strategi1 = ls1.field_value and ls1.field_name = 'strategi1')
LEFT JOIN labels ls2 on (a.strategi2 = ls2.field_value and ls2.field_name = 'strategi2')
LEFT JOIN labels ls3 on (a.strategi3 = ls3.field_value and ls3.field_name = 'strategi3')
where
strategimail = 1 AND
strategireminder = 1 AND
strategi_mail_send_first is null






-- Succes fuld udsending ved første
UPDATE answer3 set strategi_mail_send_first = datetime('now') WHERE respondentid = {respondentid}

-- Ved fejl udsending, indsæt seneste forsøgte dato
UPDATE answer3 set strategi_mail_send_first_failed = datetime('now') WHERE respondentid = {respondentid}

-- Success for udsending ved anden
UPDATE answer3 set strategi_mail_send_second = datetime('now') WHERE respondentid = {respondentid}

-- Ved fejl udsending, indsæt seneste forsøgte dato
UPDATE answer3 set strategi_mail_send_second_failed = datetime('now') WHERE respondentid = {respondentid}

select * from strategi_mailings

select * from strategi_mailings

sit 2 Når en bagvedkørende trafikant presser mig

*/