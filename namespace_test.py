import unittest
from unittest.mock import MagicMock
from kubernetes.client import CoreV1Api, V1Namespace, V1ObjectMeta
from kubernetes.client.rest import ApiException


class TestKubernetesNamespace(unittest.TestCase):
    def setUp(self):
        # Mock Kubernetes CoreV1Api client
        self.mock_client = MagicMock(spec=CoreV1Api)

    def test_get_namespace(self):
        # Define the namespace to test
        namespace_name = "testns"

        # Mock the namespace object
        mock_namespace = V1Namespace(
            metadata=V1ObjectMeta(name=namespace_name)
        )

        # Configure the mock client to return the mock namespace
        self.mock_client.read_namespace.return_value = mock_namespace

        # Function to get namespace
        def get_namespace(client, namespace_name):
            try:
                return client.read_namespace(namespace_name)
            except ApiException as e:
                return None

        # Call the function and assert the result
        found = get_namespace(self.mock_client, namespace_name)
        self.assertIsNotNone(found)
        self.assertEqual(namespace_name, found.metadata.name)

    def test_get_namespace_not_found(self):
        # Define a namespace that does not exist
        namespace_name = "nonexistent"

        # Configure the mock client to raise an ApiException for a missing namespace
        self.mock_client.read_namespace.side_effect = ApiException(status=404, reason="Not Found")

        # Function to get namespace
        def get_namespace(client, namespace_name):
            try:
                return client.read_namespace(namespace_name)
            except ApiException as e:
                if e.status == 404:
                    return None
                raise

        # Call the function and assert the result
        found = get_namespace(self.mock_client, namespace_name)
        self.assertIsNone(found)


if __name__ == "__main__":
    unittest.main()
