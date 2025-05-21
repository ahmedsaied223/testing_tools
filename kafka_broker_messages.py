from confluent_kafka import Producer, Consumer, KafkaException, KafkaError
import unittest
import json
import time

class KafkaMessageTest(unittest.TestCase):
    KAFKA_BROKER = "localhost:9092"  # Replace with your Kafka broker address
    TOPIC = "trading-app-topic"      # Replace with your Kafka topic name

    @classmethod
    def setUpClass(cls):
        # Set up Kafka producer
        cls.producer = Producer({'bootstrap.servers': cls.KAFKA_BROKER})
        # Set up Kafka consumer
        cls.consumer = Consumer({
            'bootstrap.servers': cls.KAFKA_BROKER,
            'group.id': 'trading-app-test-group',
            'auto.offset.reset': 'earliest'
        })
        cls.consumer.subscribe([cls.TOPIC])

    def test_produce_and_consume_message(self):
        """Test producing and consuming a Kafka message."""
        # Create a test message
        test_message = {
            "trade_id": "12345",
            "stock": "AAPL",
            "quantity": 10,
            "price": 150.0,
            "action": "BUY"
        }

        # Produce the message
        self.producer.produce(self.TOPIC, key="test-key", value=json.dumps(test_message))
        self.producer.flush()

        # Consume the message
        msg = None
        start_time = time.time()
        while time.time() - start_time < 10:  # Wait up to 10 seconds
            msg = self.consumer.poll(1.0)  # Poll for messages
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            else:
                break

        self.assertIsNotNone(msg, "No message received from Kafka.")
        received_message = json.loads(msg.value().decode('utf-8'))
        self.assertEqual(received_message, test_message, "Received message does not match the sent message.")

    @classmethod
    def tearDownClass(cls):
        cls.consumer.close()

if __name__ == "__main__":
    unittest.main()
