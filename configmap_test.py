import unittest
from unittest.mock import MagicMock
from kubernetes.client import V1ConfigMap, V1ObjectMeta, V1DeleteOptions
from kubernetes.client.rest import ApiException


class TestConfigMapOperations(unittest.TestCase):
    def setUp(self):
        # Mock Kubernetes client
        self.mock_client = MagicMock()

    def test_create_config_map(self):
        # Mock data for the ConfigMap
        config_map_name = "streams"
        namespace = "test"
        data = {
            "data.json": "some-json-data",
            "data.gzip": b"some-gzipped-data",
        }

        # Mock the create_namespaced_config_map method
        self.mock_client.create_namespaced_config_map.return_value = V1ConfigMap(
            metadata=V1ObjectMeta(name=config_map_name, namespace=namespace),
            data={"data.json": data["streams.json"]},
            binary_data={"data.gzip": data["streams.gzip"]},
        )

        # Simulate creating the ConfigMap
        created = self.mock_client.create_namespaced_config_map(namespace, V1ConfigMap())
        self.assertEqual(created.metadata.name, config_map_name)
        self.assertIn("data.json", created.data)
        self.assertIn("data.gzip", created.binary_data)

    def test_delete_config_map(self):
        # Mock data for the ConfigMap
        config_map_name = "seuss"
        namespace = "testns"

        # Mock the delete_namespaced_config_map method
        self.mock_client.delete_namespaced_config_map.return_value = None

        # Simulate deleting the ConfigMap
        self.mock_client.delete_namespaced_config_map(namespace, config_map_name, V1DeleteOptions())
        self.mock_client.delete_namespaced_config_map.assert_called_with(
            namespace, config_map_name, V1DeleteOptions()
        )

    def test_get_config_map(self):
        # Mock data for the ConfigMap
        config_map_name = "configmap_name"
        namespace = "NS"
        data = {"one": "fish", "two": "fish"}
        binary_data = {"red": b"fish", "blue": b"fish"}

        # Mock the read_namespaced_config_map method
        self.mock_client.read_namespaced_config_map.return_value = V1ConfigMap(
            metadata=V1ObjectMeta(name=config_map_name, namespace=namespace),
            data=data,
            binary_data=binary_data,
        )

        # Simulate retrieving the ConfigMap
        found = self.mock_client.read_namespaced_config_map(namespace, config_map_name)
        self.assertEqual(found.data["one"], "fish")
        self.assertEqual(found.data["two"], "fish")
        self.assertEqual(found.binary_data["red"], b"fish")
        self.assertEqual(found.binary_data["blue"], b"fish")

    def test_update_config_map(self):
        # Mock data for the ConfigMap
        config_map_name = "any-name"
        namespace = "ns"
        updated_data = {"one": "bird", "red": "fish", "blue": "fish", "two": b"bird"}

        # Mock the patch_namespaced_config_map method
        self.mock_client.patch_namespaced_config_map.return_value = V1ConfigMap(
            metadata=V1ObjectMeta(name=config_map_name, namespace=namespace),
            data={"one": updated_data["one"], "red": updated_data["red"], "blue": updated_data["blue"]},
            binary_data={"two": updated_data["two"]},
        )

        # Simulate updating the ConfigMap
        updated = self.mock_client.patch_namespaced_config_map(namespace, config_map_name, V1ConfigMap())
        self.assertEqual(updated.data["one"], "bird")
        self.assertEqual(updated.data["red"], "fish")
        self.assertEqual(updated.data["blue"], "fish")
        self.assertEqual(updated.binary_data["two"], b"bird")

    def test_watch_config_map(self):
        # Mock the watch functionality
        from kubernetes.watch import Watch

        mock_watch = MagicMock(spec=Watch)
        self.mock_client.watch.return_value = mock_watch

        # Simulate watching a ConfigMap
        mock_watch.data.return_value = iter([
            {"type": "ADDED", "object": V1ConfigMap(metadata=V1ObjectMeta(name="seuss"))},
            {"type": "MODIFIED", "object": V1ConfigMap(metadata=V1ObjectMeta(name="seuss"))},
            {"type": "DELETED", "object": V1ConfigMap(metadata=V1ObjectMeta(name="seuss"))},
        ])

        events = list(mock_watch.stream(self.mock_client.list_namespaced_config_map, namespace="testns"))
        self.assertEqual(events[0]["type"], "ADDED")
        self.assertEqual(events[1]["type"], "MODIFIED")
        self.assertEqual(events[2]["type"], "DELETED")


if __name__ == "__main__":
    unittest.main()
