# 8-9 Messages

messages = ['hello', 'how are you doing', "I'm learing Python.", 'See you later']

def show_messages(messages):
    """_summary_
        display all messages to be sent one by one.
    Args:
        messages (list[str]): message to be sent
    """
    print(f"These are messages to be sent: ")
    for message in messages:
        print(message)

show_messages(messages)

# 8-10 Sending Messages
print('\n=== 8-10 ===\n')

messages = ['hello', 'how are you doing', "I'm learing Python.", 'See you later']
sent_messages = []

def send_messages(messages):
    """_summary_
        send messages and move them to sent_message list.
    Args:
        messages (list[str]): message to be sent
    """
    while messages:
        message = messages.pop(0)
        print(f"Sending \"{message}\"")
        sent_messages.append(message)

# send_messages(messages)
# print(messages)
# print(sent_messages)

# 8-11 Archived Messages

send_messages(messages[:])
print(messages)
print(sent_messages)