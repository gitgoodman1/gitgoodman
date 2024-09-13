import pulsar

client = pulsar.Client('pulsar://localhost:6650')  
producer = client.create_producer('subscribe-for-more')

print("Type your messages to send to Pulsar. Type 'exit' to quit.")

while True:
    message = input("Enter message: ")
    
    if message.lower() == 'exit':
        print("Exiting...")
        break
    
    producer.send(message.encode('utf-8'))
    print(f"Message sent: {message}")

client.close()