import pandas as pd
import os

final_string = ""


def create_start(user_name, user_email):
    """This has to be called when we start to build the quiz. has version number
     and details about loading to academy page"""
    global final_string
    final_string += '<?xml version="1.0" encoding="UTF-8" ?>\n\n'
    final_string += '<rss version="2.0"\n\t'
    final_string += 'xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"\n\t'
    final_string += 'xmlns:content="http://purl.org/rss/1.0/modules/content/"\n\t'
    final_string += 'xmlns:wfw="http://wellformedweb.org/CommentAPI/"\n\t'
    final_string += 'xmlns:dc="http://purl.org/dc/elements/1.1/"\n\t'
    final_string += 'xmlns:wp="http://wordpress.org/export/1.2/">\n\n\t'
    final_string += "<channel>\n\t"
    final_string += "<wp:wxr_version>1.2</wp:wxr_version>\n\n\t\t"
    final_string += "<wp:author>\n\t\t\t"
    final_string += "<wp:author_id>31</wp:author_id>\n\t\t\t"
    final_string += "<wp:author_login><![CDATA["+user_name+"]]></wp:author_login>\n\t\t\t"
    final_string += "<wp:author_email><![CDATA["+user_email+"]]></wp:author_email>\n\t\t\t"
    final_string += "<wp:author_display_name><![CDATA["+user_name+"]]></wp:author_display_name>\n\t\t\t"
    final_string += "<wp:author_first_name><![CDATA["+user_name+"]]></wp:author_first_name>\n\t\t\t"
    final_string += "<wp:author_last_name><![CDATA["+user_name+"]]></wp:author_last_name>\n\t\t"
    final_string += "</wp:author>\n\n\n\t\t"


def start_item(q_name, quiz_name, slug, user_name):
    """every item is a question. every iteration this is being called"""
    global final_string
    final_string += "<item>\n\t\t\t"
    final_string += "<title>" + q_name + "</title>\n\t\t\t"
    final_string += "<dc:creator><![CDATA["+user_name+"]]></dc:creator>\n\t\t\t"
    final_string += "<wp:comment_status><![CDATA[closed]]></wp:comment_status>\n\t\t\t"
    final_string += "<wp:ping_status><![CDATA[closed]]></wp:ping_status>\n\t\t\t"
    final_string += "<wp:status><![CDATA[publish]]></wp:status>\n\t\t\t"
    final_string += "<wp:post_type><![CDATA[question]]></wp:post_type>\n\t\t\t"
    final_string += '<category domain="chidon" nicename="'+slug+'"><![CDATA['+quiz_name+']]></category>\n\t\t\t'
    final_string += "<wp:postmeta>\n\t\t\t\t"
    final_string += "<wp:meta_key><![CDATA[_answers]]></wp:meta_key>\n\t\t\t\t"
    final_string += "<wp:meta_value><![CDATA[field_5fc3c2ce90e5f]]></wp:meta_value>\n\t\t\t"
    final_string += "</wp:postmeta>\n\t\t\t"


def crating_answers(answers, number_of_questions):
    global final_string
    for i in range(number_of_questions):
        final_string += "<wp:postmeta>\n\t\t\t\t"
        final_string += "<wp:meta_key><![CDATA[_answers_"+str(i)+"_answer]]></wp:meta_key>\n\t\t\t\t"
        final_string += "<wp:meta_value><![CDATA[field_5fc3c2e490e60]]></wp:meta_value>\n\t\t\t"
        final_string += "</wp:postmeta>\n\t\t\t\t"
        final_string += "<wp:postmeta>\n\t\t\t\t"
        final_string += "<wp:meta_key><![CDATA[_answers_"+str(i)+"_תשובה_נכונה]]></wp:meta_key>\n\t\t\t\t"
        final_string += "<wp:meta_value><![CDATA[field_5fc3c2fa90e61]]></wp:meta_value>\n\t\t\t"
        final_string += "</wp:postmeta>\n\t\t\t"
    final_string += "<wp:postmeta>\n\t\t\t\t"
    final_string += "<wp:meta_key><![CDATA[answers]]></wp:meta_key>\n\t\t\t\t"
    final_string += "<wp:meta_value><![CDATA[" + str(number_of_questions) + "]]></wp:meta_value>\n\t\t\t"
    final_string += "</wp:postmeta>\n\t\t\t"
    for j in range(number_of_questions):
        final_string += "<wp:postmeta>\n\t\t\t\t"
        final_string += "<wp:meta_key><![CDATA[answers_" + str(j) + "_answer]]></wp:meta_key>\n\t\t\t\t"
        final_string += "<wp:meta_value><![CDATA[" + answers[j] + "]]></wp:meta_value>\n\t\t\t"
        final_string += "</wp:postmeta>\n\t\t\t"


def right_answers(num_of_q, correct):
    """creating the right answer"""
    global final_string
    temp = 0
    for i in range(num_of_q):
        if i+1 == correct:
            temp = 1
        final_string += "<wp:postmeta>\n\t\t\t\t"
        final_string += "<wp:meta_key><![CDATA[answers_"+ str(i) +"_תשובה_נכונה]]></wp:meta_key>\n\t\t\t\t"
        final_string += "<wp:meta_value><![CDATA["+str(temp)+"]]></wp:meta_value>\n\t\t\t"
        final_string += "</wp:postmeta>\n\t\t\t"
        temp = 0


def end_item():
    global final_string
    final_string += "\n\t\t</item> \n\t\t"


def check_how_many_questions(df, row):
    questions_num = 4
    if type(df.loc[row][4]) == float:
        questions_num += -1
        if type(df.loc[row][3]) == float:
            questions_num += -1
            if type(df.loc[row][2]) == float:
                questions_num += -1
                if type(df.loc[row][1] == float):
                    questions_num += -1
    return questions_num


def save_to_xml(address, name):
    global final_string
    save_path = str(address)
    file_name = str(name)+'.xml'
    completeName = os.path.join(save_path, file_name)
    with open(completeName, "w") as file:
        file.write(final_string)
        file.close()


def main_loop(df, quiz_name, slug, user_name, user_email, address, file_name):
    global final_string
    columns = len(df.columns)
    rows = len(df)
    # quiz_name is the name of the quiz inside the academy wordpress page
    # slug is the name of the nickname inside the quiz in the academy
    question_name, ans1, ans2, ans3, ans4, correct_answer = 0, 1, 2, 3, 4, 5
    answers_array = []
    # first we add the attributes data with "create_start". we need to call this only once.
    create_start(user_name, user_email)
    for row in range(rows):
        # every iteration we check how many answers we have to question.
        num_of_answers = check_how_many_questions(df, row)
        # here we are adding to answers_array all of the answers
        for i in range(1, num_of_answers+1):
            answers_array.append(df.loc[row][i])
        # creating the item with the question name.
        start_item(df.loc[row][question_name], quiz_name, slug, user_name)
        # Here we are creating the number of answers
        crating_answers(answers_array, num_of_answers)
        # clearing the array for the next answers row
        answers_array.clear()
        # Defining the right answer
        right_answers(num_of_answers, df.loc[row][correct_answer])
        end_item()
    # This is the last row when we finish with all the questions
    final_string += "\n\n\t</channel>\n</rss>"
    save_to_xml(address, file_name)
    return 1


# if __name__ == '__main__':
#     exit()

