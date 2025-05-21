###Valid Certificate**

import unittest
import ssl
import socket
import threading

class TestSSL(unittest.TestCase):
  def setUp(self):
   self.host = 'localhost'
   self.server_ready = threading.Event()
   self.server_error = None
   self.server_port = None

def start_server(self, certfile, keyfile, client_auth=False):
 def server_task():
     context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
     context.load_cert_chain(certfile=certfile, keyfile=keyfile)
     if client_auth:
         context.verify_mode = ssl.CERT_REQUIRED
     context.load_verify_locations(cafile='ca.crt')

     with socket.socket() as sock:
         sock.bind((self.host, 0))
         self.server_port = sock.getsockname()[1]
         sock.listen(1)
         self.server_ready.set()
         try:
             conn, _ = sock.accept()
             with context.wrap_socket(conn, server_side=True) as ssock:
                 ssock.recv(1024)
                 ssock.send(b"OK")
         except Exception as e:
             self.server_error = e

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    def start_tls12_server(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_2
        context.load_cert_chain('server.crt', 'server.key')
        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    self.server_thread = threading.Thread(target=start_tls12_server)
    self.server_thread.start()
    self.server_ready.wait()

    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    def start_tls12_server(self, certfile, keyfile):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_2
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    self.start_tls12_server('server.crt', 'server.key')
    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=certfile, keyfile=keyfile)
if client_auth:
 context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile='ca.crt')

with socket.socket() as sock:
 sock.bind((self.host, 0))

def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    def start_tls12_server(self, certfile, keyfile):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_2
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    self.start_server('server.crt', 'server.key')
    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()

def start_tls12_server(self, certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    with socket.socket() as sock:
        sock.bind((self.host, 0))
        self.server_port = sock.getsockname()[1]
        sock.listen(1)
        self.server_ready.set()
        try:
            conn, _ = sock.accept()
            with context.wrap_socket(conn, server_side=True) as ssock:
                ssock.recv(1024)
                ssock.send(b"OK")
        except Exception as e:
            self.server_error = e

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    self.start_tls12_server('server.crt', 'server.key')
    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()

def start_tls12_server(self, certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    with socket.socket() as sock:
        sock.bind((self.host, 0))
        self.server_port = sock.getsockname()[1]
        sock.listen(1)
        self.server_ready.set()
        try:
            conn, _ = sock.accept()
            with context.wrap_socket(conn, server_side=True) as ssock:
                ssock.recv(1024)
                ssock.send(b"OK")
        except Exception as e:
            self.server_error = e

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    self.start_tls12_server('server.crt', 'server.key')
    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
            
def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()

def start_tls12_server(self, certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    with socket.socket() as sock:
        sock.bind((self.host, 0))
        self.server_port = sock.getsockname()[1]
        sock.listen(1)
        self.server_ready.set()
        try:
            conn, _ = sock.accept()
            with context.wrap_socket(conn, server_side=True) as ssock:
                ssock.recv(1024)
                ssock.send(b"OK")
        except Exception as e:
            self.server_error = e

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    self.start_tls12_server('server.crt', 'server.key')
    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def test_valid_cert(self):
    self.start_server('server.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_expired_cert(self):
    self.start_server('server_expired.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("certificate has expired", str(cm.exception))

def test_hostname_mismatch(self):
    self.start_server('wrong_host.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

def test_mutual_auth_success(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    context.load_cert_chain('client.crt', 'client.key')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_mutual_auth_failure(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLError):
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def tearDown(self):
    if self.server_thread:
        self.server_thread.join()

def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()

def start_tls12_server(self, certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    with socket.socket() as sock:
        sock.bind((self.host, 0))
        self.server_port = sock.getsockname()[1]
        sock.listen(1)
        self.server_ready.set()
        try:
            conn, _ = sock.accept()
            with context.wrap_socket(conn, server_side=True) as ssock:
                ssock.recv(1024)
                ssock.send(b"OK")
        except Exception as e:
            self.server_error = e

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    self.start_tls12_server('server.crt', 'server.key')
    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def test_valid_cert(self):
    self.start_server('server.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_expired_cert(self):
    self.start_server('server_expired.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("certificate has expired", str(cm.exception))

def test_hostname_mismatch(self):
    self.start_server('wrong_host.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

def test_mutual_auth_success(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    context.load_cert_chain('client.crt', 'client.key')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_mutual_auth_failure(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLError):
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def tearDown(self):
    if self.server_thread:
        self.server_thread.join()

def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()

def start_tls12_server(self, certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    with socket.socket() as sock:
        sock.bind((self.host, 0))
        self.server_port = sock.getsockname()[1]
        sock.listen(1)
        self.server_ready.set()
        try:
            conn, _ = sock.accept()
            with context.wrap_socket(conn, server_side=True) as ssock:
                ssock.recv(1024)
                ssock.send(b"OK")
        except Exception as e:
            self.server_error = e

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    self.start_tls12_server('server.crt', 'server.key')
    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def test_valid_cert(self):
    self.start_server('server.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_expired_cert(self):
    self.start_server('server_expired.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("certificate has expired", str(cm.exception))

def test_hostname_mismatch(self):
    self.start_server('wrong_host.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

def test_mutual_auth_success(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    context.load_cert_chain('client.crt', 'client.key')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_mutual_auth_failure(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLError):
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def tearDown(self):
    if self.server_thread:
        self.server_thread.join()
def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()


def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()

def start_tls12_server(self, certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    with socket.socket() as sock:
        sock.bind((self.host, 0))
        self.server_port = sock.getsockname()[1]
        sock.listen(1)
        self.server_ready.set()
        try:
            conn, _ = sock.accept()
            with context.wrap_socket(conn, server_side=True) as ssock:
                ssock.recv(1024)
                ssock.send(b"OK")
        except Exception as e:
            self.server_error = e

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    self.start_tls12_server('server.crt', 'server.key')
    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def test_valid_cert(self):
    self.start_server('server.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_expired_cert(self):
    self.start_server('server_expired.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("certificate has expired", str(cm.exception))

def test_hostname_mismatch(self):
    self.start_server('wrong_host.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

def test_mutual_auth_success(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    context.load_cert_chain('client.crt', 'client.key')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_mutual_auth_failure(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLError):
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def tearDown(self):
    if self.server_thread:
        self.server_thread.join()

def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()

def start_tls12_server(self, certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    with socket.socket() as sock:
        sock.bind((self.host, 0))
        self.server_port = sock.getsockname()[1]
        sock.listen(1)
        self.server_ready.set()
        try:
            conn, _ = sock.accept()
            with context.wrap_socket(conn, server_side=True) as ssock:
                ssock.recv(1024)
                ssock.send(b"OK")
        except Exception as e:
            self.server_error = e

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    self.start_tls12_server('server.crt', 'server.key')
    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def test_valid_cert(self):
    self.start_server('server.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_expired_cert(self):
    self.start_server('server_expired.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("certificate has expired", str(cm.exception))

def test_hostname_mismatch(self):
    self.start_server('wrong_host.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

def test_mutual_auth_success(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    context.load_cert_chain('client.crt', 'client.key')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_mutual_auth_failure(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLError):
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def tearDown(self):
    if self.server_thread:
        self.server_thread.join()
self.server_port = sock.getsockname()[1]  
def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()

def start_tls12_server(self, certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    with socket.socket() as sock:
        sock.bind((self.host, 0))
        self.server_port = sock.getsockname()[1]
        sock.listen(1)
        self.server_ready.set()
        try:
            conn, _ = sock.accept()
            with context.wrap_socket(conn, server_side=True) as ssock:
                ssock.recv(1024)
                ssock.send(b"OK")
        except Exception as e:
            self.server_error = e

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    self.start_tls12_server('server.crt', 'server.key')
    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def test_valid_cert(self):
    self.start_server('server.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_expired_cert(self):
    self.start_server('server_expired.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("certificate has expired", str(cm.exception))

def test_hostname_mismatch(self):
    self.start_server('wrong_host.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

def test_mutual_auth_success(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    context.load_cert_chain('client.crt', 'client.key')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_mutual_auth_failure(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLError):
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def tearDown(self):
    if self.server_thread:
        self.server_thread.join()
    sock.close()
    self.server_ready.clear()
    self.server_error = None

def test_valid_cert(self):
    self.start_server('server.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)
    sock.close()


#### **2. Expired Certificate**
def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()

def start_tls12_server(self, certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    with socket.socket() as sock:
        sock.bind((self.host, 0))
        self.server_port = sock.getsockname()[1]
        sock.listen(1)
        self.server_ready.set()
        try:
            conn, _ = sock.accept()
            with context.wrap_socket(conn, server_side=True) as ssock:
                ssock.recv(1024)
                ssock.send(b"OK")
        except Exception as e:
            self.server_error = e

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    self.start_tls12_server('server.crt', 'server.key')
    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def test_valid_cert(self):
    self.start_server('server.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_expired_cert(self):
    self.start_server('server_expired.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("certificate has expired", str(cm.exception))

def test_hostname_mismatch(self):
    self.start_server('wrong_host.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

def test_mutual_auth_success(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    context.load_cert_chain('client.crt', 'client.key')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_mutual_auth_failure(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLError):
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def tearDown(self):
    if self.server_thread:
        self.server_thread.join()
def start_server(self, certfile, keyfile, client_auth=False):
    def server_task():
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        if client_auth:
            context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(cafile='ca.crt')

        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    self.server_thread = threading.Thread(target=server_task)
    self.server_thread.start()
    self.server_ready.wait()

def start_tls12_server(self, certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    with socket.socket() as sock:
        sock.bind((self.host, 0))
        self.server_port = sock.getsockname()[1]
        sock.listen(1)
        self.server_ready.set()
        try:
            conn, _ = sock.accept()
            with context.wrap_socket(conn, server_side=True) as ssock:
                ssock.recv(1024)
                ssock.send(b"OK")
        except Exception as e:
            self.server_error = e

def test_tls_version_mismatch(self):
    # Start server with TLS 1.2 only
    self.start_tls12_server('server.crt', 'server.key')
    # Client allows only TLS 1.3
    client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    client_context.minimum_version = ssl.TLSVersion.TLSv1_3
    client_context.maximum_version = ssl.TLSVersion.TLSv1_3
    client_context.load_verify_locations('ca.crt')

    with self.assertRaises(ssl.SSLError):
        # Client connection attempt fails
        with socket.create_connection((self.host, self.server_port)) as sock:
            with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def test_valid_cert(self):
    self.start_server('server.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_expired_cert(self):
    self.start_server('server_expired.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("certificate has expired", str(cm.exception))

def test_hostname_mismatch(self):
    self.start_server('wrong_host.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

def test_mutual_auth_success(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    context.load_cert_chain('client.crt', 'client.key')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_mutual_auth_failure(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLError):
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

def tearDown(self):
    if self.server_thread:
        self.server_thread.join()


class TestSSL(unittest.TestCase):
    def setUp(self):
        self.host = 'localhost'
        self.server_ready = threading.Event()
        self.server_error = None
        self.server_port = None
        self.server_thread = None

    def start_server(self, certfile, keyfile, client_auth=False):
        def server_task():
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain(certfile=certfile, keyfile=keyfile)
            if client_auth:
                context.verify_mode = ssl.CERT_REQUIRED
            context.load_verify_locations(cafile='ca.crt')

            with socket.socket() as sock:
                sock.bind((self.host, 0))
                self.server_port = sock.getsockname()[1]
                sock.listen(1)
                self.server_ready.set()
                try:
                    conn, _ = sock.accept()
                    with context.wrap_socket(conn, server_side=True) as ssock:
                        ssock.recv(1024)
                        ssock.send(b"OK")
                except Exception as e:
                    self.server_error = e

        self.server_thread = threading.Thread(target=server_task)
        self.server_thread.start()
        self.server_ready.wait()

    def start_tls12_server(self, certfile, keyfile):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_2
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    def test_tls_version_mismatch(self):
        # Start server with TLS 1.2 only
        self.start_tls12_server('server.crt', 'server.key')
        # Client allows only TLS 1.3
        client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        client_context.minimum_version = ssl.TLSVersion.TLSv1_3
        client_context.maximum_version = ssl.TLSVersion.TLSv1_3
        client_context.load_verify_locations('ca.crt')

        with self.assertRaises(ssl.SSLError):
            # Client connection attempt fails
            with socket.create_connection((self.host, self.server_port)) as sock:
                with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass

    def test_valid_cert(self):
        self.start_server('server.crt', 'server.key')
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                ssock.send(b"Hello")
                self.assertEqual(ssock.recv(1024), b"OK")
                self.assertIsNone(self.server_error)

    def test_expired_cert(self):
        self.start_server('server_expired.crt', 'server.key')
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with self.assertRaises(ssl.SSLCertVerificationError) as cm:
            with socket.create_connection((self.host, self.server_port)) as sock:
                with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass
        self.assertIn("certificate has expired", str(cm.exception))

    def test_hostname_mismatch(self):
        self.start_server('wrong_host.crt', 'server.key')
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with self.assertRaises(ssl.SSLCertVerificationError) as cm:
            with socket.create_connection((self.host, self.server_port)) as sock:
                with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass
        self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

    def test_mutual_auth_success(self):
        self.start_server('server.crt', 'server.key', client_auth=True)
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        context.load_cert_chain('client.crt', 'client.key')
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                ssock.send(b"Hello")
                self.assertEqual(ssock.recv(1024), b"OK")
                self.assertIsNone(self.server_error)

    def test_mutual_auth_failure(self):
        self.start_server('server.crt', 'server.key', client_auth=True)
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with self.assertRaises(ssl.SSLError):
            with socket.create_connection((self.host, self.server_port)) as sock:
                with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass

    def tearDown(self):
        if self.server_thread:
            self.server_thread.join()
            
class TestSSL(unittest.TestCase):
    def setUp(self):
        self.host = 'localhost'
        self.server_ready = threading.Event()
        self.server_error = None
        self.server_port = None
        self.server_thread = None

    def start_server(self, certfile, keyfile, client_auth=False):
        def server_task():
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain(certfile=certfile, keyfile=keyfile)
            if client_auth:
                context.verify_mode = ssl.CERT_REQUIRED
            context.load_verify_locations(cafile='ca.crt')

            with socket.socket() as sock:
                sock.bind((self.host, 0))
                self.server_port = sock.getsockname()[1]
                sock.listen(1)
                self.server_ready.set()
                try:
                    conn, _ = sock.accept()
                    with context.wrap_socket(conn, server_side=True) as ssock:
                        ssock.recv(1024)
                        ssock.send(b"OK")
                except Exception as e:
                    self.server_error = e

        self.server_thread = threading.Thread(target=server_task)
        self.server_thread.start()
        self.server_ready.wait()

    def start_tls12_server(self, certfile, keyfile):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_2
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    def test_tls_version_mismatch(self):
        # Start server with TLS 1.2 only
        self.start_tls12_server('server.crt', 'server.key')
        # Client allows only TLS 1.3
        client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        client_context.minimum_version = ssl.TLSVersion.TLSv1_3
        client_context.maximum_version = ssl.TLSVersion.TLSv1_3
        client_context.load_verify_locations('ca.crt')

        with self.assertRaises(ssl.SSLError):
            # Client connection attempt fails
            with socket.create_connection((self.host, self.server_port)) as sock:
                with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass

    def test_valid_cert(self):
        self.start_server('server.crt', 'server.key')
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                ssock.send(b"Hello")
                self.assertEqual(ssock.recv(1024), b"OK")
                self.assertIsNone(self.server_error)

    def test_expired_cert(self):
        self.start_server('server_expired.crt', 'server.key')
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with self.assertRaises(ssl.SSLCertVerificationError) as cm:
            with socket.create_connection((self.host, self.server_port)) as sock:
                with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass
        self.assertIn("certificate has expired", str(cm.exception))

    def test_hostname_mismatch(self):
        self.start_server('wrong_host.crt', 'server.key')
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with self.assertRaises(ssl.SSLCertVerificationError) as cm:
            with socket.create_connection((self.host, self.server_port)) as sock:
                with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass
        self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

    def test_mutual_auth_success(self):
        self.start_server('server.crt', 'server.key', client_auth=True)
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        context.load_cert_chain('client.crt', 'client.key')
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                ssock.send(b"Hello")
                self.assertEqual(ssock.recv(1024), b"OK")
                self.assertIsNone(self.server_error)

    def test_mutual_auth_failure(self):
        self.start_server('server.crt', 'server.key', client_auth=True)
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with self.assertRaises(ssl.SSLError):
            with socket.create_connection((self.host, self.server_port)) as sock:
                with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass

    def tearDown(self):
        if self.server_thread:
            self.server_thread.join()
            
class TestSSL(unittest.TestCase):
    def setUp(self):
        self.host = 'localhost'
        self.server_ready = threading.Event()
        self.server_error = None
        self.server_port = None
        self.server_thread = None

    def start_server(self, certfile, keyfile, client_auth=False):
        def server_task():
            context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            context.load_cert_chain(certfile=certfile, keyfile=keyfile)
            if client_auth:
                context.verify_mode = ssl.CERT_REQUIRED
            context.load_verify_locations(cafile='ca.crt')

            with socket.socket() as sock:
                sock.bind((self.host, 0))
                self.server_port = sock.getsockname()[1]
                sock.listen(1)
                self.server_ready.set()
                try:
                    conn, _ = sock.accept()
                    with context.wrap_socket(conn, server_side=True) as ssock:
                        ssock.recv(1024)
                        ssock.send(b"OK")
                except Exception as e:
                    self.server_error = e

        self.server_thread = threading.Thread(target=server_task)
        self.server_thread.start()
        self.server_ready.wait()

    def start_tls12_server(self, certfile, keyfile):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_2
        context.load_cert_chain(certfile=certfile, keyfile=keyfile)
        with socket.socket() as sock:
            sock.bind((self.host, 0))
            self.server_port = sock.getsockname()[1]
            sock.listen(1)
            self.server_ready.set()
            try:
                conn, _ = sock.accept()
                with context.wrap_socket(conn, server_side=True) as ssock:
                    ssock.recv(1024)
                    ssock.send(b"OK")
            except Exception as e:
                self.server_error = e

    def test_tls_version_mismatch(self):
        # Start server with TLS 1.2 only
        self.start_tls12_server('server.crt', 'server.key')
        # Client allows only TLS 1.3
        client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        client_context.minimum_version = ssl.TLSVersion.TLSv1_3
        client_context.maximum_version = ssl.TLSVersion.TLSv1_3
        client_context.load_verify_locations('ca.crt')

        with self.assertRaises(ssl.SSLError):
            # Client connection attempt fails
            with socket.create_connection((self.host, self.server_port)) as sock:
                with client_context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass

    def test_valid_cert(self):
        self.start_server('server.crt', 'server.key')
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                ssock.send(b"Hello")
                self.assertEqual(ssock.recv(1024), b"OK")
                self.assertIsNone(self.server_error)

    def test_expired_cert(self):
        self.start_server('server_expired.crt', 'server.key')
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with self.assertRaises(ssl.SSLCertVerificationError) as cm:
            with socket.create_connection((self.host, self.server_port)) as sock:
                with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass
        self.assertIn("certificate has expired", str(cm.exception))

    def test_hostname_mismatch(self):
        self.start_server('wrong_host.crt', 'server.key')
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with self.assertRaises(ssl.SSLCertVerificationError) as cm:
            with socket.create_connection((self.host, self.server_port)) as sock:
                with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass
        self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

    def test_mutual_auth_success(self):
        self.start_server('server.crt', 'server.key', client_auth=True)
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        context.load_cert_chain('client.crt', 'client.key')
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                ssock.send(b"Hello")
                self.assertEqual(ssock.recv(1024), b"OK")
                self.assertIsNone(self.server_error)

    def test_mutual_auth_failure(self):
        self.start_server('server.crt', 'server.key', client_auth=True)
        context = ssl.create_default_context()
        context.load_verify_locations('ca.crt')
        with self.assertRaises(ssl.SSLError):
            with socket.create_connection((self.host, self.server_port)) as sock:
                with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                    pass

    def tearDown(self):
        if self.server_thread:
            self.server_thread.join()

def test_expired_cert(self):
    self.start_server('server_expired.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("certificate has expired", str(cm.exception))

def test_hostname_mismatch(self):
    self.start_server('wrong_host.crt', 'server.key')
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLCertVerificationError) as cm:
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass
    self.assertIn("hostname 'localhost' doesn't match", str(cm.exception))

def test_mutual_auth_success(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    context.load_cert_chain('client.crt', 'client.key')
    with socket.create_connection((self.host, self.server_port)) as sock:
        with context.wrap_socket(sock, server_hostname='localhost') as ssock:
            ssock.send(b"Hello")
            self.assertEqual(ssock.recv(1024), b"OK")
            self.assertIsNone(self.server_error)

def test_mutual_auth_failure(self):
    self.start_server('server.crt', 'server.key', client_auth=True)
    context = ssl.create_default_context()
    context.load_verify_locations('ca.crt')
    with self.assertRaises(ssl.SSLError):
        with socket.create_connection((self.host, self.server_port)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as ssock:
                pass

pass


#### **5. TLS Version Mismatch
def start_tls12_server(self, certfile, keyfile):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    with socket.socket() as sock:
        sock.bind((self.host, 0))
        self.server_port = sock.getsockname()[1]
        sock.listen(1)
        self.server_ready.set()
        try:
            conn, _ = sock.accept()
            with context.wrap_socket(conn, server_side=True) as ssock:
                ssock.recv(1024)
                ssock.send(b"OK")
        except Exception as e:
            self.server_error = e