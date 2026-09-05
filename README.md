# Simple FTP Server

A lightweight, fully configurable asynchronous FTP server built with Python.

---

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`:
  - `pyftpdlib`
  - `python-dotenv`

---

## Project Structure

```text
.
├── .env                  # Environment configuration file
├── .env.example          # Template for environment variables
├── requirements.txt      # Python dependencies
├── server.py             # Main FTP server script
└── ftp_data/             # Default root storage directory (auto-created)
```

---

## Installation

1. **Clone or download the repository:**

   ```bash
   git clone https://github.com/Miaoumap24/Simple-FTP-Server.git
   cd Simple-FTP-Server
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

Copy `.env.example` to `.env` and adjust settings as needed:

```bash
cp .env.example .env
```

### `.env` File Options

```ini
# Network Binding
FTP_HOST=0.0.0.0
FTP_PORT=2121

# User Credentials
FTP_USER=admin
FTP_PASS=secret123

# Root Storage Directory
FTP_ROOT=./ftp_data

# Passive Mode Port Range (Optional)
FTP_PASV_PORTS_START=60000
FTP_PASV_PORTS_END=60050

# Public IP for NAT Traversal (Optional)
# FTP_MASQUERADE_ADDRESS=192.168.1.50
```

### Environment Variables Breakdown

| Variable | Default | Description |
| :--- | :--- | :--- |
| `FTP_HOST` | `0.0.0.0` | IP address to bind the server. Use `0.0.0.0` for all interfaces. |
| `FTP_PORT` | `2121` | Listening port for incoming FTP connections. |
| `FTP_USER` | `admin` | Username for authentication. |
| `FTP_PASS` | `admin` | Password for authentication. |
| `FTP_ROOT` | `./ftp_data` | Root directory path accessible to connected clients. |
| `FTP_PASV_PORTS_START` | *None* | Starting port for passive mode transfers. |
| `FTP_PASV_PORTS_END` | *None* | Ending port for passive mode transfers. |
| `FTP_MASQUERADE_ADDRESS` | *None* | External IP address returned to clients in passive mode. |

---

## Usage

Start the FTP server:

```bash
python server.py
```

### Example Console Output

```text
[*] FTP Server started to 0.0.0.0:2121
[*] Root DIR : /path/to/project/ftp_data
```

---

## Client Connection Examples

### Command Line (`ftp`)

```bash
ftp -P 2121 admin@localhost
```

### FileZilla / Cyberduck

- **Host**: `localhost` (or server IP)
- **Port**: `2121`
- **Logon Type**: Normal
- **User**: `admin`
- **Password**: `secret123`

---

## User Permissions Reference

The server assigns full read/write permissions (`elradfmw`) to the user configured in `.env`:

- `e`: Change directory (`cwd`)
- `l`: List files (`list`)
- `r`: Retrieve file from server (`get`)
- `a`: Append data to an existing file (`appe`)
- `d`: Delete file or directory (`dele`, `rmd`)
- `f`: Rename file (`rnfr`, `rnto`)
- `m`: Create directory (`mkd`)
- `w`: Store file to server (`put`)

---

## License

AGPL-3.0 License
