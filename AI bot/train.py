from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

bot = ChatBot("Shrek")

bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    "chatterbot.corpus.english.greetings",
	"chatterbot.corpus.english.conversations",
    "./chatterbot-corpus/chatterbot_corpus/data/custom/myown.yml"
)
