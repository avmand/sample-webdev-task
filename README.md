What Is This?
-------------

This is a sample web development task done implemented using Flask, with the database stored using Firebase. The website is currently hosted on a Heroku server (sent by email).  


How To Use This
---------------

1. Run `pip install -r requirements.txt` to install dependencies
2. Run `python3 wsgi.py`. This calls app/main.py. main.py contains a majority of the code.
3. Navigate to http://127.0.0.1:5000/ in your browser to use the transaction system

If you are using the one hosted on the Heroku server, please ignore the above steps and use the link.


Assumptions
---------------

It works according to the specifications given in the document (uses Flask, Firebase, Heroku and logic-wise too). Some of the assumptions are:
1. The 'primary key' is your email address. Even if you enter a different name, your email address's last saved data will be used.
2. The bold numbers on the interaction page are the feedback values for the cell. They can be positive or negative.
3. The non-bold numbers on the same page are the cell numbers.
