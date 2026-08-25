Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import mysql.connector 
... mydb = mysql.connector.connect( 
... host = "localhost", 
... user="yourusername", 
... password="password", 
... database="mydatabase" 
... ) 
... mycursor=mydb.cursor() 
... create_table_query = ''' 
... CREATE TABLE IF NOT EXISTS items ( 
... id INT AUTO_INCREMENT PRIMARY KEY, 
... item_name VARCHAR(255), 
... description TEXT, 
... quantity1 INT, 
... price1 DECIMAL(10, 2) 
... ) 
... ''' 
... cursor.execute(create_table_query) 
... conn.commit() 
... def add_item(item_name,description,quantity,price): 
... try: 
... insert_query = "INSERT INTO 
... items(item_name,description,quantity1,price1)VALUES(%s,%s,%s,%s)"cursor.execute(inesrt_query,data)
... mydb.commit() 
... print(f"added{item_name}to the inventory.") 
... except mysqlconnector.Error as err: 
... print(f"Error adding item:{err}") 
... def update_item(item_id,new_quantity,new_price): 
... try: 
... update_query="UPDATE items SET quantity1 =%s,price1 =%s WHERE id=%s"data = 
... (new_quantity,new_price,item_id) 
... cursor.execute(update_query,data) 
... mysql.commit() 
... print(f"Updated item with id {item_id}") 
... except mysql.connector.Error as err: 
... print(f"Error updating item  {err}") 
... def track_item(item_id): 
... try: 
... select_query = "SELECT 8 FROM items WHERE id = %s"cursor.execute(select_query,(item_id)) 
... item = cursor.fetchone() 
... if item: 
... else: 
... print("Item details:") 
... print(f"id :{item[0]} \n\ 
... item_name:{item[1]}\n\ 
description:{item[2]}\n\ 
quantity1 :{item[3]}\n\ 
price1:{item[4]}") 
print(f"item with id{item_id} is not found") 
except mysql.connector.Error as err: 
print(f"error retrieving details:{err}") 
add_item("Widget a","small widget", 100,6.83) 
add_item("Widget b", "Large widget",80,13.78) 
update_item(1,90,5.78) 
track_item(1) 
cursor.close() 
