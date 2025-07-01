# 🛡️ Phishing Link Scanner

A Python-based tool for detecting and identifying phishing URLs.  
Developed for the internship program at **Brainwave Matrix Solutions**.

## 🚀 Features

- **Manual Analysis**:  
  Detects phishing links using rule-based checks such as:
  - Suspicious keywords (login, verify, secure, etc.)
  - Use of IP addresses instead of domain names
  - Suspicious domain extensions (.ru, .cn, .xyz, etc.)
  - Use of link shorteners (bit.ly, tinyurl, etc.)
  - Use of suspicious symbols or very long URLs
  - Non-HTTPS links

- **Real-time Safe Browsing Check**:  
  Integrates with **Google Safe Browsing API** to verify if a link is reported as malicious, phishing, or potentially harmful.

## 🛠️ Technologies

- **Python 3**
- [Google Safe Browsing API](https://developers.google.com/safe-browsing/)
- `requests` library

## 📸 Example

**Input:**
