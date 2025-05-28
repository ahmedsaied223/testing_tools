import unittest
from kubernetes import client, config
from kubernetes.client.rest import ApiException

class KubernetesConfigMapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load kube config from default location or in-cluster config
        try:
            config.load_kube_config()
        except Exception:
            config.load_incluster_config()
        cls.v1 = client.CoreV1Api()
        cls.namespace = "default"  # Change if your ConfigMap is in another namespace
        cls.configmap_name = "your-configmap-name"  # Change to your ConfigMap name

    def test_configmap_exists(self):
        """Test that the ConfigMap exists in the namespace."""
        try:
            configmap = self.v1.read_namespaced_config_map(
                name=self.configmap_name,
                namespace=self.namespace
            )
            self.assertIsNotNone(configmap)
        except ApiException as e:
            self.fail(f"ConfigMap not found: {e}")

    def test_configmap_data(self):
        """Test that the ConfigMap contains expected keys."""
        try:
            configmap = self.v1.read_namespaced_config_map(
                name=self.configmap_name,
                namespace=self.namespace
            )
            # Example: Check for a key called 'APP_ENV'
            self.assertIn('APP_ENV', configmap.data)
            self.assertEqual(configmap.data['APP_ENV'], 'production')  # Change as needed
        except ApiException as e:
            self.fail(f"ConfigMap not found or missing data: {e}")

if __name__ == "__main__":
    unittest.main()
