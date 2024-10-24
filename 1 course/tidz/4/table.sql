CREATE TABLE Requirements
(	u_num int primary key not null,
	pr_num int,
	s1 float,
	s2 float,
	s3 float,
	s4 float,
	s5 float,
	s6 float,
	s7 float,
	s8 float,
	s9 float,
	s10 float,
	s11 float,
	s12 float,
	s13 float,
	A	float,
	D	float,
	K	float,
	L	float,
	T	float,
	Pa float,
	Pp	float,
	MPp	float,
	LH float);


CREATE TABLE Rules
(	pr_num int primary key not null,
	r1 float, 	
	r2 float, 	
	r3 float, 	
	r4 float, 	
	r5 float, 	
	r6 float, 	
	r7 float, 	
	r8 float, 	
	r9 float,
	r10 float,
	r11 float,
	r12 float,
	r13 float,
	r14 float,
	r15 float,
	r16 float,
	r17 float,
	r18 float,
	r19 float
	);
    


CREATE TABLE Auxiliary
( id int primary key not null,
  G float,
  w1 float,
  w2 float,
  w3 float,
  w4 float,
  w5 float,
  w6 float,
  w7 float,
  NK float,
  RT float);


INSERT INTO Rules VALUES (13, 0.06, 0.40, 0.20, 0.85, 0.70, 0.70, 0.42, 0.70, 0.80, 0.60, 0.40, 0.90, -0.99, -0.15, 0.11, 0.48, 0.58, 0.65, 0.60);
INSERT INTO Requirements VALUES(13, 13, -0.373333388, 0.25, 0.100000001, 0.400000006, 0.5, 0.300000012, 0.25, 0.050000001, -0.600000024, -1, 0.119999997, 0.25, -0.449999988, 1500, 400, 600, 0.5, 0.600000024, 0.400000006, 10, 10, 0.400000006);
INSERT INTO Auxiliary VALUES(13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);


CREATE TABLE Conjectures AS
SELECT G, w1, w2, w3, w4, w5, w6, w7, NK, RT, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, A, D, K, L, T, Pa, Pp, MPp, LH
FROM Auxiliary INNER JOIN Regulations ON id = Rules.pr_num INNER JOIN Requirements ON Rules.pr_num = u_num;


SELECT * from Rules;
SELECT * from Requirements;
SELECT * from Auxiliary;
SELECT * from Conjectures;


UPDATE Conjectures
SET w7 = s12*r9 + s13*r10 - s12*r9*s13*r10;

UPDATE Conjectures
SET w4 = (s6*r7 + w7*r11 - s6*r7*w7*r11) + s7*r8 - s7*r8*(s6*r7 + w7*r11 - s6*r7*w7*r11);

UPDATE Conjectures
SET w5 = (s3*r1 + s4*r1 - s3*r1*s4*r2) + s5*r3 - s5*r3*(s3*r1 + s4*r1 - s3*r1*s4*r2) WHERE Pp <= MPp;

UPDATE Conjectures
SET w5 = s3*r1 + s5*r3 - s5*r3*s3*r1 WHERE Pp > MPp;

UPDATE Conjectures
SET w6 = 0 WHERE (r4 > 0 AND ((s2 > w5 AND s2 < 0) OR (w5 > s2 AND w5 < 0))) OR (r4 < 0 AND ((s2 > w5 AND s2 > 0) OR (w5 > s2 AND w5 > 0)));

UPDATE Conjectures
SET w6 = s2*r4 WHERE (s2 > w5 AND s2 > 0 AND r4 > 0) OR (s2 > w5 AND s2 < 0 AND r4 < 0);

UPDATE Conjectures
SET w6 = w5*r4 WHERE (w5 > s2 AND w5 > 0 AND r4 > 0) OR (w5 > s2 AND w5 < 0 AND r4 < 0);

UPDATE Conjectures
SET w3 = s1*r5 + w6*r6 - s1*r5*w6*r6;

UPDATE Conjectures
SET w1 = w3*r12 + w4*r13 - w3*r12*w4*r13;

UPDATE Conjectures
SET NK = A/K;

UPDATE Conjectures
SET w2 = (s8*r14 + s9*r15 - s8*r14*s9*r15) + s11*r16 - s11*r16*(s8*r14 + s9*r15 - s8*r14*s9*r15) WHERE Pa <= NK AND L >= LH AND ((s11 > 0 AND r16 > 0) OR (s11 < 0 AND r16 < 0));

UPDATE Conjectures
SET w2 = s8*r14 + s11*r16 - s8*r14*s11*r16 WHERE Pa <= NK AND L < LH AND ((s11 > 0 AND r16 > 0) OR (s11 < 0 AND r16 < 0));

UPDATE Conjectures
SET w2 = s8*r14 + s9*r15 - s8*r14*s9*r15 WHERE L >= LH AND ( Pa > NK OR (s11 > 0 AND r16 < 0) OR (s11 > 0 AND r16 < 0));

UPDATE Conjectures
SET RT = D/Pa;

UPDATE Conjectures
SET G = (w1*r18 + w2*r19 - w1*r18*w2*r19) + s10*r17 - s10*r17*(w1*r18 + w2*r19 - w1*r18*w2*r19) WHERE T <= RT AND ((w1 > 0 AND r18 > 0) OR (w1 < 0 AND r18 < 0)) AND ((w2 > 0 AND r19 > 0) OR (w2 < 0 AND r19 < 0));

UPDATE Conjectures
SET G = w1*r18 + w2*r19 - w1*r18*w2*r19 WHERE T > RT AND ((w1 > 0 AND r18 > 0) OR (w1 < 0 AND r18 < 0)) AND ((w2 > 0 AND r19 > 0) OR (w2 < 0 AND r19 < 0));

UPDATE Conjectures
SET G = w1*r18 + s10*r17 - w1*r18*s10*r17 WHERE T <= RT AND ((w1 > 0 AND r18 > 0) OR (w1 < 0 AND r18 < 0)) AND ((w2 > 0 AND r19 < 0) OR (w2 < 0 AND r19 > 0));

UPDATE Conjectures
SET G = w2*r19 + s10*r17 - w2*r19*s10*r17 WHERE T <= RT AND ((w1 > 0 AND r18 < 0) OR (w1 < 0 AND r18 > 0)) AND ((w2 > 0 AND r19 > 0) OR (w2 < 0 AND r19 < 0));

UPDATE Conjectures
SET G = w1*r18 WHERE T > RT AND ((w1 > 0 AND r18 > 0) OR (w1 < 0 AND r18 < 0)) AND ((w2 > 0 AND r19 < 0) OR (w2 < 0 AND r19 > 0));

UPDATE Conjectures
SET G = w2*r19 WHERE T > RT AND ((w1 > 0 AND r18 < 0) OR (w1 < 0 AND r18 > 0)) AND ((w2 > 0 AND r19 > 0) OR (w2 < 0 AND r19 < 0));

UPDATE Conjectures
SET G = s10*r17 WHERE T <= RT AND ((w1 > 0 AND r18 < 0) OR (w1 < 0 AND r18 > 0)) AND ((w2 > 0 AND r19 < 0) OR (w2 < 0 AND r19 > 0));

UPDATE Conjectures
SET G = 0 WHERE T > RT AND ((w1 > 0 AND r18 < 0) OR (w1 < 0 AND r18 > 0)) AND ((w2 > 0 AND r19 < 0) OR (w2 < 0 AND r19 > 0));


SELECT * FROM Conjectures;
