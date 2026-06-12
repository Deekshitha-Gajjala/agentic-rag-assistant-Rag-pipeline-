import sqlite3

def create_database():
    """Create a sample legal cases database."""
    conn = sqlite3.connect("legal_cases.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT UNIQUE,
            case_type TEXT,
            year INTEGER,
            fine_amount TEXT,
            outcome TEXT
        )
    """)

    cases = [
        ("Amazon", "privacy", 2023, "$30 million", "Settled"),
        ("Google", "privacy", 2023, "$93 million", "Settled"),
        ("Meta", "privacy", 2023, "$1.3 billion", "Fined"),
        ("Apple", "privacy", 2024, "$500 million", "Fined"),
        ("Microsoft", "antitrust", 2023, "$69 million", "Settled"),
        ("Uber", "data breach", 2022, "$148 million", "Settled"),
        ("Twitter", "privacy", 2022, "$150 million", "Fined"),
        ("TikTok", "privacy", 2023, "$368 million", "Fined"),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO cases 
        (company, case_type, year, fine_amount, outcome) 
        VALUES (?, ?, ?, ?, ?)
    """, cases)

    conn.commit()
    conn.close()

def sql_search(query: str) -> str:
    """Search legal cases database using SQL."""
    create_database()
    conn = sqlite3.connect("legal_cases.db")
    cursor = conn.cursor()

    query_lower = query.lower()

    if "privacy" in query_lower:
        cursor.execute("SELECT * FROM cases WHERE case_type='privacy'")
    elif "antitrust" in query_lower:
        cursor.execute("SELECT * FROM cases WHERE case_type='antitrust'")
    elif "data breach" in query_lower:
        cursor.execute("SELECT * FROM cases WHERE case_type='data breach'")
    elif "2022" in query_lower:
        cursor.execute("SELECT * FROM cases WHERE year=2022")
    elif "2023" in query_lower:
        cursor.execute("SELECT * FROM cases WHERE year=2023")
    elif "2024" in query_lower:
        cursor.execute("SELECT * FROM cases WHERE year=2024")
    else:
        for company in ["Amazon", "Google", "Meta", "Apple", "Microsoft", "Uber", "Twitter", "TikTok"]:
            if company.lower() in query_lower:
                cursor.execute("SELECT * FROM cases WHERE company=?", (company,))
                break
        else:
            cursor.execute("SELECT * FROM cases")

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No matching cases found in database."

    result = []
    for row in rows:
        result.append(f"Company: {row[1]} | Type: {row[2]} | Year: {row[3]} | Fine: {row[4]} | Outcome: {row[5]}")

    return "\n".join(result)

# Test it
if __name__ == "__main__":
    print("Testing SQL Tool...\n")

    print("Query 1: privacy cases")
    print(sql_search("privacy cases"))
    print()

    print("Query 2: Amazon cases")
    print(sql_search("Amazon lawsuit"))
    print()

    print("Query 3: 2023 cases")
    print(sql_search("cases in 2023"))