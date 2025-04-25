import email
import re
import requests
from urllib.parse import urlparse
import whois
from datetime import datetime
import random
import time

# ⚔️ FORTNITE PHISHING EMAIL DETECTION SYSTEM ⚔️
# Drop into Tilted Towers and eliminate those scam emails!

# Global Battle Pass scoring system
BATTLE_PASS_LEVELS = {
    0: "Default Skin",       # Safe email
    1: "Uncommon Threat",    # Slightly suspicious
    2: "Rare Concern",       # Moderately suspicious
    3: "Epic Warning",       # Highly suspicious
    4: "Legendary Danger",   # Extremely suspicious
    5: "Mythic Scam"         # Definitely a scam
}

# Fortnite POI (Points of Interest) for our detector systems
POI_LOCATIONS = [
    "Tilted Towers", "Pleasant Park", "Retail Row", "Lazy Lake",
    "Sweaty Sands", "Slurpy Swamp", "Weeping Woods", "Steamy Stacks"
]

class FortnitePhishingDetector:
    def __init__(self):
        self.shield_potions = 100  # Email security score
        self.eliminations = 0      # Threats detected
        self.storm_circle = 5      # Scanning intensity
        
    def drop_into_email(self, email_file):
        """Land on the email and loot its contents"""
        print(f"\n🚌 BATTLE BUS LAUNCHING... DROP ZONE: {random.choice(POI_LOCATIONS)} 🪂")
        print("3... 2... 1... DROP!")
        
        with open(email_file, 'r') as supply_drop:
            msg = email.message_from_file(supply_drop)
        
        # Loot the email contents like chests
        sender_loot = msg.get('From', '')
        subject_loot = msg.get('Subject', '')
        body_loot = ""

        print(f"📦 Opening supply drop from: {sender_loot}")
        
        # Check if this email has multiple parts (like a Slurp Juice with shields AND health)
        if msg.is_multipart():
            print("🔍 Multiple attachments detected! Checking for traps...")
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == 'text/plain':
                    try:
                        body_loot += part.get_payload(decode=True).decode('utf-8', errors='ignore')
                        print("📜 Text content looted!")
                    except:
                        print("⚠️ Failed to decode payload! Possible Boogie Bomb!")
        else:
            try:
                body_loot = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                print("📜 Text content looted!")
            except:
                print("⚠️ Failed to decode payload! Possible Boogie Bomb!")

        return {
            'sender': sender_loot, 
            'subject': subject_loot, 
            'body': body_loot
        }
    
    def harvest_urls(self, text_material):
        """Harvest materials (URLs) from the text like you're farming wood, brick, and metal"""
        print("🔨 Harvesting URLs from message content...")
        
        # Extract URLs like farming materials
        urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text_material)
        
        if urls:
            print(f"🌲 Harvested {len(urls)} URLs! (+{len(urls)*10} materials)")
        else:
            print("No materials harvested from this area.")
        
        return urls
    
    def check_domain_storm_circle(self, url):
        """Check if domain is in the storm circle (recently created)"""
        try:
            print(f"🔭 Scouting location: {url}")
            domain = urlparse(url).netloc
            
            # Use storm eye tracker (WHOIS) to check domain age
            print(f"🌀 Checking storm circle for {domain}...")
            domain_info = whois.whois(domain)
            creation_date = domain_info.creation_date
            
            if isinstance(creation_date, list):
                creation_date = creation_date[0]
            
            if creation_date:
                domain_age = (datetime.now() - creation_date).days
                
                # Storm circle check - newer domains are in the storm
                in_storm = domain_age < 30
                
                if in_storm:
                    print(f"⚡ ALERT: {domain} is IN THE STORM! Only {domain_age} days old!")
                    return True
                else:
                    print(f"✅ {domain} is in the safe zone. Age: {domain_age} days")
                    return False
            else:
                print(f"⚠️ Cannot determine age of {domain}. Treating as suspicious!")
                return True
                
        except Exception as e:
            print(f"💥 Error checking domain: {str(e)}")
            return True
    
    def check_for_legendary_phishing_words(self, text):
        """Check for legendary (suspicious) words like you're checking for legendary weapons"""
        # These are our legendary phishing items to look for
        phishing_items = {
            'urgent': 'Chug Jug',
            'verify': 'Shield Potion',
            'password': 'Legendary Assault Rifle',
            'account': 'Gold SCAR',
            'suspended': 'Storm Warning',
            'confirm': 'Slurp Juice',
            'login': 'Launch Pad',
            'security': 'Port-a-Fort',
            'update': 'Med Kit',
            'click here': 'Supply Drop',
            'limited time': 'Limited Time Mode',
            'bank': 'Gold Pump Shotgun',
            'alert': 'Campfire',
            'validate': 'Bandages',
            'expire': 'Storm Shrinking'
        }
        
        found_items = []
        
        print("🔍 Searching for suspicious loot...")
        for word, item in phishing_items.items():
            if word.lower() in text.lower():
                found_items.append(item)
                print(f"⚠️ Found {item} in message!")
        
        suspicious_score = len(found_items)
        
        if suspicious_score > 3:
            print(f"🏆 LEGENDARY THREAT DETECTED! Found {suspicious_score} suspicious items!")
        elif suspicious_score > 0:
            print(f"🔹 Found {suspicious_score} suspicious items in the loot.")
        else:
            print("✅ No suspicious items found in this area.")
            
        return {
            'suspicious_score': suspicious_score,
            'found_items': found_items,
            'is_legendary_threat': suspicious_score > 3
        }
    
    def check_sender_for_defaults(self, sender):
        """Check if sender looks like a default skin (suspicious)"""
        print(f"👤 Checking sender: {sender}")
        
        suspicious = False
        reasons = []
        
        # Check for suspicious patterns
        if '@' not in sender:
            suspicious = True
            reasons.append("Missing @ symbol (Default skin alert!)")
        
        if ' ' in sender:
            suspicious = True
            reasons.append("Contains spaces (Noob alert!)")
        
        if re.search(r'[<>{}[\]()]', sender):
            suspicious = True
            reasons.append("Contains suspicious brackets (Tryhard alert!)")
            
        if len(sender) > 50:
            suspicious = True
            reasons.append("Suspiciously long username (Stream sniper alert!)")
        
        if suspicious:
            print(f"⚠️ Sender looks like a default skin: {', '.join(reasons)}")
        else:
            print("✅ Sender seems like a pro player.")
            
        return {
            'is_suspicious': suspicious,
            'reasons': reasons
        }
    
    def calculate_victory_royale(self, email_data):
        """Calculate final threat assessment (Victory Royale if we detect the scam)"""
        print("\n🔥 FINAL CIRCLE ASSESSMENT 🔥")
        
        # Extract links like collecting materials
        links = self.harvest_urls(email_data['body'])
        
        # Check domains like checking if enemies are in the storm
        suspicious_links = []
        for link in links:
            if self.check_domain_storm_circle(link):
                suspicious_links.append(link)
        
        # Check for suspicious words like legendary weapons
        subject_check = self.check_for_legendary_phishing_words(email_data['subject'])
        body_check = self.check_for_legendary_phishing_words(email_data['body'])
        
        # Check sender like checking if someone's a default skin
        sender_check = self.check_sender_for_defaults(email_data['sender'])
        
        # Calculate final threat level (Battle Pass level)
        threat_score = 0
        
        # Add points for suspicious sender (like a default skin)
        if sender_check['is_suspicious']:
            threat_score += 1
            self.eliminations += 1
            
        # Add points for suspicious subject (like finding a legendary weapon)
        if subject_check['suspicious_score'] > 2:
            threat_score += 1
            self.eliminations += 1
            
        # Add points for suspicious body content (like finding multiple legendaries)
        if body_check['suspicious_score'] > 3:
            threat_score += 1.5
            self.eliminations += 1
            
        # Add points for suspicious links (like enemies in the storm)
        if suspicious_links:
            threat_score += len(suspicious_links) * 0.5
            self.eliminations += len(suspicious_links)
        
        # Cap the threat score at 5 (Mythic level)
        final_threat_score = min(5, threat_score)
        
        # Find the appropriate Battle Pass level
        threat_level = BATTLE_PASS_LEVELS[int(final_threat_score)]
        
        result = {
            'threat_score': round(final_threat_score, 1),
            'threat_level': threat_level,
            'suspicious_links': suspicious_links,
            'suspicious_words': subject_check['found_items'] + body_check['found_items'],
            'sender_issues': sender_check['reasons'],
            'eliminations': self.eliminations
        }
        
        return result

# --- MAIN GAME LOOP ---
if __name__ == "__main__":
    print("""
    ░█▀▀░█▀█░█▀▄░▀█▀░█▀█░▀█▀░▀█▀░█▀▀░░░█▀█░█░█░▀█▀░█▀▀░█░█░▀█▀░█▀█░█▀▀
    ░█▀▀░█░█░█▀▄░░█░░█░█░░█░░░█░░█▀▀░░░█▀▀░█▀█░░█░░█▀▀░█▀█░░█░░█░█░█░█
    ░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░░░▀░░░▀░▀░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀
    ░█▀▄░█▀▀░▀█▀░█▀▀░█▀▀░▀█▀░█▀█░█▀▄░░░█▀▄░█▀█░█░█░█▀█░█░░░█▀▀░█
    ░█░█░█▀▀░░█░░█▀▀░█░░░░█░░█░█░█▀▄░░░█▀▄░█░█░░█░░█▀█░█░░░█▀▀░▀
    ░▀▀░░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀░▀▀▀░▀
    """)
    print("🚀 DROPPING INTO THE EMAIL BATTLE ROYALE 🚀")
    
    detector = FortnitePhishingDetector()
    email_file_path = "test_emails/phishing_sample.eml"  # Replace with your email file
    
    # Add some "loading the game" delay
    for i in range(5):
        dots = "." * (i + 1)
        print(f"\rLoading battle bus{dots.ljust(5)}", end="")
        time.sleep(0.3)
    print("\n")
    
    # Run the detection
    email_data = detector.drop_into_email(email_file_path)
    result = detector.calculate_victory_royale(email_data)
    
    # Display final results like end-game stats
    print("\n" + "=" * 60)
    if result['threat_score'] >= 4:
        print("""
        #1 VICTORY ROYALE!
        Phishing email eliminated!
        """)
    else:
        print("""
        THREAT ASSESSMENT COMPLETE
        Stay alert for storm movements!
        """)
    
    print(f"🏆 THREAT LEVEL: {result['threat_level']}")
    print(f"🔢 SCORE: {result['threat_score']}/5")
    print(f"💀 ELIMINATIONS: {result['eliminations']}")
    print("=" * 60)
    
    # Display details like match stats
    if result['suspicious_links']:
        print("\n🔗 ENEMY LOCATIONS DETECTED:")
        for url in result['suspicious_links']:
            print(f" - {url}")
    
    if result['suspicious_words']:
        print("\n⚔️ LEGENDARY THREAT ITEMS FOUND:")
        for item in set(result['suspicious_words']):
            print(f" - {item}")
    
    if result['sender_issues']:
        print("\n👤 SENDER THREAT ASSESSMENT:")
        for issue in result['sender_issues']:
            print(f" - {issue}")
    
    print("\n🎮 GG! Thanks for using the Fortnite Phishing Detector! 🎮")