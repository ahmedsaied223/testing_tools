import subprocess
from prettytable import PrettyTable


def configure_kubectl_context(cluster_name, rdei_server, token, namespace):
    """
    Configures the Kubernetes context using kubectl commands.
    """
    try:
        # Set the cluster
        subprocess.run(
            ["kubectl", "config", "set-cluster", cluster_name, "--server", rdei_server, "--insecure-skip-tls-verify"],
            check=True
        )
        
        # Set the credentials
        subprocess.run(
            ["kubectl", "config", "set-credentials", cluster_name, "--token", token],
            check=True
        )
        
        # Set the context
        subprocess.run(
            ["kubectl", "config", "set-context", cluster_name, "--cluster", cluster_name, "--namespace", namespace, "--user", cluster_name, "--insecure-skip-tls-verify"],
            check=True
        )
        
        # Use the context
        subprocess.run(
            ["kubectl", "config", "use-context", cluster_name],
            check=True
        )
        
        print(f"Kubectl context '{cluster_name}' configured and set successfully.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to configure kubectl context: {e}")
    
def get_pods(namespace):
    """
    Runs `kubectl get pods` for the specified namespace and returns the list of pods.
    
    Args:
        namespace (str): The Kubernetes namespace to query pods from.
    
    Returns:
        str: The output of the `kubectl get pods` command.
    
    Raises:
        RuntimeError: If the `kubectl get pods` command fails.
    """
    try:
        result = subprocess.run(
            ["kubectl", "get", "pods", "-n", namespace],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("List of Pods:")
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to get pods: {e.stderr}")
    

def describe_pod(namespace, podname):
    """
    Finds a pod by its name prefix, fetches its labels, and prints them in a table.
    
    Args:
        namespace (str): The Kubernetes namespace to search in.
        prefix (str): The prefix of the pod name to search for.
    
    Returns:
        None: Prints the labels in a table.
    
    Raises:
        RuntimeError: If no pod is found or the `kubectl describe pod` command fails.
    """
    try:
        # Get the list of pods
        result = subprocess.run(
            ["kubectl", "get", "pods", "-n", namespace, "-o", "jsonpath={.items[*].metadata.name}"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        pod_names = result.stdout.split()

        # Find the first pod that starts with the given prefix
        target_pod = next((name for name in pod_names if name.startswith(podname)), None)
        if not target_pod:
            raise RuntimeError(f"No pod found with prefix '{podname}' in namespace '{namespace}'.")

        # Get the pod details in JSON format
        pod_details = subprocess.run(
            ["kubectl", "get", "pod", target_pod, "-n", namespace, "-o", "json"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Parse the labels from the JSON output
        import json
        pod_data = json.loads(pod_details.stdout)
        labels = pod_data.get("metadata", {}).get("labels", {})
        
        # Extract specific labels
        amr_version = labels.get("amrVersion", "N/A")
        app = labels.get("app", "N/A")
        version = labels.get("version", "N/A")
        
        return {
            "app": app,
            "version": version
        }
        
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to execute kubectl command: {e.stderr}")

