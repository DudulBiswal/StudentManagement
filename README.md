Django Student Management System (beta)
This is a Simple Student Management System Developed for Educational Purpose using Python (Django). Feel free to make changes based on your requirements.

Project Demo on YouTube

I've created this project while learnging Django and followed tutorial series from SuperCoders

And if you like this project then ADD a STAR ⭐️ to this project 👆

Features of this Project
A. Admin Users Can
See Overall Summary Charts of Stuudents Performance, Staffs Perfomrances, Courses, Subjects, Leave, etc.
Manage Staffs (Add, Update and Delete)
Manage Students (Add, Update and Delete)
Manage Course (Add, Update and Delete)
Manage Subjects (Add, Update and Delete)
Manage Sessions (Add, Update and Delete)
View Student Attendance
Review and Reply Student/Staff Feedback
Review (Approve/Reject) Student/Staff Leave
B. Staff/Teachers Can
See the Overall Summary Charts related to their students, their subjects, leave status, etc.
Take/Update Students Attendance
Add/Update Result
Apply for Leave
Send Feedback to HOD
C. Students Can
See the Overall Summary Charts related to their attendance, their subjects, leave status, etc.
View Attendance
View Result
Apply for Leave
Send Feedback to HOD
Support Developer
Subscribe & Share my YouTube Channel - https://bit.ly/vijay-thapa-online-courses
Add a Star 🌟 to this 👆 Repository
Donate
PayPal

Buy me a Coffee ☕️

Donate by wire transfer: E-Mail at donate@vijaythapa.com for wire transfer details.

How to Install and Run this project?
Pre-Requisites:
Install Git Version Control [ https://git-scm.com/ ]

Install Python Latest Version [ https://www.python.org/downloads/ ]

Install Pip (Package Manager) [ https://pip.pypa.io/en/stable/installing/ ]

Alternative to Pip is Homebrew

Installation
1. Create a Folder where you want to save the project

2. Create a Virtual Environment and Activate

Install Virtual Environment First

$  pip install virtualenv
Create Virtual Environment

For Windows

$  python -m venv venv
For Mac

$  python3 -m venv venv
Activate Virtual Environment

For Windows

$  source venv/scripts/activate
For Mac

$  source venv/bin/activate
3. Clone this project

$  git clone https://github.com/vijaythapa333/django-student-management-system.git
Then, Enter the project

$  cd django-student-management-system
4. Install Requirements from 'requirements.txt'

$  pip install -r requirements.txt
5. Add the hosts

Got to settings.py file
Then, On allowed hosts, Add [‘*’].
ALLOWED_HOSTS = ['*']
No need to change on Mac.

6. Now Run Server

Command for PC:

$ python manage.py runserver
Command for Mac:

$ python3 manage.py runserver
7. Login Credentials

Create Super User (HOD)

$  python manage.py createsuperuser
Then Add Email, Username and Password

or Use Default Credentials

For HOD /SuperAdmin Email: admin@gmail.com Password: admin

For Staff Email: staff@gmail.com Password: staff

For Student Email: student@gmail.com Password: student

For Sponsor or Projects Enquiry
Email - hi@vijaythapa.com
LinkedIn - vijaythapa
