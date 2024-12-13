# Dynamic-Inventory-Management-with-AWS-from-ansible-

Objective
Use Ansible's dynamic inventory script to retrieve and categorize AWS EC2 instances based on tags or regions.



Step 1: Create a Python Script for Dynamic Inventory
Create a Python script named dynamic_inventory.py that will interact with the AWS SDK (Boto3) to fetch EC2 instance details.

Step 2: Make the Script Executable
chmod +x filename.py

Step 3: Test Your Dynamic Inventory Script
You can test your dynamic inventory setup by running:

ansible -i /path/to/your/custom_inventory.py all -m debug -a "msg={{ hostvars }}"
