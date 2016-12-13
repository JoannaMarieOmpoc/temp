CREATE TABLE topemployee(
  employeeID int8 PRIMARY KEY,
  employeename text,
  gender text,
  salary text,
  address text
  )

AS BEGIN
  IF @StatementType = 'Insert'
  BEGIN
  insert into employee(employeeID, employeename, gender, salary, address) values(@employeeID, @employeename, @gender, @salary, @address)
  END

  IF @StatementType = 'Update'
  BEGIN

  UPDATE employee
    SET
      employeename =  @employeename,
      gender = @gender,
      salary = @salary,
      address = @address,
    WHERE employeeID = @employeeID
  END
end

CREATE TABLE votecount(employeeID int PRIMARY KEY, years text)

CREATE OR REPLACE FUNCTION getvote(out int, out text) RETURNS SETOF RECORDS as
$$
   select ((select count(topemployee.employeeID) from topemployee)*count(years)) from votecount;

$$
 language 'sql';

AS BEGIN
  IF @StatementType = 'Insert'
  BEGIN
  insert into votecount(employeeID, years) values(@employeeID, @years)
  END
end