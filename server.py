# Copyright (C) 2026 Lixiod Technologies

import os
import sys
from dotenv import load_dotenv
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

load_dotenv()

def run_ftp_server():
    host = os.getenv("FTP_HOST", "0.0.0.0")
    port = int(os.getenv("FTP_PORT", 2121))
    username = os.getenv("FTP_USER", "admin")
    password = os.getenv("FTP_PASS", "admin")
    ftp_root = os.getenv("FTP_ROOT", "./ftp_data")
    
    pasv_start = os.getenv("FTP_PASV_PORTS_START")
    pasv_end = os.getenv("FTP_PASV_PORTS_END")
    masquerade_addr = os.getenv("FTP_MASQUERADE_ADDRESS")

    abs_ftp_root = os.path.abspath(ftp_root)
    os.makedirs(abs_ftp_root, exist_ok=True)

    # Gestion of Users
    authorizer = DummyAuthorizer()
    authorizer.add_user(
        username=username,
        password=password,
        homedir=abs_ftp_root,
        perm="elradfmw"
    )

    # Configuration FTP handler
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "FTP Server Ready"

    # Configuration passive mode
    if pasv_start and pasv_end:
        handler.passive_ports = range(int(pasv_start), int(pasv_end) + 1)
    
    if masquerade_addr:
        handler.masquerade_address = masquerade_addr

    # Server start config
    address = (host, port)
    server = FTPServer(address, handler)
    
    # Connexion Limit
    server.max_cons = 100
    server.max_cons_per_ip = 10

    print(f"[*] FTP Server started on : {host}:{port}")
    print(f"[*] Root dir : {abs_ftp_root}")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Stopping FTP Server.")
        sys.exit(0)

if __name__ == "__main__":
    run_ftp_server()
