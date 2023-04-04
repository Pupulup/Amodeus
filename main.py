import openai
from telegram.ext import Updater, MessageHandler


API_TOKEN = '6012611381:AAEksVc4WZ-LEPEgjElNSFbi29osua_ir8Y'
openai_api_key = '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'


def ask_gpt(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message


def echo(update, context):
    response = ask_gpt(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


updater = Updater(token=API_TOKEN, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
updater.start_polling()
updater.idle()
