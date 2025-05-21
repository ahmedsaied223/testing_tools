import csv
import re
import os

def parse_endpoints(endpoints_csv_path):
    """
    Parse the endpoints CSV file to map endpoints to site, namespace, and pod_name.

    Args:
        endpoints_csv_path (str): Path to the endpoints CSV file.

    Returns:
        dict: A mapping of endpoint to (site, namespace, pod_name).
    """
    endpoint_mapping = {}
    try:
        with open(endpoints_csv_path, mode="r") as endpoints_csv:
            reader = csv.DictReader(endpoints_csv)
            for row in reader:
                endpoint = row.get("endpoint")
                if not endpoint:
                    continue

                # Use regex to extract pod_name, namespace, and site
                match = re.match(r"http://([^-]+-[^-]+)-([^-]+-[^-]+-\d+)-(.+)\.net", endpoint)
                if match:
                    pod_name, namespace, site = match.groups()
                    endpoint_mapping[endpoint] = (pod_name,namespace,site )
                else:
                    print(f"Could not parse endpoint: {endpoint}")  # Debug log
        return endpoint_mapping
    except FileNotFoundError:
        raise RuntimeError(f"Endpoints file not found: {endpoints_csv_path}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while parsing the endpoints file: {e}")

def merge_csvs(output_csv_path, output_missing_metrics_csv_path, endpoints_csv_path, merged_csv_path):
    """
    Merge output.csv with output_missing_metrics.csv based on site, namespace, and pod_name.

    Args:
        output_csv_path (str): Path to the output.csv file.
        output_missing_metrics_csv_path (str): Path to the output_missing_metrics.csv file.
        endpoints_csv_path (str): Path to the endpoints.csv file.
        merged_csv_path (str): Path to the merged output CSV file.

    Returns:
        None
    """
    try:
        # Parse the endpoints CSV to map endpoints to site, namespace, and pod_name
        endpoint_mapping = parse_endpoints(endpoints_csv_path)
        print(f"Parsed endpoint mapping: {endpoint_mapping}")  # Debug log

        # Parse the missing metrics CSV
        missing_metrics = {}
        with open(output_missing_metrics_csv_path, mode="r") as missing_metrics_csv:
            reader = csv.DictReader(missing_metrics_csv)
            for row in reader:
                endpoint = row.get("endpoint").strip().lower()  # Normalize endpoint
                missing_metrics[endpoint] = row.get("missing_metrics", "")
        print(f"Parsed missing metrics: {missing_metrics}")  # Debug log

        # Open the merged CSV file for writing
        with open(merged_csv_path, mode="w", newline="") as merged_csv:
            fieldnames = ["site", "namespace", "pod_name", "app", "version", "missing_metrics"]
            writer = csv.DictWriter(merged_csv, fieldnames=fieldnames)
            writer.writeheader()

            # Read the output.csv file and merge with missing metrics
            with open(output_csv_path, mode="r") as output_csv:
                reader = csv.DictReader(output_csv)
                for row in reader:
                    site = row.get("site")
                    namespace = row.get("namespace")
                    pod_name = row.get("pod_name")
                    # Find the corresponding endpoint
                    endpoint = None
                    for ep, (ep_pod_name, ep_namespace,ep_site, ) in endpoint_mapping.items():
                        if (site and namespace and pod_name and 
                            site.strip().lower() == ep_site.strip().lower() and 
                            namespace.strip().lower() == ep_namespace.strip().lower() and 
                            pod_name.strip().lower() == ep_pod_name.strip().lower()):
                            endpoint = ep
                            print(f"Matched endpoint: {endpoint} for site={site}, namespace={namespace}, pod_name={pod_name}")  # Debug log
                            break

                    # Add missing metrics if available
                    if endpoint:
                        row["missing_metrics"] = missing_metrics.get(endpoint, "N/A")
                        print(f"Missing metrics for endpoint {endpoint}: {row['missing_metrics']}")  # Debug log
                    else:
                        row["missing_metrics"] = "N/A"
                        print(f"No matching endpoint found for site={site}, namespace={namespace}, pod_name={pod_name}")  # Debug log

                    writer.writerow(row)

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
  
    # Paths to the input and output CSV files
    output_csv_path = "pod_output_details.csv"  # Replace with the actual path to your output.csv file
    output_missing_metrics_csv_path = "output_missing_metrics.csv"  # Replace with the actual path to your output_missing_metrics.csv file
    endpoints_csv_path = "endpoints.csv"  # Replace with the actual path to your endpoints.csv file
    merged_csv_path = "merged_output.csv"  # Replace with the desired path for the merged output CSV file

    # Merge the CSV files
    merge_csvs(output_csv_path, output_missing_metrics_csv_path, endpoints_csv_path, merged_csv_path)
