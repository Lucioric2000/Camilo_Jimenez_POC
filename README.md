# Camilo_Jimenez_POC

These test use the Chrome Driver for realizing the scraping. If the Chrome driver executable for your pataform is not in the folder where you are executing the software, you shoud download the appropiate driver there.

# Settings

This option will allow you to see and edit the database. First, yo need to create a superuser, using the command line. Under the project root folder, execute python manage.py createsuperuser. Then, the program will ask you a username, an email and a password. Record your credentials in a secure place. Thee, enter to the webpage, and click in settings. A login page will appear, where you need to enter your credentials. Then, at the upper left of the page there will appear your username with a menu with 2 options:
Settings: there will appear a page when you can view, edit, delete and add database records of diffent types.
Log out: logs you out.

# Retailer accounts:
Under this link you can add a new Amazon account

# My codes:
You can add a gift code to redeem to a specified account. When pushing Submit, it will submit the code redemption to a background process where the code is to be checked later.

# Quick redeem:
You can add a gift code to redeem to a specified account. When pushing Submit, it will reseem the code at the moment and display the redemption status.

#status:
This link shows the status of all the gift codes redemption

#Accounts:
This link shows all the Amazon accounts in the database

#Clear:
This endpoint (/clear) is not linked, for safety, so it has to be entered manually. It clears all the databases.