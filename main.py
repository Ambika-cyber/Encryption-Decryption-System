import eel
from cryptography.fernet import Fernet
import base64
import logging
import traceback
import pymysql
from Crypto.Cipher import AES
import binascii, os
from os import urandom
import mysql.connector
from mysql.connector import Error

# start crypt folder
eel.init("crypt")


iv = urandom(16)
# print("iv",iv)

# AES encryption function
@eel.expose
def AES_encrypt(msg,secretKey):
    # padding
    if(len(msg)!=16):
        result = msg + (16 - len(msg) % 16) * "{"
        msg1 = result
        print(msg1)
        msg2 = bytes(msg1, 'utf-8')
        print(msg2)
        key = secretKey.encode("utf-8")
        print(key)
        private_key = binascii.unhexlify(key)
        print(private_key)
        # For Generating cipher text
        obj = AES.new(private_key, AES.MODE_CBC, iv)
        print(obj)
       
        encrypted_text = obj.encrypt(msg2)
    
        print(encrypted_text)
    else:
        print(msg)
        msg1 = bytes(msg, 'utf-8')
        print(msg1)
        key = secretKey.encode("utf-8")
        print(key)
        private_key = binascii.unhexlify(key)
        print(private_key)
        obj = AES.new(private_key, AES.MODE_CBC, iv)
        print(obj)
       
        encrypted_text = obj.encrypt(msg1)
    
        print(encrypted_text)

    encoded= binascii.hexlify(encrypted_text)
    print("encoded:",encoded)
    data2 = encoded.decode("utf-8")
    print("data2:",data2)
    return data2

# AES decryption function
@eel.expose
def AES_decrypt(encryptedMsg, secretKey):
    print("********************Welcome to Decrytion******************")
    print(encryptedMsg)
    msg =  bytes(encryptedMsg, 'utf-8')
    msg2 = binascii.unhexlify(msg)
    print(msg2)
    key = secretKey.encode("utf-8")
    print(key)
    private_key = binascii.unhexlify(key)
    print(private_key)

    rev_obj = AES.new(private_key, AES.MODE_CBC, iv)
    print(rev_obj)
    plain_text = rev_obj.decrypt(msg2)
    print(plain_text)

    dec = plain_text.decode("utf-8")
    if "{" in dec:
        dec_msg = dec.replace('{','')
        print(dec_msg)
        return dec_msg
    else:
        print("dec text:",dec)
        return dec

   


# generate_key function
@eel.expose
def generate_key():
    secretKey = urandom(16)  # -bit random encryption key
    key= binascii.hexlify(secretKey)
    print("key:",key)
    pk = key.decode("utf-8")
    print("pk:",pk)
    return pk



# sign up function
@eel.expose
def register(name,emailid,passw,CPass):
    if passw!="" and CPass!="":
        if passw == CPass:
            try:
                connection = mysql.connector.connect(host='localhost',database='edcrypt',user='root',password='')
                if connection.is_connected():
                    db_Info = connection.get_server_info()
                    print("Connected to MySQL Server version ", db_Info)
                    cursor = connection.cursor()
                    sql = "INSERT INTO register (Name,EmailId,Password,ConfirmPassword) VALUES (%s, %s,%s,%s)"
                    val = (name, emailid,passw,CPass)
                    cursor.execute(sql, val)

                    connection.commit()
            
                    print("sign up done")
                    return "1"
                    # sql_select_Query = "insert into register values()" 
                    # cursor.execute(sql_select_Query ,[(user),(passw)])
            except Error as e:
                return "2"       
        else:
            print("please enter password and confirm password same")
            return "0"


# login function
@eel.expose
def login(user,passw):

    try:
        connection = mysql.connector.connect(host='localhost',database='edcrypt',user='root',password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            # cursor.execute("select database();")
            # record = cursor.fetchone()
            # print("You're connected to database: ", record)
    
            sql_select_Query = "select * from Register where emailid= %s and Password = %s" 
            cursor.execute(sql_select_Query ,[(user),(passw)])
            records = cursor.fetchall()
            if records:
        
                print("\nPrinting each row")
                for row in records:
                    print("Name = ", row[0], )
                    print("Email = ", row[1])
                    print("Pass  = ", row[2])
                    print("CPass  = ", row[3], "\n")
                print("LOGIN SUCCESSFULLY")
                return(1)
            else:
                print("enter valid username and password")
                return(0)

    except Error as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



@eel.expose
def image_encrypt(path,k):
	# try block to handle exception
	try:
		key = int(k)
		print('The path of file : ', path)
		print('Key for encryption : ', key)
	
		# open file for reading purpose
		fin = open(path, 'rb')
	
		# storing image data in variable "image"
		image = fin.read()
		fin.close()
	
		# converting image into byte array to
		# perform encryption easily on numeric data
		image = bytearray(image)

		# performing XOR operation on each value of bytearray
		for index, values in enumerate(image):
			image[index] = values ^ key

		# opening file for writing purpose
		fin = open(path, 'wb')
	
		# writing encrypted data in image
		fin.write(image)
		fin.close()
		print('Encryption Done...')
	except Exception:
		print('Error caught : ', Exception.__name__)



@eel.expose
def image_decrypt(path,k):
	# try block to handle exception
	try:
		key = int(k)
		print('The path of file : ', path)
		print('Key for decryption : ', key)
	
		# open file for reading purpose
		fin = open(path, 'rb')
	
		# storing image data in variable "image"
		image = fin.read()
		fin.close()
	
		# converting image into byte array to
		# perform encryption easily on numeric data
		image = bytearray(image)

		# performing XOR operation on each value of bytearray
		for index, values in enumerate(image):
			image[index] = values ^ key

		# opening file for writing purpose
		fin = open(path, 'wb')
	
		# writing encrypted data in image
		fin.write(image)
		fin.close()
		print('Decryption Done...')
	except Exception:
		print('Error caught : ', Exception.__name__)


# # contact from
@eel.expose
def contact_form(name,email,msg):
    try:
        connection = mysql.connector.connect(host='localhost',database='edcrypt',user='root',password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            sql = "INSERT INTO contact (Name,EmailId,Message) VALUES (%s, %s,%s)"
            val = (name, email,msg)
            cursor.execute(sql, val)

            connection.commit()
            print("form submitted successfully!")
    except Error as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


eel.start("index.html")
            # ============================================================================
