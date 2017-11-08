import smtplib

class mailer(object):
	def __init__(self, fromaddr, toaddr, username, password):
		self.fromaddr = fromaddr
		self.toaddr = toaddr
		self.username = username
		self.password = password
		self.server = None

	def initiate_session(self):
		self.server = smtplib.SMTP('smtp.gmail.com:587')
		self.server.starttls()
		self.server.login(self.username, self.password)

	def send_email(self, msg):
		self.server.sendmail(self.fromaddr, self.toaddr, msg)
		return True

	def quit(self):
		self.server.quit()