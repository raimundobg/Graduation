# -*- coding: utf-8 -*-
"""
GRADUATION PROJECT FIRST PROTOTYPE
DATASET : first_it_df.txt

Raimundo Burchardt
Student Number: 1779575
Master: Data-Driven-Design
                'Recommendation system based on keywords for finding mentors and mentees'

@author: raimu
"""

#1) main menu: user can choose to register and log in - 
import csv
def mainmenu():
    print("Welcome to  Reflecta - the mentor-mentee match maker")
    while True: 
        print("""--------MAIN MENU--------
        Find a mentor  or a mentee
        1. Register
        2. Login
        """)
#if statements to provide select described options
        x=input('Select an option writing the number: ')
        if int(x)==1:
            register()
            break
        elif int(x)==2:
            login()
            break
        
#2 ) registration function - here all the relevant data for the dataset is 
#asked aligned with the datapoints defined on the theoretical framework and survey
def register():
    print("----------Registration Form----------")
    print()
    print("Relevant questions for finding your perfect match will be asked. No worries, accordingly to GDPR the data will be anonymyzed and stored in an encrypted server")

#open dataset to store where survey data was stored to append new users
    with open("first_it_df.txt", "a") as fo:
        writer=csv.writer(fo)
# data will be collected here :  With the library Faker first and lastname, plus emails were simulated while in user testing users were asked to give an alias
        firstname=input("Please tell us your firstname: ")
        lastname=input("Now your lastname: ")
        username=firstname[0:4]+lastname[0:3] # username is generated based on the first four values of first name and first 3 values of lastname
        #username=firstname+lastname[0]+'-member' #stringmanipulation
        print("Your generated username is: ", username)
        password=input("Now enter a password: ")
        print('Do not forget to write down the username and password and store it safely...')
        gender=input("Enter your Gender - : Write either: male - female - other: ")
        age=input("How old are you? - write down the number, e.g. 18  : ")
        email=input("Please enter your email: ")
        print()
        print("******************************************************************************")
        print()
        print('Now we will ask you questions to find your perfect match:')
        status_list=["1) mentor", "2) mentee"]
        print()
        print('What are you looking for?: ', *status_list, sep='\n')
        status=input('Please type your answer: mentor or mentee: ')
        #type of intelligences
        print()
        print('Awesesome! We will help you find the best', status)
        #data collection based on literature research starts here with the theory of 8 type of intelligence
        #list of values (intelligence type list (itype))
        itypes_list=["1) natural", "2) musical", "3) linguistic", "4) interpersonal", "5) intrapersonal", "6) corporal", "7) mathematical", "8) visual-spacial", "9) existential"]
        print()
        print()
        print(" What kind of intelligence represents you? Choose from the list below (Feel free to select min. 1 and max. 3 options): ")
        print()
        print(*itypes_list, sep='\n') #intelligence types are separated as an horizontal list and displayed for collecting user input
        itypes1=input("First Intelligence type: please write the intelligence that appeals you the most - if none press ENTER to continue: ")
        print()
        itypes2=input("Second Intelligence type: please write the second intelligence that appeals you the most - if none press ENTER to continue: ")
        print()
        itypes3=input("Third Intelligence type:please write the third intelligence that appeals you the most - if none press ENTER to continue: ")        
        print()
        
        #what are your strengths# based on survey the top 5 most mentioned were used
        field_list=["1) psychology/rrhh ", "2) design", "3) medicine", "4) web development", "5) it", "6) entrepreneurship", "7) sustainability", "8) commercial", "9) art"]
        print("******************************************************************************")
        print("Based on data collected we have found that these are the most demanded career fields: ")
        print(*field_list, sep='\n')
        professional_field=input("Please choose the one you are an expert or the one that interests you to become an expert: ")
        print()
        print("******************************************************************************")
        print()
        print("Now the final details are missing, let´s find out your expectations towards your match: ")
        print()
        attribute_list=["1) enthusiasm", "2) empathy", "3) calmness", "4) meticulousness", "5) modesty"]
        print()
        print(*attribute_list, sep='\n')
        print()
        relevant_attribute=input('Which one is the most important characteristic for your match: ')
        print()
        print("******************************************************************************")
        role_list=["1) availability", "2) guidance", "3) motivate", "4) share personal experiences", "5) solve problems", "6) support"]
        print()
        print(*role_list, sep='\n')
        print()
        mentor_role=input('Which one should be a mentor role? (type the answer):')
        print()
        print("******************************************************************************")
        print()
        print("For managing expectations, finally we need to know the frequency of sessions you expect")
        frequency_list=["1) once per week ",  "2) once per month ", "3) twice per month "]
        print()
        print(*frequency_list, sep='\n')
        print()
        sesh_frequency=input('How often would you be available for the sessions with your match? : ')
        print()
        
#username, password, firstname, lastname, status, itype1, itype2, itype3, user_gender, user_age, professional_field, relevant_attribute, 
#mentor_expertise, match_desired_gender, match_desired_age, mentor_rol_1, mentor_rol_2, session_freq


        writer.writerow([username, password, firstname, lastname, gender, email, age, status, itypes1, 
                         itypes2, itypes3, professional_field, relevant_attribute, mentor_role, sesh_frequency])
        print()
        print("Congrats, ", username, ",", "you have completed the form")
        print("You have succesfully registered")
        print()
        print("******************************************************************************")
        mainmenu()

#Login section : for login the generated username and password must be provided

def login():
    print('---login---')
    notloggedin=True
    while notloggedin==True:
        with open("first_it_df.txt", "r") as f:
            username=input('Enter username: ')
            password=input('Enter password: ')
            reader=csv.reader(f)
            for row in reader:
                for field in row:
                    if field ==username and row[1]==password:
                        notloggedin=False
                    else:
                        break
            if notloggedin==True:
                print("please try again: ")
            else:
                print("--Welcome-- lets find your match!")
                profile(username)

#after users log in, the function profile is called and the value username is printed together with the index equivalent to user
# here the user is asked to take actions : to find recommendations based on keywords (SEARCH 'S' section (user can provide them freely) 
#or to find recommendations based on the keywords given at the moment of registering (MATCH 'M' section)
#in the Match section user is asked again to provide the keywords as in the User Interface this represents a Drag and Drop Feature
#Where the user can freely change their keywords and so influence the recommendations


def profile(username):
    print()
    print()
    print("Username:", username)
    print(" --Welcome to your profile-- ")
    with open("first_it_df.txt", newline="") as f:
        reader=list(csv.reader(f))
        temporarylist=enumerate(reader)
        for idx, row in temporarylist:
            for field in row:
                if field==username:
                    #username_index=idx
                    #print("Your username index is", username_index)
                    print()
    print("Time to find your match?")
    choice=input("Press S to search or M for Match: ")
    if choice=='s' or choice=='S':
        search()
    elif choice=='M' or choice=='m':
        matchmake()

# =============================================================================

# here the user is asked to take actions : to find recommendations based on keywords (SEARCH 'S' section (user can provide them freely) 
# it must be noted that based on preliminary research, gender and age based search was not considered as more than 85% of survey respondents
# considered those points as not relevant

def search():
    print("--Search Tool-- ")
    print("""
    1. Search by  Keyword
    2. Return to main menu 
    """)
    choice=input("What would you like to do?")
    if int(choice)==1:
        keyword()
    elif int(choice)==2:
        mainmenu()

    
#search by keyword 
# here user can enter the keyword based on professional fields of interest, intelligence types (which represent personality traits), mentor attribute or characteristics
def keyword():
    print("--Keyword Search--")
    wordfound=False
    while wordfound==False:
        with open("first_it_df.txt", "r") as f:
            keyword=input("Enter keyword: It could be a intelligence type, a professional field or a relevant attribute.")
            reader=csv.reader(f)
            for row in reader:
                for field in row:
                    if field==keyword:
                        print(row)
                        wordfound=True

# If user choose MATCH 'M' user will be taken to match section
#in the Match section user is asked again to provide the keywords as in the User Interface this represents a Drag and Drop Feature
# Where the user can freely change their keywords and doing so influence its recommendations
# After finishing its actions, the user can wave other user ('equivalent to like') and if the other user waved back, 
#then a direct message feature will show up -- This last is considered on the User Interface

def matchmake():
    print("Welcome to the match section ")
    wordfound=False
    while wordfound==False:
        with open("first_it_df.txt","r") as f:
            status_list=["1) mentor", "2) mentee"]
            print()
            print('What are you looking for?: ', *status_list, sep='\n')
            status_search=input('Please type your answer: mentor or mentee: ')
            print()
            print("******************************************************************************")
            keystrength=input("enter one of your intelligence types:")  
            keystrength1=input("enter a second intelligence type (press enter to skip question):")
            keystrength2=input("enter a third intelligence type (press enter to skip question):")
            #what are your strengths
            field_list=["1) psychology/rrhh ", "2) design", "3) medicine", "4) web development", "5) it", "6) entrepreneurship", "7) sustainability", "8) commercial", "9) art"]
            print("******************************************************************************")
            print("Based on research we have found that these are the most demanded professional fields: ")
            print(*field_list, sep='\n')
            keycareer=input("choose the field you are an expert or want to become an expert: ")
            print()
            print()
            attribute_list=["1) enthusiasm", "2) empathy", "3) calmness", "4) meticulousness", "5) modesty"]
            print(*attribute_list, sep='\n')
            attribute=input('Which one is the most important characteristic for your match?: ')
            
            print("potential - matches: ")
            reader=csv.reader(f)
            for row in reader:
                #if row[7] == keystrength and row[8] == keystrength1 and row[10] == keycareer:
                if keystrength in row and keystrength1 in row and keystrength2 in row and keycareer in row and attribute in row and status_search in row :
                    print("Recommended profiles based on your keywords")
                    print("Wave the match you like and if the user waves back, get in touch")
                    print()
                    print((row[0:1], row[7:14]))
                    print("******************************************************************************")
                elif keystrength in row and keystrength1 in row and keycareer in row and status_search in row and attribute in row:
                    print("Recommended profiles based on your keywords")
                    print("Wave the match you like and if the user waves back, get in touch")
                    print()
                    print((row[0:1], row[7:14]))
                    print()
                    print("******************************************************************************")
                elif keystrength in row and keycareer in row and status_search in row and attribute in row:
                    print("Recommended profiles based on your keywords")
                    print("Wave the match you like and if the user waves back, get in touch")
                    print()
                    print((row[0:1], row[7:14]))
                    print()
            break                        
mainmenu()