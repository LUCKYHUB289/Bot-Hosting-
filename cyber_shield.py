import os
import re
import asyncio
import random
import string
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ================= CONFIG =================
API_ID = 38186654
API_HASH = "8470283982:AAG7ekCTaaWg4MmX85i4wh8zvDq-8oR9nRA"
BOT_TOKEN = "8694963124:AAGxvgI-WQDPy-0U1bQInnpfB4q1OA928w0"

bot = Client("CyberShieldBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ================= DATA =================
user_stats = {}
quiz_scores = {}

# ================= START =================
@bot.on_message(filters.command("start"))
async def start(_, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛡️ TOOLS", callback_data="tools"), InlineKeyboardButton("📚 LEARN", callback_data="learn")],
        [InlineKeyboardButton("🏆 STATS", callback_data="stats"), InlineKeyboardButton("📢 ABOUT", callback_data="about")]
    ])
    
    # Welcome message with RAHUL WORLD
    welcome_text = f"""
╔══════════════════════════════════════╗
║     🌟 WELCOME TO RAHUL WORLD 🌟      ║
╚══════════════════════════════════════╝

🛡️ **CYBER SHIELD BOT** 🔐

👋 Hello **{message.from_user.first_name}**!

🎓 **School Project:** Ethical Hacking & Security

🔧 **Features:**
✅ Password Strength Checker
✅ Secure Password Generator  
✅ IP/Domain Lookup
✅ Cybersecurity Quiz
✅ Security Tips

⚠️ **100% Educational Purpose**

👨‍💻 **Developer:** @RAHUL_MODS_OWNER
💫 **Powered by:** RAHUL WORLD

╔══════════════════════════════════════╗
║    🔥 STAY SAFE, STAY SECURE 🔥       ║
╚══════════════════════════════════════╝
"""
    
    await message.reply_text(
        welcome_text,
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

# ================= CALLBACKS =================
@bot.on_callback_query()
async def callback(_, query):
    data = query.data
    
    if data == "tools":
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔐 CHECK PASSWORD", callback_data="check")],
            [InlineKeyboardButton("🔑 GENERATE PASSWORD", callback_data="gen")],
            [InlineKeyboardButton("🌐 IP LOOKUP", callback_data="ip")],
            [InlineKeyboardButton("🔙 BACK", callback_data="back")]
        ])
        await query.message.edit_text("🔧 **Security Tools - RAHUL WORLD**", reply_markup=kb)
        await query.answer()
    
    elif data == "learn":
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("📚 TIPS", callback_data="tips")],
            [InlineKeyboardButton("🎯 QUIZ", callback_data="quiz")],
            [InlineKeyboardButton("🔙 BACK", callback_data="back")]
        ])
        await query.message.edit_text("📖 **Learning Center - RAHUL WORLD**", reply_markup=kb)
        await query.answer()
    
    elif data == "back":
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("🛡️ TOOLS", callback_data="tools"), InlineKeyboardButton("📚 LEARN", callback_data="learn")],
            [InlineKeyboardButton("🏆 STATS", callback_data="stats"), InlineKeyboardButton("📢 ABOUT", callback_data="about")]
        ])
        back_text = """
╔══════════════════════════════════════╗
║     🌟 WELCOME TO RAHUL WORLD 🌟      ║
╚══════════════════════════════════════╝

🛡️ **Cyber Shield Bot**

Welcome back to **RAHUL WORLD**!

👨‍💻 @RAHUL_MODS_OWNER
"""
        await query.message.edit_text(back_text, reply_markup=kb)
        await query.answer()
    
    elif data == "check":
        await query.message.reply_text("🔐 **Send me any password to check its strength...**\n\n💫 RAHUL WORLD Security")
        await query.answer()
    
    elif data == "gen":
        kb = InlineKeyboardMarkup([
            [InlineKeyboardButton("8", callback_data="g8"), InlineKeyboardButton("12", callback_data="g12")],
            [InlineKeyboardButton("16", callback_data="g16"), InlineKeyboardButton("20", callback_data="g20")],
            [InlineKeyboardButton("🔙 BACK", callback_data="tools")]
        ])
        await query.message.edit_text("🔑 **Select password length - RAHUL WORLD**", reply_markup=kb)
        await query.answer()
    
    elif data == "ip":
        await query.message.reply_text("🌐 **Send IP or domain:**\nEx: 8.8.8.8 or google.com\n\n💫 Powered by RAHUL WORLD")
        await query.answer()
    
    elif data == "stats":
        uid = query.from_user.id
        stats = user_stats.get(uid, {"quizzes": 0, "passwords": 0})
        stats_text = f"""
╔══════════════════════════════════════╗
║        🏆 YOUR STATISTICS 🏆          ║
╚══════════════════════════════════════╝

👤 **User:** {query.from_user.first_name}
📝 **Quizzes Taken:** {stats.get('quizzes', 0)}
🔐 **Passwords Checked:** {stats.get('passwords', 0)}
⭐ **Quiz Score:** {quiz_scores.get(uid, 0)}/3

💫 **RAHUL WORLD - Cyber Shield**
"""
        await query.message.reply_text(stats_text)
        await query.answer()
    
    elif data == "about":
        about_text = """
╔══════════════════════════════════════╗
║         📢 ABOUT PROJECT 📢           ║
╚══════════════════════════════════════╝

🎓 **School Project:** Cyber Shield Bot
👨‍💻 **Developer:** RAHULXSUMAN
💫 **World:** RAHUL WORLD
📅 **Year:** 2024

**Purpose:**
Educational Cybersecurity Tool

**Features:**
• Password Security
• Password Generator  
• IP Lookup
• Cyber Quiz
• Security Tips

⚠️ **100% Educational Only**

👑 **Contact:** @RAHUL_MODS_OWNER

╔══════════════════════════════════════╗
║    🔥 POWERED BY RAHUL WORLD 🔥       ║
╚══════════════════════════════════════╝
"""
        await query.message.reply_text(about_text)
        await query.answer()
    
    elif data == "tips":
        tips_list = [
            "🔐 Use 12+ character passwords",
            "📱 Enable 2FA on all accounts",
            "⚠️ Don't reuse passwords",
            "🔍 Check URLs before clicking",
            "🔄 Update software regularly",
            "🔒 Use VPN on public WiFi",
            "💾 Backup important data"
        ]
        tip_text = f"""
╔══════════════════════════════════════╗
║        🛡️ SECURITY TIP 🛡️            ║
╚══════════════════════════════════════╝

{random.choice(tips_list)}

💫 **RAHUL WORLD - Stay Secure**
"""
        await query.message.reply_text(tip_text)
        await query.answer()
    
    elif data == "quiz":
        quiz_scores[query.from_user.id] = 0
        quiz_scores[f"{query.from_user.id}_q"] = 0
        await send_question(query)
        await query.answer()
    
    elif data.startswith("g"):
        length = int(data[1:])
        chars = string.ascii_letters + string.digits + "!@#$%"
        pwd = ''.join(random.choice(chars) for _ in range(length))
        pwd_text = f"""
╔══════════════════════════════════════╗
║      🔑 PASSWORD GENERATED 🔑         ║
╚══════════════════════════════════════╝

**Password:** `{pwd}`
📏 **Length:** {length} characters

⚠️ Copy now - won't be shown again!

💫 **RAHUL WORLD - Secure Password**
"""
        await query.message.reply_text(pwd_text, parse_mode="Markdown")
        await query.answer()
    
    elif data.startswith("a"):
        parts = data.split("_")
        qid = int(parts[1])
        ans = int(parts[2])
        await check_answer(query, qid, ans)

# ================= QUIZ =================
questions = [
    ["What is 2FA?", ["Two Factor Authentication", "Two Form Auth", "Double Authentication"], 0],
    ["What is Phishing?", ["Fake emails/websites to steal data", "Computer Virus", "Network Hacking"], 0],
    ["Which is a strong password?", ["X9#mK2$pL8@qR", "password123", "admin2024"], 0]
]

async def send_question(query):
    qid = quiz_scores.get(f"{query.from_user.id}_q", 0)
    if qid >= len(questions):
        score = quiz_scores.get(query.from_user.id, 0)
        uid = query.from_user.id
        if uid not in user_stats:
            user_stats[uid] = {"quizzes": 0, "passwords": 0}
        user_stats[uid]["quizzes"] = user_stats[uid].get("quizzes", 0) + 1
        
        complete_text = f"""
╔══════════════════════════════════════╗
║         🎓 QUIZ COMPLETED 🎓          ║
╚══════════════════════════════════════╝

📊 **Your Score:** {score}/{len(questions)}
🏆 **Percentage:** {int(score/len(questions)*100)}%

💫 **RAHUL WORLD - Keep Learning!**
"""
        await query.message.reply_text(complete_text)
        return
    
    q = questions[qid]
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"A) {q[1][0][:30]}", callback_data=f"a_{qid}_0")],
        [InlineKeyboardButton(f"B) {q[1][1][:30]}", callback_data=f"a_{qid}_1")],
        [InlineKeyboardButton(f"C) {q[1][2][:30]}", callback_data=f"a_{qid}_2")]
    ])
    
    question_text = f"""
╔══════════════════════════════════════╗
║         📚 CYBER QUIZ 📚              ║
╚══════════════════════════════════════╝

❓ **Question {qid+1}/{len(questions)}**

{q[0]}

💫 **RAHUL WORLD - Test Your Knowledge**
"""
    await query.message.reply_text(question_text, reply_markup=kb)

async def check_answer(query, qid, ans):
    if ans == questions[qid][2]:
        quiz_scores[query.from_user.id] = quiz_scores.get(query.from_user.id, 0) + 1
        await query.answer("✅ Correct! +1 Point", show_alert=True)
    else:
        correct = questions[qid][1][questions[qid][2]]
        await query.answer(f"❌ Wrong! Answer: {correct}", show_alert=True)
    
    quiz_scores[f"{query.from_user.id}_q"] = qid + 1
    await send_question(query)

# ================= PASSWORD CHECKER =================
@bot.on_message(filters.text & ~filters.command(["start"]))
async def check_input(_, message):
    text = message.text.strip()
    
    # Check if IP/Domain
    if re.match(r'^[\d\.]+$', text) or re.match(r'^[\w\-\.]+\.\w+$', text):
        await message.reply_text(f"""
╔══════════════════════════════════════╗
║         🌐 IP LOOKUP RESULT 🌐        ║
╚══════════════════════════════════════╝

📡 **Query:** {text}
📍 **Demo Mode:** Educational Purpose

💫 **RAHUL WORLD - Cyber Shield**
""")
        return
    
    # Check password strength
    if len(text) < 50:
        score = 0
        feedback = []
        
        # Length check
        if len(text) >= 12:
            score += 30
            feedback.append("✅ Excellent length (12+ chars)")
        elif len(text) >= 8:
            score += 20
            feedback.append("✅ Good length (8-11 chars)")
        else:
            score += 10
            feedback.append("⚠️ Short length (<8 chars)")
        
        # Character checks
        if re.search(r'[A-Z]', text):
            score += 20
            feedback.append("✅ Has uppercase letters")
        else:
            feedback.append("❌ Missing uppercase")
        
        if re.search(r'[a-z]', text):
            score += 10
            feedback.append("✅ Has lowercase letters")
        else:
            feedback.append("❌ Missing lowercase")
        
        if re.search(r'\d', text):
            score += 20
            feedback.append("✅ Has numbers")
        else:
            feedback.append("❌ Missing numbers")
        
        if re.search(r'[!@#$%]', text):
            score += 20
            feedback.append("✅ Has special characters")
        else:
            feedback.append("❌ Missing special chars")
        
        # Strength level
        if score >= 80:
            level = "🟢 VERY STRONG"
            emoji = "🔒⭐"
        elif score >= 60:
            level = "🟡 STRONG"
            emoji = "🔒"
        elif score >= 40:
            level = "🟠 MEDIUM"
            emoji = "⚠️"
        else:
            level = "🔴 WEAK"
            emoji = "❌"
        
        # Update stats
        uid = message.from_user.id
        if uid not in user_stats:
            user_stats[uid] = {"quizzes": 0, "passwords": 0}
        user_stats[uid]["passwords"] = user_stats[uid].get("passwords", 0) + 1
        
        result = f"""
╔══════════════════════════════════════╗
║      🔐 PASSWORD STRENGTH REPORT     ║
╚══════════════════════════════════════╝

{emoji} **Strength:** {level}
📊 **Score:** {score}/100

📋 **Analysis:**
{chr(10).join(feedback)}

💫 **RAHUL WORLD - Stay Secure**
"""
        await message.reply_text(result)

# ================= HELP =================
@bot.on_message(filters.command("help"))
async def help_cmd(_, message):
    help_text = """
╔══════════════════════════════════════╗
║         🛡️ HELP MENU 🛡️              ║
╚══════════════════════════════════════╝

📝 **Commands:**
/start - Main Menu
/help - This Menu

🔧 **Features:**
• Send any password → Check strength
• Send domain/IP → Lookup info
• Use buttons for more options

💫 **RAHUL WORLD - Cyber Shield**
👨‍💻 @RAHUL_MODS_OWNER
"""
    await message.reply_text(help_text)

# ================= MAIN =================
async def main():
    os.system("clear")
    
    print("""
╔══════════════════════════════════════╗
║     🌟 WELCOME TO RAHUL WORLD 🌟      ║
║    🛡️ CYBER SHIELD BOT v3.0 🛡️       ║
║    🔐 Educational Cybersecurity      ║
║    👨‍💻 @RAHUL_MODS_OWNER              ║
╚══════════════════════════════════════╝

✅ Bot Starting...
""")
    
    await bot.start()
    
    print("""
╔══════════════════════════════════════╗
║         ✅ BOT IS RUNNING! ✅         ║
║    💫 POWERED BY RAHUL WORLD 💫       ║
║    👑 @RAHUL_MODS_OWNER              ║
╚══════════════════════════════════════╝
""")
    
    # Keep bot running
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())