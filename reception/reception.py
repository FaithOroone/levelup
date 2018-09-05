def registration_checker(name):
    file1=open('names/vip_list.txt', 'r')
    content_list1=file1.readlines()
    file1.close()

    file2=open('name/ordonary_list.txt', 'r')
    content_list1=file1.readlines()
    file1.close()
    for test_name in content_list1:
        if name.lower() in test_name.lower():
            return(test_name.strip('\n')+',vip ')

    for test_name in content_list1:
        if name.lower() in test_name.lower():
            return(test_name.strip('\n')+',ordinary')
    return 'Not Registered'

    print(registration_checker(input('Enter name:')))




    from flask import Flask, Request, jsonify, json
import sys

sys.path.append("/usr/local/bin/flask")

app = Flask(__name__)
@app.route('/levelup/learners',methods=['GET'])
def get_learners():
    learners_list = {'keren':[{'age':2, 'sex':'female', 'class':'baby'}], 'faith':[{'age':24, 'sex':'female', 'class':'s4'}],'jacob':[{'age':30, 'sex':'male', 'class':'s6'}]}
    if len(learners_list)==0:
        return ({"message":"no students"}), 400
        return jsonify({"learners":learners_list, "number":len(learners_list)}), 200



if __name__=='__main__':
    app.run(debug = True, port=5000)
