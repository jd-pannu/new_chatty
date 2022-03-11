from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__) 
english_bot = ChatBot("Chatterbot", storage_adapter='chatterbot.storage.SQLStorageAdapter', logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }, 'chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.UnitConversion'],)
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("data/twice.yml")
trainer.train("data/tzuyu.yml")
trainer.train("data/jihyo.yml")
trainer.train("data/nayeon.yml")
trainer.train("data/sana.yml")
trainer.train("data/dahyun.yml")
trainer.train("data/chaeyoung.yml")
trainer.train("data/momo.yml")
trainer.train("data/mina.yml")
trainer.train("data/jeongyeon.yml")

trainer.train("chatterbot.corpus.english")
trainer.train("data/thanks.yml")



@app.route("/")
def index():
     return render_template("index.html") #to send context to html

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg") #get data from input,we write js  to index.html
     return str(english_bot.get_response(userText))


if __name__ == "__main__":
     app.run(debug = True)


