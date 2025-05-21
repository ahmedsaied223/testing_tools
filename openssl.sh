# Generate CA
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 365 -key ca.key -out ca.crt -subj "/CN=Test CA"

# Server Certificate (valid)
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr -subj "/CN=localhost"
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365

# Expired Server Certificate
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server_expired.crt -days -1

# Wrong Hostname Certificate
openssl req -new -key server.key -out wrong_host.csr -subj "/CN=example.com"
openssl x509 -req -in wrong_host.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out wrong_host.crt -days 365

# Client Certificate
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr -subj "/CN=Test Client"
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 365



/Users/aahmed829@cable.comcast.com/google_search.py/cucumber-testing-framework