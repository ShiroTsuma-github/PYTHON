people = {
["red":[255,0,0],"#FF0000"],
['name': "Mark", 'age': 5],
['name': "Pam", 'age': 7]
}

filter(lambda color: color['name'] == 'Pam', people)