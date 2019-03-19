# sending-email-using-python-and-mailgun-api

This script can be used to send emails to multiple users at the same time.

Configuration:
==============
1. Create `env.py` file
2. Content of the `env.py` file
    
    #Your api key, from Mailgun's Control Panel
    
    `api_key = 'key-';`

    #Your domain, from the Mailgun Control Panel
    
    `domain = '';`

    #Your sending email address
    
    `from_mail = '';`
3. CGPA.csv file headers should contain (You may add or remove columns based on your requirement)
    
    rollnumber,	name,	email,	cgpa

4. Update the `msit_mailgun_test.py` file's main() function according the csv input columns    
