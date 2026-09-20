# Password Manager & Vault (Tkinter)

A secure, desktop-based Password Manager built with Python using the **Tkinter** GUI library and an **SQLite** database for persistent storage. Features user authentication, password storage per account, password generation, and clipboard integration.

---

## Features

- **User Authentication:**
  - Separate Sign-In (Registration) and Login interfaces.
  - Hashed password verification using `SHA3-384`.
  - User session management allowing multi-user usage.

- **Password Vault Management:**
  - Store key-value pairs (Service/Website and Password) under your active account.
  - Edit or delete existing vault entries.
  - Quick-copy passwords directly to your clipboard.

- **Built-in Password Generator:**
  - Generate customizable passwords based on desired length and complexity:
    - **Simple:** Digits only.
    - **Hard:** Alphanumeric (letters and numbers).
    - **Extreme:** Letters, numbers, and special characters/symbols.
  - Utilizes Python's `secrets` module for cryptographically secure random generation.

- **Dark Green Custom GUI Theme:**
  - Custom UI color palette with toggles to reveal or hide password entry fields.

---

## Tech Stack & Dependencies

- **Language:** Python 3.x
- **GUI Framework:** `tkinter` (Built-in)
- **Database:** `sqlite3` (Built-in)
- **Security / Hashing:** `hashlib`, `secrets` (Built-in)

> **Note:** Since all dependencies rely on standard Python built-in libraries, no extra `pip install` commands are required!

---

## Installation & Setup

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/Viamprogrammer/Password-Manager
   cd Password-Manager
   ```

2. **Run the Application:**
   Run the Python script directly using your Python interpreter:
   ```bash
   python "Login Page.py"
   ```

---


## Usage Guide

1. **Creating an Account:**
   - Launch the application and click on **Sign-In**.
   - Enter a username (minimum 3 characters) and a password (minimum 6 characters).
   - Click **Add Account**.

2. **Logging In:**
   - Enter your registered credentials and click **Login**.

3. **Managing Your Vault:**
   - Click **Add a password** to store credentials for a new service or site.
   - Click **Edit** to alter or delete an existing stored service.
   - Click **Copy** to save the selected item's password directly to your system clipboard.

4. **Generating Passwords:**
   - Within the "Add Password" window, click **Generate**.
   - Select the desired complexity level (**Simple**, **Hard**, or **Extreme**).
   - Input your desired length and click **Generate**, then **Copy** to use it instantly.

---

## Security Consideration Notes

- Passwords stored inside the vault table (`user_data`) are currently saved in plain text within the local SQLite database. For production or sensitive use, consider adding symmetric encryption (e.g., using `cryptography.fernet`) before saving vault entries to disk.