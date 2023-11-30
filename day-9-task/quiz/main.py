import json
class Players:
    players=[]
    sid=0
    file_path="(your_path)\q.json"
    def __init__(self,name):
        self.id=Players.sid
        self.name=name
        self.score=0
        Players.sid+=1

    def add_player(self):
        name=str(input("Enter your name:")).strip().lower()
        if name:
            self.players.append(Players(name))



class Quiz(Players):
    def __init__(self, name):
        super().__init__(name)

    def load_data(self):
        with open(self.file_path,"r") as file:
            return json.load(file)

    def show_question(self,q):
        print(f'''
            Question: {q['question']}\n
            1. {q["options"][0]}  2. {q["options"][1]}
            3. {q["options"][2]}  4. {q["options"][3]}
            ''')
    
    def play(self):
        try:
            ques=self.load_data()
            if ques and len(self.players)>2:
                for q in ques:
                    self.show_question(q)
                    for p in self.players:
                        print(f"{p.name}'s turn\n ")
                        ans=int(input("Enter your answer sn: "))
                        if q["options"][ans-1] == q['correct_answer']:
                            p.score+=1
                            print("Correct answer".center(50,"*"))
                            break
                        else:
                            print("Wrong answer".center(50,"*"))
                        
                winner=""
                score=0
                for p in self.players:
                    if p.score>score:
                        score=p.score
                        winner=p.name
                if winner and score>0:
                    print(f"winner is {winner} with score {score}")

            else:
                print("Players  not available")
                self.add_player()
        except Exception as e:
            print(e)


q=Quiz("")

    
while True:
    command=str(input("Enter your choice (add,play,exit):")).strip().lower()
    match command:
            case "add":
                q.add_player()
            case "play":
                q.play()
            case "exit":
                break