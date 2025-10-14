# 🤖 Automated Bidding Assistant (Beginner-Friendly)

A simplified Python-based auction simulator that automatically places bids on mock auction items using user-defined strategies. Built entirely with Streamlit — no separate backend or paid APIs.

## Features
- Rule-based auto-bidding (budget, per-item cap, snipe window)
- Streamlit dashboard to view auctions and bid results
- Charts to visualize bid amounts per item
- Mock data via CSV for easy experimentation

## Project Structure
```
automated_bidding_assistant/
├── data/
│   └── auctions.csv
├── app.py
├── bidding_logic.py
├── requirements.txt
└── README.md
```

## Getting Started
1. Create and activate a virtual environment (recommended)
2. Install dependencies
3. Run the app

```bash
# from the project root
pip install -r requirements.txt
streamlit run app.py
```

## Mock Data
Edit `data/auctions.csv` to add or adjust auctions. Columns:
- `item_id`, `item_name`, `current_price`, `min_increment`, `end_time` (YYYY-MM-DD HH:MM:SS)

## Deployment (Streamlit Cloud)
1. Push this project to GitHub
2. On Streamlit Cloud, create a new app and select the repo
3. Set the entry point to `app.py`

## Roadmap
- Persist bids with SQLite
- Countdown timers for live auctions
- Advanced strategies / ML-based bidding
- Notifications for winning status

---
Built with ❤️ using Python + Streamlit.
