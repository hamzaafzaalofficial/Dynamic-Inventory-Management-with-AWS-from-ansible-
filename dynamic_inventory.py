import boto3
import json

def get_ec2_instances():
    # Create an EC2 client
    ec2_client = boto3.client('ec2')
    
    # Describe EC2 instances
    instances = ec2_client.describe_instances()
    
    # Initialize lists and sets to store data
    ip_addresses = []
    regions = set()
    tags = set()

    # Loop through reservations and instances to extract details
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            # Check if the instance has a public IP address
            if 'PublicIpAddress' in instance:
                ip_addresses.append(instance['PublicIpAddress'])
                
            # Add the availability zone to the regions set
            regions.add(instance['Placement']['AvailabilityZone'])
            
            # Extract tags and add them to the tags set
            for tag in instance.get('Tags', []):
                tags.add(f"{tag['Key']}: {tag['Value']}")

    # Constructing inventory structure
    inventory_data = {
        "IP_Addresses": ip_addresses,
        "Regions": list(regions),
        "Tags": list(tags)
    }
    
    # Print the inventory data in JSON format
    print(json.dumps(inventory_data, indent=4))

if __name__ == "__main__":
    get_ec2_instances()
