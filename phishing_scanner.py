import re
import requests

# ========== SETTINGS ==========
API_KEY = 'AIzaSyAZ9vn9JmoFjZEuYtki0IBClbmUhO_M3Sc'

# ========== MANUAL PHISHING FEATURES ==========
suspicious_keywords = ['login', 'verify', 'update', 'secure', 'account', 'bank', 'signin', 'password', 'confirm']
suspicious_extensions = ['.ru', '.cn', '.xyz', '.top', '.tk', '.pw']
shorteners = ['bit.ly', 'tinyurl', 'goo.gl', 'cutt.ly', 'ow.ly', 't.co', 'shorte.st', 'adf.ly']

def manual_check(url):
    reasons = []

    # Rule: Link is too long
    if len(url) > 75:
        reasons.append("Link is too long")
    # Rule: Suspicious symbols
    if any(char in url for char in ['@', '=', '%', '&', '+']):
        reasons.append("Suspicious symbol in URL")
    # Rule: Using URL shortener
    if any(service in url for service in shorteners):
        reasons.append("Shortened URL (using a URL shortener)")
    # Rule: IP address in URL
    if re.match(r'https?://\d+\.\d+\.\d+\.\d+', url):
        reasons.append("IP address in URL")
    # Rule: No HTTPS
    if url.startswith('http://'):
        reasons.append("Not using HTTPS")
    # Rule: Suspicious domain extension
    if any(url.endswith(ext) or ext in url for ext in suspicious_extensions):
        reasons.append("Suspicious domain extension")
    # Rule: Suspicious keyword in URL
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        reasons.append("Suspicious keyword in URL")

    if reasons:
        return True, reasons
    return False, ["URL looks safe (manual rules)"]

def google_safe_browsing_check(url):
    api_url = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}'
    payload = {
        "client": {
            "clientId": "phishing-scanner",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": [
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "POTENTIALLY_HARMFUL_APPLICATION"
            ],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }
    try:
        response = requests.post(api_url, json=payload, timeout=10)
        result = response.json()
        if "matches" in result:
            return True, "⚠️ Warning! This URL is dangerous (Google Safe Browsing)."
        else:
            return False, "✅ This URL is safe (Google Safe Browsing)."
    except Exception as e:
        return False, f"Error when connecting to Google Safe Browsing: {e}"

# ========== MAIN LOGIC ==========
def main():
    url = input("Enter the URL to check: ")

    # First: Manual phishing detection
    manual_result, manual_reasons = manual_check(url)
    print("\n*** Manual Check Results ***")
    if manual_result:
        print("⚠️ Warning! Phishing suspected (Manual Rules):")
        for reason in manual_reasons:
            print("-", reason)
    else:
        print("✅", manual_reasons[0])

    # Second: Google Safe Browsing API check
    print("\n*** Google Safe Browsing Check ***")
    google_result, google_reason = google_safe_browsing_check(url)
    print(google_reason)

    # Final report
    print("\n--- Final Report ---")
    if manual_result or google_result:
        print("❌ This URL is NOT safe! Please do NOT open it.")
    else:
        print("✅ This URL appears to be safe according to all checks.")

if __name__ == '__main__':
    main()
