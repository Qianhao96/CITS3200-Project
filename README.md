# CITS3200-Project

TEAM MEMBERS TEAM U

- Geoffrey	Davis	20743192@student.uwa.edu.au
- Joshua ChunHui	Goh	21978677@student.uwa.edu.au
- Dan Hua	Jiang	21982063@student.uwa.edu.au
- Jonathan YeeLeong	Kok	20744321@student.uwa.edu.au
- Qianhao	Liu	21952083@student.uwa.edu.au
- Jainish Mahesh	Pithadiya	21962504@student.uwa.edu.au


Auditor 
Syed Zulqarnain Gilani


Standard :
- django 2.0 <- pip3 install django
- python 3.7 or up 

Additional libraries to add: 
- django pickledfield <- pip3 install django-picklefield
- pydocx <- pip install python-docx

PROCEDURE OF WORK: 

- Branch off master
- do your work
- test
- make pull request
- notify someone to review pull request to ensure correct procedures are implemented. DO NOT SELF APPROVE
- Review comments given by reviewer and make changes and create pull request
- repeat until pull request is approved.
- PLEASE FOLLOW THIS PROTOCOL WE DONT WANT TO BREAK OUR CURRENT CODEBASE


To view on your mobile: 
- For Android users: 
    - install termux 
    - clone this repo 
    - install django and python + additional libraries 
    - run as per usual 
______________________________________________________________________________________________________________________________

- Auth altered: 
To successfully create a user you must `activate user` in `user requests` in admin view. This is to prevent unauthorized users from creating accounts. 

if you run into issue (chances are its migration issues): 
run : `python3 manage.py makemigrations animalwellbeing` 
run: `python3 manage.py migrate` 

If you run into any other issues let us know. 

To run locally: 
`python3 maange.py makemigrations animalwellbeing`
`python3 manage.py migrate`
`python3 manage.py runserver`

To manually edit models in shell 
`python3 manage.py shell` 

