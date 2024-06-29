# Webbox
Educational platform for teaching IT technologies and professions. Has a Django server and a telegram bot in Python

## How to run

The test database is already in the project, so starting the project is quite simple:

### Django server:

1. Create a virtual environment:

`py -m venv venv` - Windows

`python3 -m venv venv` - Linux

2. Activate it:

`venv/Sctipts/activate` - Windows

`source venv/bin/activate` - Linux

3. Install dependencies:

`pip install -r req.txt`

4. Go to the path: ./webbox/webbox: 

`cd /webbox/webbox`
5. Rename .env.test to .env, and enter the django key there in the SECRET_KEY field.
6. Start the server: 

`python manage.py runserver`

All!

### Telegram bot:

Repeat steps 1-3 from starting django server

1.Go to the path ./webbox_bot 

`cd webbox_bot`

2. Rename .env.test to .env, and enter the telegram key there in the TG_KEY field.
3. Run: 

`py main.py`

All!

## Screenshots
![image](https://github.com/bolgaro4ka/webbox/assets/123888141/c0820ab4-75f5-4ecb-8ccc-d7782e292f97)
![image](https://github.com/bolgaro4ka/webbox/assets/123888141/f6975a87-a176-43f0-8f67-ab34b9fc9758)
![image](https://github.com/bolgaro4ka/webbox/assets/123888141/e2b3a8f0-73d2-4fba-9af6-deac02f6aa28)
![image](https://github.com/bolgaro4ka/webbox/assets/123888141/61a1b7b8-8c27-43f1-94d6-9577f16f8284)
![image](https://github.com/bolgaro4ka/webbox/assets/123888141/2947c6f9-ac89-4a06-93ee-838a8c33a716)
![image](https://github.com/bolgaro4ka/webbox/assets/123888141/6958cf1d-6950-427e-8cba-89243fe46cfe)
![image](https://github.com/bolgaro4ka/webbox/assets/123888141/4b504ddc-c858-4811-b13f-56fba3a0da31)

![image](https://github.com/bolgaro4ka/webbox/assets/123888141/a3b58f47-e62e-4325-9e20-f39cf08e3eb9)
![image](https://github.com/bolgaro4ka/webbox/assets/123888141/863cda8c-98aa-41aa-a8eb-fcab05e70ebd)
![image](https://github.com/bolgaro4ka/webbox/assets/123888141/77394120-feb1-435c-bf92-e95124bc935a)

## Presentation
https://prezi.com/view/dCrQYx6qpLPwXuq1j8nn/

## Almost everything was done by Bolgaro4ka, the rest by Gorgun Egor




