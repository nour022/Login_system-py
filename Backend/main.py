import re, base64, pandas
from cryptography.fernet import Fernet

class LoginSystem:

	def __init__(self):
		self.key = b'Gp-vK0y-SH1c9XkTgT_fjM58H68tQchE7VWw2Y1J7Vw='
		self.fullname = input("Enter Yout Full Name: ")
		
		# ckek fung to serach on username if True
		self.username = input("Enter Your Username: ")
		while self.check_username(self.username):
			print("This username is olrady exeitet")
			self.username = input("Enter Your Username: ")
		
		# Password checking
		self.passwd = input('Enter your Password: ')
		while self.check_passwoed(self.passwd,self.key):
			self.passwd = input('Enter your Password: ')
		
		self.passwdag = input("Enter the password agein: ")
		while self.decode_password(self.passwd,self.key) != self.passwdag:
			print("The password is incurret")
			self.passwdag = input("Enter the password agein: ")
		
		self.mail = input("Enter Your Email: ")
		while self.check_email(self.mail):
			self.mail = input("Enter Your Email: ")
	def save_data(self):
		new_data = {"email": self.mail, "FullName": self.fullname,
		            "Username": self.username, "Password": self.passwd}
		try:
			df = pandas.read_csv("login.csv")
		except FileNotFoundError:
			df = pandas.DataFrame([new_data])
			df.to_csv("login.csv", index=False)
		
		df.loc[len(df)] = new_data
		df.to_csv("login.csv", index=[0])
	def check_passwoed(self,passwd,key):
		pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
		if re.match(pattern,passwd):
			# key = Fernet.generate_key()

			# Erstellen eines Fernet-Objekts für die Verschlüsselung
			cipher_suite = Fernet(key)
			
			# Verschlüsseln der Nachricht mit AES-256-CBC
			cipher_text = cipher_suite.encrypt(passwd.encode('utf-8'))
			
			# Ausgabe des verschlüsselten Textes
			self.passwd = base64.b64encode(cipher_text).decode()
			
			return False
		else:
			print("mindestens 8 Zeichen lang \nmindestens eine Kleinbuchstabe\nmindestens eine Großbuchstabe\nmindestens eine Zahl\nmindestens ein Sonderzeichen")
			return True
	def decode_password(self,passwd,key):
		cipher_suite = Fernet(key)
		encrypted_bytes = base64.urlsafe_b64decode(passwd.encode())
		decrypted_bytes = cipher_suite.decrypt(encrypted_bytes)
		decrypted_text = decrypted_bytes.decode('utf-8')
		return decrypted_text
	
		
	def check_username(self, check):
		try:
			pd = pandas.read_csv("login.csv")
			data = pd.loc[pd['Username'] == check]
			if len(data) != 0:
				return True
			else:
				return False
		except:
			return False
		
	def check_email(self, check):
		pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
		if re.match(pattern,check):
			try:
				pd = pandas.read_csv("login.csv")
				data = pd.loc[pd['email'] == check]
				if len(data) != 0:
					print("This Email is olrady exeitet")#messagebox
					return True
				else:
					return False
			except:
				return False
		else:
			print("enter one currect email.")
			return True


test = LoginSystem()
test.save_data()
