def generate_uuid_password():
    return str(uuid.uuid4())

mock_data = [
    {'username': 'john_doe', 'password': generate_uuid_password(), 'email': 'john.doe@example.com', 'public_key': 'ssh-rsa AAAAB3NzaC1yc2EAAA...'},
    {'username': 'jane_smith', 'password': generate_uuid_password(), 'email': 'jane.smith@example.com', 'public_key': 'ssh-rsa AAAAB3NzaC1yc2EAAA...'},
    {'username': 'bob_jenkins', 'password': generate_uuid_password(), 'email': 'bob.jenkins@example.com', 'public_key': 'ssh-rsa AAAAB3NzaC1yc2EAAA...'},
    # Add more users as needed
]

# Display the generated data
for user in mock_data:
    print(f"Username: {user['username']}, Password: {user['password']}, Email: {user['email']}, Public Key: {user['public_key']}")
