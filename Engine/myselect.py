from connection import run, run_DataTable
#run ("""drop table Branch""")
'''
run("""create table Branch
(
	branchname varchar(20),
	branchcity varchar(20),
	asset integer,
	check (asset > 0),
	constraint pk_branch primary key(branchname)
);
""")
'''
run("insert into Branch values('SBI','Kolhapur',200);")
run("select * from Branch;")
s = run_DataTable("select * from Branch;")
print("----------")
print(s)
