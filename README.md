# TwitterFollowers

A Python-based utility to **extract all @usernames of your Twitter (X) followers or followings** using authenticated GraphQL requests and browser session cookies.

This project leverages your **logged-in browser session** to access Twitter’s internal APIs and export follower/following data in a structured format.

---

## Overview
Twitter (X) does not provide an easy way to export your full follower or following list.  
This repository automates that process by:
- Reusing browser cookies
- Making authenticated GraphQL requests
- Parsing the returned JSON data
- Extracting all `@usernames` into a text file

---

## How It Works
1. Export authenticated Twitter cookies from Firefox
2. Configure request parameters (User ID, GraphQL operation ID, Bearer token)
3. Fetch raw following/follower data via Twitter’s internal API
4. Extract all usernames into a readable list

---

## Requirements
- Python 3
- Firefox browser
- Cookie-Editor Firefox extension
- Active logged-in account on **:contentReference[oaicite:0]{index=0}**

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/TwitterFollowers.git
cd TwitterFollowers
````

---

### 2. Export Twitter Cookies

1. Open Firefox
2. Install **Cookie-Editor** add-on
3. Visit:

   ```
   https://x.com/<your-username-without-@>/following
   ```
4. Click Cookie-Editor → **Export**
5. Select **Netscape** format
6. Copy the exported cookies

---

### 3. Save Cookies

Create a file named:

```text
twitter_cookies.txt
```

Paste the copied **Netscape cookie data** into it and save.

---

## Configuration (`create_json.py`)

The script requires **three values** from your Twitter session.

### A. Twitter User ID

* Visit: [https://twiteridfinder.com/](https://twiteridfinder.com/)
* Enter your username (without `@`)
* Copy your numeric **User ID**
* Replace:

```python
enter-user-id
```

---

### B. GraphQL Operation ID

1. Visit:

   ```
   https://x.com/<your-username-without-@>/following
   ```
2. Press **F12** → Developer Tools
3. Refresh the page
4. Open **Network** tab
5. Filter/search:

   ```
   /i/api/graphql/
   ```
6. Click the request named:

   ```
   Following?variables=...
   ```
7. In **Headers**, locate:

   ```
   /i/api/graphql/<SOME-STRING>/Following
   ```
8. Copy `<SOME-STRING>` and replace:

```python
enter-GraphQL-operation-ID
```

---

### C. Bearer Token

1. From the **same GraphQL request**
2. Scroll to **Request Headers**
3. Find:

   ```
   Authorization: Bearer AAAAAAAAAAAAA....
   ```
4. Copy the entire token
5. Replace:

```python
enter-bearer-token
```

---

## Usage

### Step 1: Fetch Raw Following Data

```bash
python3 create_json.py
```

This generates:

```text
all_followings_raw.json
```

---

### Step 2: Extract Usernames

```bash
python3 extract_usernames.py
```

This generates:

```text
followings.txt
```

Each line contains one `@username`.

---

## Followers List

The same method can be adapted to fetch:

* **Followers list**
* By changing the GraphQL endpoint and query parameters accordingly

---

## Files

```text
create_json.py            # Fetches raw GraphQL JSON data
extract_usernames.py      # Extracts @usernames from JSON
twitter_cookies.txt       # Netscape-format browser cookies
all_followings_raw.json   # Raw API response
followings.txt            # Final extracted usernames
```

---

## Important Notes

* This project relies on **private Twitter APIs**, which may change
* Tokens and cookies can expire at any time
* Rate limits may apply
* Do not share your bearer token or cookies publicly

---

## Disclaimer

This project is for **educational and personal use only**.
The author is not responsible for account suspension, data misuse, or violations of Twitter’s terms of service.

---

## Author

**Pranjal**

```

---

### If you want next:
- Combine both projects under a **Security & Automation portfolio**
- Add `.gitignore` (cookies & tokens protection)
- Improve robustness with pagination support
- Make it resume / recruiter optimized

Just say the word.
```
