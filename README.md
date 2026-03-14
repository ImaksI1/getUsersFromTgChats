## Setup

1. Get your **api_id** and **api_hash** from:
   https://my.telegram.org/auth

2. Add them to the `.env` file:

```
API_ID=your_api_id
API_HASH=your_api_hash
```

3. Add the chat IDs you want to parse to the `chat_ids.txt` file (one ID per line).

4. Install the required dependencies:

```
pip install -r requirements.txt
```

5. Run the script:

```
python main.py
```
