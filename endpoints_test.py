import unittest
from unittest.mock import MagicMock
from kubernetes.client import CoreV1Api, V1Endpoints, V1ObjectMeta, V1EndpointSubset, V1EndpointAddress, V1EndpointPort


class TestKubernetesEndpoints(unittest.TestCase):
    def setUp(self):
        # Mock Kubernetes CoreV1Api client
        self.mock_client = MagicMock(spec=CoreV1Api)

    def test_get_endpoints(self):
        # Define the test data
        namespace = "NS"
        endpoint_name = "THE ENDPOINT NAME"
        mock_endpoints = V1Endpoints(
            metadata=V1ObjectMeta(name=endpoint_name, namespace=namespace),
            subsets=[
                V1EndpointSubset(
                    addresses=[
                        V1EndpointAddress(ip="123.456.789.101", node_name="00.00.000.00"),
                        V1EndpointAddress(ip="192.168.229.77", node_name="00.00.00.00"),
                        V1EndpointAddress(ip="192.168.237.236", node_name="00.00.0.0"),
                    ],
                    ports=[
                        V1EndpointPort(name="portsname", port=000, protocol="TCP"),
                    ],
                )
            ],
        )

        # Mock the read_namespaced_endpoints method
        self.mock_client.read_namespaced_endpoints.return_value = mock_endpoints

        # Function to get endpoints
        def get_endpoints(client, name, namespace):
            endpoints = client.read_namespaced_endpoints(name, namespace)
            result = []
            for subset in endpoints.subsets:
                for address in subset.addresses:
                    for port in subset.ports:
                        result.append(f"http://{address.ip}:{port.port}")
            return result

        # Call the function and assert the result
        endpoints = get_endpoints(self.mock_client, endpoint_name, namespace)
        self.assertEqual(len(endpoints), 3)
        self.assertEqual(endpoints[0], "endpoints")
        self.assertEqual(endpoints[1], "endoints")
        self.assertEqual(endpoints[2], "endpoints")


if __name__ == "__main__":
    unittest.main()
