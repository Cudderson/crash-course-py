# 8-9, 8-10, 8-11
"""More practice working with list in functions"""

def send_messages(messages, sent_messages):
    print("Here are the messages sent:\n")
    while messages:
        sent = messages.pop(0)
        print(f"{sent}")
        sent_messages.append(sent)
    print("\n")


messages = ["Come over", "don't leave", "I miss you"]
sent_messages = []
send_messages(messages, sent_messages)
# "" send_messages(messages[:], sent_messages) "" would pass a copy on the list, maintaining the original.
# This is not efficient though.

print(f"Here are the messages left to send: (should be empty)\n"
      f"{messages}")
print(f"And here are the messages successfully sent:\n"
      f"{sent_messages}")