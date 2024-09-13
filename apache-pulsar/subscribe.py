import pulsar

client = pulsar.Client('pulsar://localhost:6650') 
consumer = client.subscribe('subscribe-for-more', subscription_name='my-sub')

while True:
    msg = consumer.receive()
    print(f"Received message: '{msg.data().decode('utf-8')}'")
    
    consumer.acknowledge(msg)

client.close()