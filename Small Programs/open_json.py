import json

with open ("questions.json", 'r') as file:
    content = file.read()

#This prints out the content as a string, which makes it very useless to us.
#print(type(content))

data = json.loads(content)

#print(type(data))
#print('hi')

for question in data:
    #test_question = input(question["question_text"] + "\n" + question['alternatives'])
    #print(test_question, '\n', question['alternatives'])
    print(question["question_text"])
    [print(str(index + 1) + "." + alternative) for index, alternative in enumerate(question["alternatives"])]
    
    while True:
        response = input('please select the number of you answer\n')
        
        try:
            if int(response.strip()) == question['correct_answer']:
                print("That is correct!")
                break
            else:
                print(f"I'm sorry, the correct answer is {question['correct_answer']}")
                break
        except ValueError:
            print("You must enter a number")
    
