import mysql.connector


class ProductManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password="Arya@181094",
            database="shop_db"
        )
        print("Db Connected Succesfully...")

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = "insert into product(name, category, price, quantity, manufacturer) values (%s, %s, %s, %s, %s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Product added Successfully..")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from product"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            for data in record:
                print(data)
        except Exception as e:
            print(e)


    def get_object(self,id = None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from product where id = %s"
            values = (id, )
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def retrieve(self, id = None):
        try:
            record = self.get_object(id =id)
            if record == None:
                print("Product Not Found...")
            print(record)
        except Exception as e:
            print(e)

    def put(self,id = None, **kwargs):
        try:
            record = self.get_object(id = id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder = " "
                for k in kwargs.keys():
                    placeholder += k + "%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update product set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Product Updated...")
            else:
                print("Product Not Found")
        except Exception as e:
            print(e)

    def delete(self, id = None):
        try:
            record = self.get_object(id = id)
            if record != None:
                query = "delete from product where id = %s"
                self.cursor.execute(query)
                self.connection.commit()
                print("Product Deleted...")
            else:
                print("Product Not Found")
        except Exception as e:
            print(e)






product_instance = ProductManager()
#product_instance.post(name="Color",category="Stationary", price=150, quantity= 10,manufacturer ="Camel")
#product_instance.get()
#product_instance.retrieve(2)
#product_instance.put(2)
product_instance.delete(1)
