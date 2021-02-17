import mysql.connector as sql






db=sql.connect(host='localhost',user='root',passwd='root',database='library')

cursr=db.cursor()

def Book_Entry():
    s1='insert into lib(Book_Name, Book_author,  Availabilty)values(%s,%s,%s)'
    print('PLEASE FILL UP THE GIVEN INFORMATION')
    id1="NULL"
    name=input('ENTER THE BOOK NAME  :--  ')
    aname=input("NAME OF THE BOOK's AUTHOR :--  ")
    availability='AVAILABLE'
    
    value=(name, aname, availability)
    try:
        cursr.execute(s1,value)
        print(name," SUCCESSFULLY ADDED IN THE LIBRARY STOCK")
        db.commit()
    except:
        print("unable to add book")
        a=input("TYPE 'y' if u want to re enter the data")
        if a=='y':
            Book_Entry()
        else:
            pass


def Register_Urself():
    
    s1='insert into registration(name , admssn_no, class, sec, D_O_B)values(%s,%s,%s,%s,%s)'
    print("give information")
    name=input("ENTER STUDENNT's NAME :--  ")
    adm=int(input("ENTER STUDENT's ADMISSION NUMBER :--  "  ))
    cls=int(input("ENTER STUDENT's CLASS IN DIGITS ONLY :--"  ))
    sec=input("ENTER UR SECTION IN CAPITALS :--  ")
    DoB=input("ENTER STUDENT's DOB(YYYY-MM-DD) :--  ")
    val=(name,adm,cls,sec,DoB)

    try:
        cursr.execute(s1,val)
        print('STUDENT REGISTERED')
        db.commit()

    except:
        print('Failed To Register The student name',name)

    




def book_find():
    print(" by which means u want to check the book .  Through \n 1. it's code \n 2. name \n 3. author \n")
    a=int(input("Write the No."))
    if a=='code' or a=='CODE':
        b=int(input("Enter Book Code"))
        s1="select * from lib where book_code = %s "
        val=(b,)
        cursr.execute(s1,val)
        abc=cursr.fetchone()
        if (abc==None):
            c=input("this code is not given to any book in this library sorry !!! \n press'y' if u want to try again by other methods :)")
            if c=='y':
                book_find()
            else:
                pass
        else:
             print('Book Code:\t',abc[0])
             print('Book Name:\t',abc[1])
             print('Book Author:\t',abc[2])
             print('availability:\t',abc[3])
             

   
    elif a=='name' or a=='NAME':
        b=input("Enter name of the Book")
        s1="select * from lib where book_name=%s"
        val=(b,)
        cursr.execute(s1,val)
        c=cursr.fetchall()
        print("these are the books name",b)
        k=1
        for i in c:
                print(k ,'  \n Book Code : {}     Book Name :{}     Book Author :{}     Availability :{}     '.format(i[0], i[1], i[2], i[3]))
                k+=1
        print("here is the list of all books whose name is : {}".format(b),"and there information")

        x=input("Want to issue a book?? --> type 'y'")
        if x=='y':
            bookissue()
        else:
            pass

    elif a=="author" or a=="AUTHOR":
        b=input("Enter name of the Book")
        s1="select book_name from lib where author=%s"
        val=(b,)
        cursr.execute(s1,val)
        c=cursr.fetchall()
        print("these are the books written by",b)
        for i in c:
            print(i)
        print('which book u are willing to check')


def bookissue():
    s1='insert into issue_data(stu_admsn_no,Stu_Name,Book_No,book_name,issuing_date) values(%s,%s,%s,%s,%s)'
    a=int(input("Enter Student's Admission Number  :--   "))
    x=int(input("Enter Book's Batch Number  :--   "))
    e=input("Enter Today's Date  eg.'YYYY-MM-DD  :--    ")
    s="select name from registration where admssn_no = %s"
    s2="select Book_Name from lib where Book_Code = %s "
    v=(a,)
    v2=(x,)
    cursr.execute(s,v)
    b=cursr.fetchone()
    b=b[0]
    cursr.execute(s2,v2)
    c=cursr.fetchone()
    c=c[0]
    val=(a,b,x,c,e)
    cursr.execute(s1,val)
    try:
        cursr.execute("update lib set availabilty='NOT AVAILABLE' where Book_Code = %s",v2)

        print("successfull")
        db.commit()
    except:
        print("Book Not Issued Yet")
        print("Please re enter the given data")
        bookissue()


def Book_Return():
    
    a=int(input("Enter Student's Admission Number  :--   "))
    x=int(input("Enter Book's Batch Number  :--   "))
    
    s="delete from issue_data where Book_no = %s"
    #s1="delete from issue_data where stu_admsn_no = %s"
    #v1=(a,)
    v=(x,)
    cursr.execute(s,v)
    cursr.execute("update lib set availabilty='AVAILABLE' where Book_Code = %s",v)
    
    print("successfull")
    db.commit()
    

def startover():
    print("do u want to do another query ;)")
    b=input("If yes type 'continue' ")
    return b






#__main__
print("_"*65)
print("KENDRIYA VIDHYALAYA".center(75 , '^'))
print("A.G.C.R Colony".center(99 , '-'))
print()
print("SCHOOL LIBRARY".center(65 , '_'))
print()

print("Hello User  :)  \n To do any query please type it's number")
print("1. Book Entry \n 2. Student Registration \n 3. Book Issue \n 4. Book Return \n 5. Check the availability of a book")
print()
x="continue"
while x=="continue":
    a=int(input("Enter your query number :--  "))
    if a == 1:
        Book_Entry()
        x=startover()
    elif a==2:
        Register_Urself()
        x=startover()
    elif a== 3:
        bookissue()
        x=startover()
    elif a==4:
        Book_Return()
        x=startover()
    elif a==5:
       book_find()
       x=startover()
    else:
        print()
        print("Error: Out of QUERY No. PLEASE TRY AGAIN")
        a='continue'

else :
    print("it was so nice to work with you !!")
    print("Please come again later :)")











