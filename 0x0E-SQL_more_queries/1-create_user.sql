-- creates the MySQL server user user_0d_1
--	user_0d_1 should have all privileges on your MySQL server
CREATE USER IF NOT EXISTS user_0d_1
   IDENTIFIED BY "user_0d_1_pwd";
GRANT ALL ON *.* TO user_0d_1@localhost;
