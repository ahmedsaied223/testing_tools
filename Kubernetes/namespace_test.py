import unittest
from kubernetes import client, config
from kubernetes.client.rest import ApiException

class NamespaceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load kube config from default location or in-cluster config
        try:
            config.load_kube_config()
        except Exception:
            config.load_incluster_config()
        cls.v1 = client.CoreV1Api()
        cls.namespace = "default"  # Change to the namespace you want to test

    def test_namespace_exists(self):
        """Test that the namespace exists."""
        try:
            ns = self.v1.read_namespace(name=self.namespace)
            self.assertIsNotNone(ns)
            self.assertEqual(ns.metadata.name, self.namespace)
        except ApiException as e:
            self.fail(f"Namespace '{self.namespace}' not found: {e}")

    def test_namespace_status_active(self):
        """Test that the namespace status is Active."""
        try:
            ns = self.v1.read_namespace(name=self.namespace)
            self.assertEqual(ns.status.phase, "Active")
        except ApiException as e:
            self.fail(f"Namespace '{self.namespace}' not found or not active: {e}")

if __name__ == "__main__":
    unittest.main()
