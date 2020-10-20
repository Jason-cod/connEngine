from connection import run, run_DataTable
run ("""DROP TABLE IF EXISTS customers3""")
print("----------1")
run("CREATE TABLE customers3 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
print("----------2")
run("INSERT INTO customers3 (name, address) VALUES ('CBI','Kolhapur')")
run("INSERT INTO customers3 (name, address) VALUES ('SBI','Kolhapur');")
print("----------3")
run("SELECT * FROM customers3")
print("----------4")
s = run_DataTable("SELECT * FROM customers3")
print("----------5")
print(s)
run("delete customers3")
run("INSERT INTO customers3 (name, address) VALUES ('Boi','Panvel');")
