import colorama
import Psychology_text
import sys
import mysql.connector
from PyInquirer import prompt
import os
from examples import custom_style_3
from rich.console import Console
from pyfiglet import figlet_format
from colorama import Fore
from rich.table import Table

colorama.init(autoreset=True)
console = Console()
os.system("cls")

database_exist = True
try:
    db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="psychology")
    mycursor = db.cursor()
except Exception:
    database_exist = False
    db = mysql.connector.connect(host="localhost", user="root", passwd="root")
    mycursor = db.cursor()
    mycursor.execute("create database psychology")
if database_exist == False:
    db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="psychology")
    mycursor = db.cursor()
    mycursor.execute(
        "create table AISS(Student_ID int PRIMARY KEY AUTO_INCREMENT,Name varchar(50), Age smallint, Gender varchar(1), Emotional_Adjustment_Score int, Social_Adjustment_Score int, "
        "Educational_Adjustment_Score int, Overall_Score int, Remarks varchar(50)) ")
    mycursor.execute(
        "create table SCQ(Student_ID int PRIMARY KEY AUTO_INCREMENT,Name varchar(50), Age smallint, Gender varchar(1), Physical_Score int, "
        "Social_Score int, Temperamental_Score int, Educational_Score int, Moral_Score int, Intellectual_Score int, Overall_Score int, Remarks varchar(50))")
    mycursor.execute(
        "create table SCAT(Student_ID int PRIMARY KEY AUTO_INCREMENT, Name varchar(50), Age smallint, Gender varchar(1), SCAT_Score int, Remarks varchar(50))")
    mycursor.execute(
        "create table FLAGGED(Student_ID int PRIMARY KEY AUTO_INCREMENT, Name varchar(50), Age smallint, Gender varchar(1), Remarks varchar(50))")


def ASCII():
    ASCII_Art = figlet_format("PSYCHOLOGICAL ASSESSMENT", font="univers", justify="center", width=210)
    print(Fore.CYAN + ASCII_Art)
    print("\n" * 5)


ASCII()


def interpretation_SCQ(a, b):
    if a > 33:
        console.print("Your score in " + b + " domain is very high.", style="green")
    if a in [25, 26, 27, 28, 29, 30, 31, 32]:
        console.print("Your score in " + b + " domain is above average.", style="green")
    if a in [18, 19, 20, 21, 22, 23, 24]:
        console.print("Your score in " + b + " domain is average.", style="yellow")
    if a in [9, 10, 11, 12, 13, 14, 15, 16, 17]:
        console.print("Your score in " + b + " domain is below average.", style="red")
    if a < 8:
        console.print("Your score in " + b + " domain is very low.", style="bold red")


def interpretation_AISS(sum, sex, area):
    if sex == "M":
        if sum > 11:
            console.print(
                "The subject is categorized in E category. Very unsatisfactory result. The results indicate unstable",
                area, style="red")
        if sum in [8, 9, 10]:
            console.print(
                "The subject is categorized in D category. Unsatisfactory result. The results indicate unstable", area,
                style="red")
        if sum in [5, 6, 7]:
            console.print(
                "The subject is categorized in C category. Average result. The results indicate relatively stable",
                area, style="yellow")
        if sum in [2, 3, 4]:
            console.print("The subject is categorized in B category. Good result. The results indicate stable", area,
                          style="green")
        if sum in [1, 0]:
            console.print(
                "The subject is categorized in A category. Excellent result. The results indicate above average",
                area, style="green")
    if sex == "F":
        if sum > 11:
            console.print(
                "The subject is categorized in E category. Very unsatisfactory result. The results indicate unstable",
                area, style="red")
        if sum in [8, 9, 10]:
            console.print(
                "The subject is categorized in D category. Unsatisfactory result. The results indicate unstable",
                area, style="red")
        if sum in [6, 7]:
            console.print(
                "The subject is categorized in C category. Average result. The results indicate relatively stable",
                area, style="yellow")
        if sum in [2, 3, 4, 5]:
            console.print("The subject is categorized in B category. Good result. The results indicate stable", area,
                          style="green")
        if sum in [1, 0]:
            console.print(
                "The subject is categorized in A category. Excellent result. The results indicate above average",
                area, style="green")


def interpretation_AISS_overall(sum, sex):
    if sex == "M":
        Overall_Adjustment = " "
        if sum <= 5:
            Overall_Adjustment = "Excellent Adjustment"
        if 5 <= sum <= 12:
            Overall_Adjustment = "Good Adjustment"
        if 13 <= sum <= 21:
            Overall_Adjustment = "Average Adjustment"
        if 22 <= sum <= 30:
            Overall_Adjustment = "Unsatisfactory Adjustment"
        if sum > 31:
            Overall_Adjustment = "Very Unsatisfactory Adjustment"
    if sex == "F":
        if sum <= 5:
            Overall_Adjustment = "Excellent Adjustment"
        if 6 <= sum <= 14:
            Overall_Adjustment = "Good Adjustment"
        if 15 <= sum <= 22:
            Overall_Adjustment = "Average Adjustment"
        if 23 <= sum <= 31:
            Overall_Adjustment = "Unsatisfactory Adjustment"
        if sum > 32:
            Overall_Adjustment = "Very Unsatisfactory Adjustment"
    return Overall_Adjustment


def interpretation_SCAT(sum, sex):
    if sex == "M":
        if sum > 30:
            console.print("You have extremely high anxiety", style="red")
            x = "Extremely high anxiety"
            return x
        if 25 < sum < 30:
            console.print("You have high anxiety", style="yellow")
            x = "High anxiety"
            return x
        if 15 < sum < 25:
            console.print("You have normal anxiety", style="green")
            x = "Low Anxiety"
            return x
        if 12 < sum < 14:
            console.print("You have low anxiety", style="red")
            x = "Low anxiety"
            return x
        if sum < 12:
            console.print("You have extremely low anxiety", style="red")
            x = "Extremely low anxiety"
            return x
    if sex == "F":
        if sum > 30:
            console.print("You have extremely high anxiety", style="red")
            x = "Extremely high anxiety"
            return x
        if 25 <= sum <= 30:
            console.print("You have high anxiety", style="yellow")
            x = "High anxiety"
            return x
        if 20 <= sum <= 25:
            console.print("You have normal anxiety", style="green")
            x = "Normal anxiety"
            return x
        if 15 <= sum <= 16:
            console.print("You have low anxiety", style="yellow")
            x = "Low anxiety"
            return x
        if sum < 15:
            console.print("You have extremely low anxiety", style="red")
            x = "Extremely low anxiety"
            return x


def choice(n):
    if n == "1":
        console.print(
            "1. AISS (Adjustment inventory for school students)\n2. SCQ (Self-concept questionnaire)\n3. SCAT (Sinha's comprehensive anxiety test)",
            style="cyan", justify="center")
        F_choice = input("Choose the table you want to access: ")
        if F_choice in ["1", "2", "3", "4"]:
            os.system("cls")
            ASCII()
            pass
        else:
            while True:
                F_choice = input("Please choose a valid option: ")
                if F_choice in ["1", "2", "3", "4"]:
                    os.system("cls")
                    ASCII()
                    break
                else:
                    continue
        if F_choice == "1":
            table = Table(show_header=True, header_style="cyan")
            mycursor.execute("SELECT * FROM AISS")
            columns = ("Student_ID", "Name", "Age", "Gender", "Emotional_Adjustment_Score", "Social_Adjustment_Score",
                       "Educational_Adjustment_Score", "Overall_Score", "Remarks")
            for i in columns:
                count = 0
                table.add_column(i)
            for j in mycursor:
                for k in j:
                    count = count + 1
                    k = str(k)
                    if count == 1:
                        a = k
                    if count == 2:
                        b = k
                    if count == 3:
                        c = k
                    if count == 4:
                        d = k
                    if count == 5:
                        e = k
                    if count == 6:
                        f = k
                    if count == 7:
                        g = k
                    if count == 8:
                        h = k
                    if count == 9:
                        i = k
                table.add_row(a, b, c, d, e, f, g, h, i)
                count = 0
            console.print(table)
        if F_choice == "2":
            table = Table(show_header=True, header_style="cyan")
            mycursor.execute("SELECT * FROM SCQ")
            columns = (
                "Student_ID", "Name", "Age", "Gender", "Physical_Score", "Social_Score", "Temperamental_Score",
                "Educational_Score",
                "Moral_Score", "Intellectual_Score", "Overall_Score", "Remarks")
            count = 0
            for i in columns:
                table.add_column(i)
            for j in mycursor:
                for k in j:
                    count = count + 1
                    k = str(k)
                    if count == 1:
                        a = k
                    if count == 2:
                        b = k
                    if count == 3:
                        c = k
                    if count == 4:
                        d = k
                    if count == 5:
                        e = k
                    if count == 6:
                        f = k
                    if count == 7:
                        g = k
                    if count == 8:
                        h = k
                    if count == 9:
                        i = k
                    if count == 10:
                        l = k
                    if count == 11:
                        m = k
                    if count == 12:
                        n = k
                table.add_row(a, b, c, d, e, f, g, h, i, l, m, n)
                count = 0
            console.print(table)
        if F_choice == "3":
            table = Table(show_header=True, header_style="cyan")
            mycursor.execute("SELECT * FROM SCAT")
            columns = ("Student_ID", "Name", "Age", "Gender", "SCAT_Score", "Remarks")
            count = 0
            for i in columns:
                table.add_column(i)
            for j in mycursor:
                for k in j:
                    count = count + 1
                    k = str(k)
                    if count == 1:
                        a = k
                    if count == 2:
                        b = k
                    if count == 3:
                        c = k
                    if count == 4:
                        d = k
                    if count == 5:
                        e = k
                    if count == 6:
                        f = k
                table.add_row(a, b, c, d, e, f)
                count = 0
            console.print(table)
    if n == "2":
        mycursor.execute("SELECT * FROM FLAGGED")
        table = Table(show_header=True, header_style="cyan", title_justify="center")
        columns = ["Student_ID", "Name", "Age", "Gender", "Remarks"]
        count = 0
        for i in columns:
            table.add_column(i)
        for j in mycursor:
            for k in j:
                count = count + 1
                k = str(k)
                if count == 1:
                    a = k
                if count == 2:
                    b = k
                if count == 3:
                    c = k
                if count == 4:
                    d = k
                if count == 5:
                    e = k
            table.add_row(a, b, c, d, e)
            count = 0
        console.print(table)


def info():
    fn = input("Enter your first name: ")
    ln = input("Enter your last name: ")
    n = fn + " " + ln
    try:
        a = int(input("Enter your age:"))
    except ValueError:
        a = int(input("Please enter an integer: "))
    return [n, a]


def gender_sex():
    sex = input('Please input your sex (M/F): ')
    if sex not in ["M", "F"]:
        while True:
            sex = input("Please choose a valid option: ")
            if sex in ["M", "F"]:
                break
            else:
                continue
    return sex


console.print(
    "1. AISS (Adjustment inventory for school students)\n2. SCQ (Self-concept questionnaire)\n3. SCAT (Sinha's comprehensive anxiety test)\n4. Administrator Privileges*",
    style="white", justify="center")
print("* Administer Privileges require password")
print("\n" * 2)
I_choice = input("Choose the option you want to use: ")
if I_choice in ["1", "2", "3", "4"]:
    pass
else:
    while True:
        I_choice = input("Please choose a valid option: ")
        if I_choice in ["1", "2", "3", "4"]:
            break
        else:
            continue

if I_choice in ["1", "2", "3"]:
    info = info()
    name = info[0]
    age = info[1]
    gender = gender_sex()


def test(n):
    if n == "1":
        print("\n")
        console.print('''Instructions:

•	Each question can be answered in `yes` or `no`.
•	Don’t leave any question and try to complete as soon as possible.
•	There are no right or wrong answers.
•	Give the first natural answer as it comes to you. When in doubt, give the best possible answer.
•	Read the questions carefully.
•	There is no time limit for this test.
•   Press on the "X" to quit the test.

''', style="cyan", justify="left")
        input("Press any key to continue...")
        os.system("cls")
        Questions = Psychology_text.Questions_AISS
        A = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57]
        B = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58]
        C = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59]
        A_AR = []
        B_AR = []
        C_AR = []
        AR_list = []
        ER_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1,
                   1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
        score = 0
        count = -1
        for i in Questions:
            answer = prompt(
                {
                    'type': 'confirm',
                    'name': 'answer_AISS',
                    'message': i,
                }, style=custom_style_3)
            answer = answer['answer_AISS']
            if answer is None:
                print("Program Terminated.")
                sys.exit()
            elif answer is True:
                AR_list.append(1)
            else:
                AR_list.append(0)
        for j in range(0, 60):
            if AR_list[j] == ER_list[j]:
                score = score + 1
                count = count + 1
                if count in A:
                    A_AR.append(1)
                if count in B:
                    B_AR.append(1)
                if count in C:
                    C_AR.append(1)
            else:
                continue
        sum1 = 0
        for k in A_AR:
            sum1 = sum1 + k
        sum2 = 0
        for l in B_AR:
            sum2 = sum2 + l
        sum3 = 0
        for m in C_AR:
            sum3 = sum3 + m
        fin_sum = sum1 + sum2 + sum3

        print("------------------------------------------------------------------------------------------")
        console.print(Psychology_text.AISS_text, style="cyan", justify="left")
        input("Press any key to continue...")
        os.system("cls")

        interpretation_AISS(sum1, gender, "emotional adjustment.")
        print("\n")
        interpretation_AISS(sum2, gender, "social adjustment.")
        print("\n")
        interpretation_AISS(sum3, gender, "educational adjustment.")
        print("\n")
        remark = interpretation_AISS_overall(fin_sum, gender)
        if remark in ["Unsatisfactory Adjustment", "Very Unsatisfactory Adjustment"]:
            mycursor.execute("INSERT INTO FLAGGED(Name, Age, Gender, Remarks) VALUES(%s, %s, %s, %s)",
                             (name, age, gender, remark))
        mycursor.execute("INSERT INTO AISS(Name, Age, Gender, Emotional_Adjustment_Score, Social_Adjustment_Score, "
                         "Educational_Adjustment_Score, Overall_Score, Remarks) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                         (name, age, gender, sum1, sum2, sum3, fin_sum, remark))
        db.commit()
    if n == "2":
        print("\n")
        console.print('''Instructions: 
        On the following pages there are some questions and their probable answers given
        against them. You read them carefully and whichever suits, you choose them. You have to mark only one answer. An illustration is given below. There is no
        time limit for it but you should answer it as soon as possible.
        ------------------------------------------------------------------------------------------
        Illustration: 
        What type of teeth do you have?
        Very Beautiful (1), Beautiful (2), Average (3), Beautiless (4), Beautiless at all (5)
        If you think that you have beautiful teeth, you choose the word ‘Beautiful.''', style="cyan", justify="left")
        print()
        input("Press any key to continue...")
        os.system("cls")

        A = [2, 3, 9, 20, 22, 27, 29, 31]
        B = [1, 8, 21, 37, 40, 43, 46, 48]
        C = [4, 10, 14, 16, 19, 23, 24, 28]
        D = [5, 13, 15, 17, 25, 26, 30, 35]
        E = [6, 34, 35, 41, 42, 44, 45, 47]
        F = [7, 11, 12, 18, 33, 36, 38, 39]
        A_AR = []
        B_AR = []
        C_AR = []
        D_AR = []
        E_AR = []
        F_AR = []
        S_AR = []
        A_sum = 0
        B_sum = 0
        C_sum = 0
        D_sum = 0
        E_sum = 0
        F_sum = 0

        def find(a_, b_):
            if a_ in A:
                A_AR.append(b_)
            if a_ in B:
                B_AR.append(b_)
            if a_ in C:
                C_AR.append(b_)
            if a_ in D:
                D_AR.append(b_)
            if a_ in E:
                E_AR.append(b_)
            if a_ in F:
                F_AR.append(b_)

        def check(question, choices, x):
            answer_SCQ = prompt(
                {
                    'name': 'answer_SCQ',
                    'type': 'list',
                    'message': question,
                    'choices': choices
                }, style=custom_style_3)
            answer_SCQ = answer_SCQ['answer_SCQ']
            if answer_SCQ is None:
                print("Program Terminated.")
                sys.exit()
            choices.reverse()
            raw_score = choices.index(answer_SCQ) + 1
            x = x + raw_score
            S_AR.append(x)
            find(count, raw_score)

        Questions = Psychology_text.Questions_SCQ

        choice1 = Psychology_text.choice1
        choice2 = Psychology_text.choice2
        choice3 = Psychology_text.choice3
        choice4 = Psychology_text.choice4
        choice5 = Psychology_text.choice5
        choice6 = Psychology_text.choice6
        choice7 = Psychology_text.choice7
        choice8 = Psychology_text.choice8
        choice9 = Psychology_text.choice9
        choice10 = Psychology_text.choice10
        choice11 = Psychology_text.choice11
        count = 1
        sum = 0
        for i in Questions:
            if count in [1, 4, 7, 8, 10, 11, 12, 13, 15, 18, 28, 30, 32, 33, 36, 37, 34, 35, 38, 39]:
                check(i, choice1, sum)
                count += 1
            elif count in [16, 17, 19, 23, 24, 41, 43]:
                check(i, choice2, sum)
                count += 1
            elif count in [2, 3, 5, 9, 20, 22, 25, 27, 29, 31]:
                check(i, choice3, sum)
                count += 1
            elif count in [6, 14, 21, 26]:
                check(i, choice4, sum)
                count += 1
            elif count == 40:
                check(i, choice5, sum)
                count += 1
            elif count == 42:
                check(i, choice6, sum)
                count += 1
            elif count == 44:
                check(i, choice7, sum)
                count += 1
            elif count == 45:
                check(i, choice8, sum)
                count += 1
            elif count == 46:
                check(i, choice9, sum)
                count += 1
            elif count == 47:
                check(i, choice10, sum)
                count += 1
            elif count == 48:
                check(i, choice11, sum)
                count += 1

        for i in A_AR:
            A_sum = A_sum + i
        for j in B_AR:
            B_sum = B_sum + j
        for k in C_AR:
            C_sum = C_sum + k
        for l in D_AR:
            D_sum = D_sum + l
        for m in E_AR:
            E_sum = E_sum + m
        for o in F_AR:
            F_sum = F_sum + o
        fin_sum = A_sum + B_sum + C_sum + D_sum + E_sum + F_sum

        console.print(Psychology_text.SCQ_text, style="cyan", justify="left")
        input("Press any key to continue...")
        os.system("cls")
        print()
        interpretation_SCQ(A_sum, "Physical")
        print("\n")
        interpretation_SCQ(B_sum, "Social")
        print("\n")
        interpretation_SCQ(C_sum, "Temperamental")
        print("\n")
        interpretation_SCQ(D_sum, "Educational")
        print("\n")
        interpretation_SCQ(E_sum, "Moral")
        print("\n")
        interpretation_SCQ(F_sum, "Intellectual")
        remark = ""
        print()
        if fin_sum > 193:
            console.print("You have a very high self-concept.", style="green")
            remark = "Very-High self-concept"
        if 193 > fin_sum > 145:
            console.print("You have an above high self-concept.", style="green")
            remark = "High self-concept"
        if 144 > fin_sum > 97:
            console.print("You have an average self-concept.", style="yellow")
            remark = "Average self-concept"
        if 96 > fin_sum > 49:
            console.print("You have a below average self-concept.", style="red")
            remark = "Below Average self-concept"
        if fin_sum < 48:
            console.print("You have a low self-concept.", style="red")
            remark = "Very-low self-concept"
        if remark in ["Below Average self-concept", "Very-low self-concept"]:
            mycursor.execute("INSERT INTO FLAGGED(Name, Age, Gender, Remarks) VALUES(%s, %s, %s, %s)",
                             (name, age, gender, remark))
        mycursor.execute(
            "INSERT INTO SCQ(Name, Age, Gender, Physical_Score, Social_Score, Temperamental_Score, Educational_Score, Moral_Score, Intellectual_Score, Overall_Score, Remarks) VALUE(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name, age, gender, A_sum, B_sum, C_sum, D_sum, E_sum, F_sum, fin_sum, remark))
        db.commit()
    if n == "3":
        Questions = Psychology_text.Questions_SCAT
        console.print(Psychology_text.SCAT_text, style="cyan", justify="left")
        input("Press enter to continue...")
        os.system("cls")
        count = 0
        for i in Questions:
            # answer = easygui.ynbox(i, "choose your answer")
            answer = prompt({"name": "answer_SCAT", "type": "confirm", "message": i}, style=custom_style_3)
            answer = answer["answer_SCAT"]
            if answer == True:
                count = count + 1
            if answer is None:
                print("Program Terminated.")
        print('\n')
        remark = interpretation_SCAT(count, gender)
        if remark in ["Extremely high anxiety", "Extremely low anxiety"]:
            mycursor.execute("INSERT INTO FLAGGED(Name, Age, Gender, Remarks) VALUES(%s, %s, %s, %s)",
                             (name, age, gender, remark))
        mycursor.execute("INSERT INTO SCAT(Name, Age, Gender, SCAT_Score, Remarks) VALUE(%s, %s, %s, %s, %s)",
                         (name, age, gender, count, remark))
        db.commit()
    if n == "4":
        passwd = input("Enter your password: ")
        if passwd == "root":
            console.print("\n1. Access database\n2. Show flagged students", justify="center")
            print("\n" * 2)
            F_choice = input("Enter the privilege you want to use: ")
            os.system("cls")
            ASCII()
            if F_choice in ["1", "2"]:
                choice(F_choice)
            else:
                while True:
                    F_choice = input("Please enter a valid option: ")
                    if F_choice in ["1", "2"]:
                        choice(F_choice)
                    else:
                        continue
        else:
            while True:
                chance = input("Try again(Y/N): ")
                if chance in ["Y", "y"]:
                    passwd = input("Re-enter password: ")
                    if passwd == "root":
                        console.print("\n1. Access database\n2. Show flagged students", justify="center")
                        print("\n" * 2)
                        F_choice = input("Enter the privilege you want to use: ")
                        if F_choice in ["1", "2"]:
                            choice(F_choice)
                        break
                    else:
                        continue
                if chance in ["N", "n"]:
                    break
                else:
                    print("Please enter a valid option!")
                    continue


test(I_choice)
print("\n" * 2)
input("Press any key to close... ")
