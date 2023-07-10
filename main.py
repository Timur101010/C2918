# мессенджер
class User:
    def __init__(self, name):
        self.name = name
        self.messages = []

    def send_message(self, content, recipient):
        message = Message(content, self, recipient)
        self.messages.append(message)
        recipient.receive_message(message)

    def receive_message(self, message):
        self.messages.append(message)

    def get_all_messages(self):
        return self.messages


class Message:
    def __init__(self, content, sender, recipient):
        self.content = content
        self.sender = sender
        self.recipient = recipient


# Create users
user1 = User("Alice")
user2 = User("Bob")

# Send messages
user1.send_message("Hello Bob!", user2)
user2.send_message("Hi Alice!", user1)

# Get all messages for user1 and user2
user1_messages = user1.get_all_messages()
user2_messages = user2.get_all_messages()

# Print the messages
print("Messages for", user1.name)
for message in user1_messages:
    print(f"{message.sender.name}: {message.content}")

print("\nMessages for", user2.name)
for message in user2_messages:
    print(f"{message.sender.name}: {message.content}")
