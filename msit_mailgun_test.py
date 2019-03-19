import requests
from env import api_key, domain, from_mail
import csv

def send_simple_message(to_mail, subject="", body="", from_mail=from_mail):
    return requests.post(
        "https://api.mailgun.net/v3/%s/messages"%domain,
        auth=("api", api_key),
        data={"from": "MSIT LMS <%s>"%from_mail,
              "to": [to_mail],
              "subject": subject,
              "text": body})

def user_data(file_name="cgpa.csv"):
	# Example data object
	# data = [{
	# 		"email": "ss@fju.us",
	# 		"rollnumber": "1584",
	# 		"name": "sreenath sirimala",
	# 		"cgpa": 9.0
	# 	}]
	data = []
	try:
		data = csv.DictReader(open(file_name))
	except Exception as e:
		print(e)
		data = []
	return data

def main(file_name):
	data = user_data(file_name)
	subject = "CGPA"
	body = """
	Hi {},

		Your ({}) overall CGPA so far is {}.
	"""
	for user in data:
		try:
			print("sending email to {} with rollnumber {}. {} cgpa is {}".format(
				user['email'], user['rollnumber'], user['name'], user['cgpa']
			))
			body1 = body.format(user['name'], user['rollnumber'], user['cgpa'])
			response = send_simple_message(user['email'], subject, body1)
			print(response)
		except Exception as e:
			raise e

if __name__ == '__main__':
	file_name = "CGPA1.csv"
	main(file_name)
