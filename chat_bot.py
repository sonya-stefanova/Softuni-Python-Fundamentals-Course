from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Nice to meet you! You got in contact with the BulgarianPoker bot.\nHow can we help you?", ]
    ],
    [
        r"(.*) (missing chips|bought chips|chips missing|not received chips|I didn't get my poker chips)",
        ["Please, don't worry about the receipt of your poker chips. Would you please tell us your ID in the game and the Google purchase number and we will check the status of your purchase as soon as possible. We kindly ask for your patience!", ]
    ],
    [
        r'i have a problem (.*)',
        ["We're always available to help you out with whatever problem you meet. But before we go on, would you please tell us what is your ID?", ]
    ],
    [
        r"(.*) (blocked|terminated|banned)",
        ["If your profile has been blocked, please let us know your ID. Then, we will check the reason for this. "]
    ],
    [
        r"(.*) cheating",
        ["If you think that another player is cheating, kidnly tell us what is his ID. We will check the logs and take immidiate actions. "]
    ],
    [
        r"(.*) id ",
        ["Thanks for the information! We will check the status of the problem, now. "]
    ],
    [
        r"i lost my tourist account",
        ["We are really sorry to hear this. Not everything is lost, though! If you know your ID, date of registration along with any other important information about this, we will help you transfer the chips to your Facebook profile."]
    ],
[
        r"my chat is (.*) (blocked|terminated|banned)",
        ["We are really sorry to hear this. This is a temporary measure against your bad behavior in the chat. It ends in 1 week after which period you will be able to chat again. Kindly, observe our Community Rules in the Game's Settings page"]
    ],

    [
        r"end",
        ["Thanks for your kind cooperation. Wishing you luck in the game", "It was nice talking to you. Good luck and many winning!", ]
    ],
    [
        r"(.*)",
        ['Please, let us know your profile ID', 'Good luck!', ]
    ],
[
        r"(thanks | thanks | thank you | 10x | great | thank you) (.*)",
        ['You are welcome! Good luck!', ]
    ],
]

# default message at the start of chat
print("Please use lowercase English language to start a conversation. "
      "Type end to leave.\nHi, there!\n")

# Create Chat Bot
chat = Chat(pairs, reflections)
# Start conversation
chat.converse()