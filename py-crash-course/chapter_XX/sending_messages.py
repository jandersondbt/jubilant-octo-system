messages = ['thnks ;)', 'omg :0', 'Great! Thnks a lot :)']

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
show_messages(messages)

#
print('\n')
send_messages(messages)

#
print('\n')
print(messages)
#
print(sent_messages)

