messages = ['thnks ;)', 'omg :0', 'Great! Thnks a lot :)']
messages_copy = messages[:]
#
def show_messages(messages):
    for message in messages:
        print(message)

#
sent_messages = []
#
def send_messages(messages):
    for message in messages:
        sent_messages.append(message)
        #
        print(message)

#
send_messages(messages_copy)

#
print('\n')

print(messages) #
print(messages_copy) ##
