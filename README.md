# 🏆 Fortnite Battle Royale Phishing Detector 🏆

A Fortnite-themed email security tool that helps you detect and eliminate phishing emails using battle royale terminology!

![Fortnite Phishing Detector](https://i.redd.it/rmwd240cwo2a1.jpg)

## 🚌 Drop Into Security

This tool analyzes emails for phishing attempts using the following Fortnite-themed detection mechanisms:

- **Battle Bus Email Landing**: Parse and extract email contents
- **Storm Circle Domain Check**: Identify suspiciously new domains
- **Legendary Item Detection**: Find suspicious keywords and phrases
- **Default Skin Sender Analysis**: Detect suspicious sender addresses
- **Victory Royale Assessment**: Calculate overall threat level

## 🎮 How To Play

### Installation

1. Clone the repository:
```bash
git clone https://github.com/helenscun/fortnite-phishing-detector.git
cd fortnite-phishing-detector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the detector on an email file:

```bash
python fortnite_phishing_detector.py
```

By default, it will scan the sample email in `test_emails/phishing_sample.eml`. To scan your own email:

1. Save the suspicious email as an .eml file
2. Edit the `email_file_path` variable in the script to point to your file
3. Run the detector and get your Victory Royale!

## 📊 Threat Levels

The detector categorizes emails using Fortnite's item rarity system:

| Threat Level | Description | Action |
|--------------|-------------|--------|
| Default Skin | Safe email | No action required |
| Uncommon Threat | Slightly suspicious | Proceed with caution |
| Rare Concern | Moderately suspicious | Verify sender before taking action |
| Epic Warning | Highly suspicious | Do not click any links |
| Legendary Danger | Extremely suspicious | Do not reply or interact |
| Mythic Scam | Definitely a scam | Delete immediately! |

## 🛡️ Features

- **URL Harvesting**: Extracts and analyzes all URLs in the email body
- **Domain Age Check**: Identifies recently created domains (in the storm)
- **Keyword Analysis**: Detects suspicious words like "urgent", "verify", etc.
- **Sender Analysis**: Checks for suspicious sender email formatting
- **Visual Output**: Provides Fortnite-themed console output with ASCII art

## 📝 Sample Output

```
░█▀▀░█▀█░█▀▄░▀█▀░█▀█░▀█▀░▀█▀░█▀▀░░░█▀█░█░█░▀█▀░█▀▀░█░█░▀█▀░█▀█░█▀▀
░█▀▀░█░█░█▀▄░░█░░█░█░░█░░░█░░█▀▀░░░█▀▀░█▀█░░█░░█▀▀░█▀█░░█░░█░█░█░█
░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░░░▀░░░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀
░█▀▄░█▀▀░▀█▀░█▀▀░█▀▀░▀█▀░█▀█░█▀▄░░░█▀▄░█▀█░█░█░█▀█░█░░░█▀▀░█
░█░█░█▀▀░░█░░█▀▀░█░░░░█░░█░█░█▀▄░░░█▀▄░█░█░░█░░█▀█░█░░░█▀▀░▀
░▀▀░░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░▀

#1 VICTORY ROYALE!
Phishing email eliminated!

🏆 THREAT LEVEL: Legendary Danger
🔢 SCORE: 4.5/5
💀 ELIMINATIONS: 7
============================================================

🔗 ENEMY LOCATIONS DETECTED:
 - http://bit.ly/suspiciouslink123
 - http://verify-account-now.com

⚔️ LEGENDARY THREAT ITEMS FOUND:
 - Gold SCAR
 - Shield Potion
 - Chug Jug
 - Supply Drop
 - Storm Warning

👤 SENDER THREAT ASSESSMENT:
 - Contains suspicious brackets (Tryhard alert!)
 - Suspiciously long username (Stream sniper alert!)

🎮 GG! Thanks for using the Fortnite Phishing Detector! 🎮
```

## 🧰 Dependencies

See `requirements.txt` for the full list of dependencies.

## 🔫 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 Disclaimer

This tool is meant for educational purposes and fun. While it can help identify suspicious emails, it should not replace comprehensive cybersecurity practices or professional security software. Always be cautious with emails from unknown senders!

*Note: This project is not affiliated with, endorsed by, or related to Epic Games or Fortnite.*
