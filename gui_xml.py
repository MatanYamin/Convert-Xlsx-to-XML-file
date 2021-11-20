from tkinter import *
from tkinter import filedialog
import pandas as pd
import converFromCsvToXml as con
list_of_labels = []
list_of_inputs = []
excel_flag = False
folder_selected = ""
columns = 0
rows = 0
# Setting icon of master window
root = Tk()
p1 = PhotoImage(file='acad.png')
root.iconphoto(False, p1)

root.title('המרת קובץ אקסל לקובץ שאלות')
root.geometry("500x700")
xml_name_label = Label(root, text="נבנה על ידי מתן ימין")
xml_name_label.pack()
canvas1 = Canvas(root, width=100, height=70)
canvas1.pack()


def getExcel():
    global df, columns, rows, excel_flag, list_of_labels
    for i in list_of_labels:
        i.destroy()
    import_file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    df = pd.read_excel(import_file_path)
    columns = len(df.columns)
    rows = len(df)
    excel_flag = True
    success = Label(root, text="הקובץ נטען בהצלחה", fg="green")
    success.pack()
    list_of_labels.append(success)


# Upload excel button
browseButton_Excel = Button(text='טען קובץ אקסל', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(50, 50, window=browseButton_Excel)
label = Label(root, bg="white", text=":הערה: קובץ האקסל צריך להיות בן 6 עמודות בסדר הבא\n .שם שאלה, תשובה1, תשובה2, תשובה3, תשובה4, מספר תשובה נכונה\n.אם יש פחות מ 4 תשובות לשאלה, יש להשאיר שדה ריק")
label.pack(padx=0, pady=5)

# Enter user name
enter_user_name_label = Label(root, text=":שם משתמש באקדמיה", font=('helvetica', 10, 'bold'))
enter_user_name_label.pack(padx=0, pady=5)
user_name_input = Entry(root, width=30, justify=RIGHT)
user_name_input.pack()
list_of_inputs.append(user_name_input)

# enter email
enter_email_label = Label(root, text=":מייל של המשתמש האקדמיה", font=('helvetica', 10, 'bold'))
enter_email_label.pack(padx=0, pady=5)

email_input = Entry(root, width=30, justify=RIGHT)
email_input.pack()
list_of_inputs.append(email_input)

# enter file name
xml_name_label = Label(root, text=":שם לקובץ", font=('helvetica', 10, 'bold'))
xml_name_label.pack(padx=0, pady=5)

xml_input = Entry(root, width=30, justify=RIGHT)
xml_input.pack()
list_of_inputs.append(xml_input)

# enter quiz name
quiz_name_label = Label(root, text=":שם החידון כפי שמופיע באתר", font=('helvetica', 10, 'bold'))
quiz_name_label.pack(padx=0, pady=5)

quiz_name = Entry(root, width=30, justify=RIGHT)
quiz_name.pack()
list_of_inputs.append(quiz_name)

# enter slug
quiz_slug_label = Label(root, text=":כינוי החידון כפי שמופיע באתר", font=('helvetica', 10, 'bold'))
quiz_slug_label.pack(padx=0, pady=5)

quiz_slug = Entry(root, width=30, justify=RIGHT)
quiz_slug.pack()
list_of_inputs.append(quiz_slug)


def find_location():
    global folder_selected, list_of_labels
    folder_selected = filedialog.askdirectory()
    if folder_selected != "":
        for i in list_of_labels:
            i.destroy()


address = Button(root, text="בחר לאן תרצה שהקובץ יגיע", command=find_location)
address.pack(padx=15, pady=25)


def close_me():
    exit()


def action():
    global excel_flag, folder_selected, list_of_labels, list_of_inputs
    for i in list_of_labels:
        i.destroy()
    if not excel_flag:
        label1 = Label(root, text="אנא העלה קובץ אקסל", fg="red")
        label1.pack()
        list_of_labels.append(label1)
    if folder_selected == "":
        label0 = Label(root, text="אנא בחר מיקום לקובץ החדש", fg="red")
        label0.pack()
        list_of_labels.append(label0)
    else:
        if folder_selected == "" or email_input.get() == "" or user_name_input.get() == "" or xml_input.get() == "" or quiz_name.get() == "" or quiz_slug.get() == "":
            label2 = Label(root, text="אחד מהשדות חסרים", fg="red")
            label2.pack()
            list_of_labels.append(label2)
        else:
            label_load = Label(root, text="...ההמרה מתבצעת")
            label_load.pack()
            list_of_labels.append(label_load)
            check = con.main_loop(df, quiz_name.get(), quiz_slug.get(), user_name_input.get(), email_input.get(), folder_selected, xml_input.get())
            if check == 1:
                label3 = Label(root, text=" \u2713  " + "ההמרה בוצעה בהצלחה", fg="green")
                label3.pack()
                list_of_labels.append(label3)
                for i in list_of_inputs:
                    i.delete(0, END)
                label4 = Label(root, text=folder_selected + " הקובץ נמצא ב ")
                label4.pack()
                list_of_labels.append(label4)


do_it = Button(root, text="בצע המרה", command=action, bg="green", fg="white", font=('helvetica', 11, 'bold'))
do_it.pack(padx=5, pady=5)


do_it2 = Button(root, text="סגור", command=close_me, fg="red")
do_it2.pack(padx=5, pady=15)


if __name__ == '__main__':
    root.mainloop()
