import random
import webbrowser
from datetime import datetime
from time import sleep as s
import instaloader
import pyautogui
#Greet part
greet_input=['hi','hey','hello','hey hello','helo']
greet_responses=['Hi' ,'Yes','Yup!',"Hey Mate!"'Welcome!','Whatsup!',' Yes, Iam glad here to work for you!']
input_converted=""
#Questions list to user
qst=["Whats Yours?","What is Your Age?","Are you in love ?","Which Friends do you have more BOYS/GIRLS ?","Which School are you studied?","Whats your Dream!?","What is Your Hobby","Which Type of Songs Do You love more?","Who's songs Do You like more?","Are You Moms Child?"]
bot_ans=['My name is Elisa','I dont have Age ','Im love with my Developer '," I have so many freinds some of them are Alexa , Google , Siri","I am learning  By talking to You","My Dream is to Serve a Best Ever Assistant to users","My hobby is chatting with my developer","I love romantic songs","I mostly like U1 songs","My Developer taught me Moms are the only True hearted Persons!"]
talk_contunity=["Good","Awesome!","Sounds Good","Okay Well","Well","Nice"]
bot_spl="Ok Always Take Care of Her!Tell Her about me :)"
#lists
time_list=["whats the time now","hey, what is the time now","current time","time","what is the time now","tell the current time"]
search_list=["search something","search","i want to search","i want to search something"]
do_list_ss=["take a screenshot","take screenshot","screenshot"]
do_list_insta=["download instagram dp","download instagram profile","instagram profile download","instagram dp download"]
date_list=["whats the today date","hey, what is the todays date","what is the todays date","current date","date","tell the current date"]
ignore_msg=["no","i dont have time","no i have some other work",'no i dont have time']
user_ans=['okie','okay','ok','cool','done','hmm','hm','mm','mmm','nice','well','good','wow','oh good','oh nice']
#date and time
now = str(datetime.now())
nowsplit = now.split()
def time():
    current_time = nowsplit[1]
    return("\nCurrent Time in Hours : Minutes : Seconds.Milliseconds: "+current_time)
def date():
    current_date = nowsplit[0]
    return("\nCurrent Date in Year-Month-Date :", current_date,"\n")
def search(msg):
        s(1);print("Bot : What Do You Want to Search ?")
        input1 = input("You : ")
        if(msg=="wikipedia"):
            search = "https://en.wikipedia.org/wiki/"
        elif(msg=="youtube"):
            search="https://www.youtube.com/results?search_query="
        elif(msg=="google"):
            search="https://www.google.com/search?q="
        else:
            print("Bot : Sorry this platform isn't programmed in me! Please Check Anyother Platform from these : 'youtube','google','wikipedia' ")
        search_final = search + input1
        s(1);print("Bot : Okay Just Wait few Minutes!")
        webbrowser.open(search_final)
def do_work_insta(msg):
        ig = instaloader.Instaloader()
        s(1);print("Bot : Enter the Username")
        dp = input("You : ")
        s(1);print("Bot : Wait a Minute !")
        ig.download_profile(dp, profile_pic_only=True)
        dp_path=r"Bot : Pic path ==> C:\Users\ELCOT\PycharmProjects\ProjectBot"
        dp_filename='\ '+dp+'\ '
        s(1);print(dp_path+dp_filename)
def do_work_ss(msg):
    s(1);print("Bot : Give the Name for Screenshot with 'BACK SLASH' (\) and Extension (.png)!")
    ss_name=input("You : ")
    ss_path=r'C:\Users\ELCOT\Desktop'
    path_edited=ss_path+ss_name
    pyautogui.screenshot(path_edited)
    s(1);print("Bot : Yeah Screenshot has Taken!")
    s(1);print(r"Bot : Screenshot stored in ",path_edited)
while(input_converted!="bye"):
    greet = input("You : ")
    input_converted = greet.lower()
    if (input_converted in greet_input):
        s(1);print("Bot : ",random.choice(greet_responses)+" , Are you Want to Know Anything?")

    elif(input_converted=="bye"):
        s(1);print("Bot : Bye Bye Take Care!")
    elif(input_converted=="yes"):
        s(1);print("Bot : Cool...! What do You Want to know? or Want to do?")
        reply=""
        while(reply!="exit"):
            reply = (input("You : ")).lower()
            if (reply in time_list):
                time()
            elif(reply in date_list):
                date()
            elif(reply in user_ans):
                if(reply in user_ans):
                    s(1);print("Bot : Hmmm! Do You still Want to Know Anything ? If you don't Want please text 'Exit' ")
                    s(1);reply=(input("You : ")).lower()
                    if(reply!="exit"):
                        print("Bot : Okie! Ask...,Im Here to serve for You! :)")
                else:
                    s(1);print("Bot : Sorry I Can't Understand!")
            elif(reply in search_list):
                s(1);print("Bot : In which Platform do you want to search?")
                s(1);reply=(input("You : ")).lower()
                search(reply)
            elif(reply in do_list_ss):
                do_work_ss(reply)

            elif(reply in do_list_insta):
                do_work_insta(reply)

        if(reply=="exit"):
            s(1);print("Bot : Okay Your were Exited ! Are you Want to ask any other question ?" )

    elif(input_converted=="no"):
        s(1);print("Bot : Thank you !")
        s(1);print("Bot : If you don't Mind Shall I ask Something?")
        s(1);reply=(input("You : ")).lower()
        if(reply not in ignore_msg):
            i=0
            ans=[]
            while(i<10):
                s(1);print("Bot : ",bot_ans[i])
                s(1);print("Bot : ",qst[i])
                s(1);reply=(input("You : ")).lower()
                if(reply=="yes"):
                    s(1);print("Bot : ",bot_spl)
                    s(1);reply=(input("You : ")).lower()
                    if(reply=="sure"):
                        s(1);print("Bot : Great!!")
                    break
                ans.append(reply)
                s(1);print("Bot : ",random.choice(talk_contunity),ans[0])
                i=i+1
        else:
            s(1);print("Bot : Okie !Bye Bye Take Care!")

    else:
        s(1);print("Bot : ","OOPs Sorry I can't able to understand :)")

