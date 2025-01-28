# Library Management System

## Overview
A comprehensive library management system built with Flask, designed to efficiently manage books, members, and library operations.

## Features
- Book management (add, update, delete, search)
- Member management
- Author Management
- User authentication and authorization

## Tech Stack
- Flask (Python web framework)
- SQLAlchemy (ORM)
- Alembic 
- Marshmallow
- Jwt
- progressSQL

## Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/libraryManagement.git
cd libraryManagement
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Unix
venv\Scripts\activate     # For Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
flask run
```

## Project Structure
```
libraryManagement/
│   config.py
│   marsh.py
│   model.py
│   __init__.py
│
├───auth
│       routes.py
│
├───author
│       routes.py
│
├───books
│       routes.py
│
└───Member
        routes.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)