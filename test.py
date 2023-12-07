def generate_uuid_password():
    return str(uuid.uuid4())

mock_data = [
    {'username': 'john_doe', 'password': 'c249f5a0-5cb5-4c0f-8a64-68b1a7e6ac2az', 'email': 'john.doe@example.com', 'public_key': 'ssh-rsa AAAAB3NzaC1yc2EAAA...'},
    {'username': 'jane_smith', 'password': '8a82c93b-3b3c-4a2a-b14d-3a8234128a74', 'email': 'jane.smith@example.com', 'public_key': 'ssh-rsa AAAAB3NzaC1yc2EAAA...'},
    {'username': 'bob_jenkins', 'password': 'ec8eb9b2-39cb-4a69-9f2f-1f5813f1d86d', 'email': 'bob.jenkins@example.com', 'public_key': 'ssh-rsa AAAAB3NzaC1yc2EAAA...'},
    # Add more users as needed
]

# Display the generated data
for user in mock_data:
    print(f"Username: {user['username']}, Password: {user['password']}, Email: {user['email']}, Public Key: {user['public_key']}")
