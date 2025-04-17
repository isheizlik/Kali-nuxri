from telethon import events, Button
import json
import os

ADMINS_FILE = "admins.json"
ADMIN_STATE_FILE = "admin_state.txt"

def load_admins():
    if not os.path.exists(ADMINS_FILE):
        with open(ADMINS_FILE, "w") as f:
            json.dump([], f)
    with open(ADMINS_FILE, "r") as f:
        return json.load(f)

def save_admins(admins):
    with open(ADMINS_FILE, "w") as f:
        json.dump(admins, f, indent=4)

def register_admin_handler(bot):

    @bot.on(events.NewMessage(pattern="/admin"))
    async def show_admin_panel(event):
        admins = load_admins()
        if event.sender_id not in admins:
            return await event.reply("❌ Siz admin emassiz!")

        btns = [
            [Button.inline("➕ Admin qo‘shish", b"add_admin")],
            [Button.inline("➖ Admin o‘chirish", b"remove_admin")],
            [Button.inline("👥 Adminlar ro‘yxati", b"list_admins")]
        ]
        await event.respond("🔐 Admin boshqaruvi", buttons=btns)

    @bot.on(events.CallbackQuery(data=b"add_admin"))
    async def ask_new_admin(event):
        with open(ADMIN_STATE_FILE, "w") as f:
            f.write("add")
        await event.respond("✏️ Yangi adminning Telegram ID raqamini yuboring:")

    @bot.on(events.CallbackQuery(data=b"remove_admin"))
    async def ask_remove_admin(event):
        with open(ADMIN_STATE_FILE, "w") as f:
            f.write("remove")
        await event.respond("❌ O‘chirish uchun admin ID raqamini yuboring:")

    @bot.on(events.CallbackQuery(data=b"list_admins"))
    async def list_admins(event):
        admins = load_admins()
        if not admins:
            await event.respond("🛑 Adminlar ro‘yxati bo‘sh.")
        else:
            text = "📋 Adminlar ro‘yxati:\n\n"
            for i, admin in enumerate(admins, start=1):
                text += f"{i}. <code>{admin}</code>\n"
            await event.respond(text, parse_mode="html")

    @bot.on(events.NewMessage(pattern=r"^\d+$"))
    async def handle_admin_input(event):
        if not os.path.exists(ADMIN_STATE_FILE):
            return

        with open(ADMIN_STATE_FILE, "r") as f:
            state = f.read().strip()

        admins = load_admins()
        admin_id = int(event.raw_text.strip())

        if state == "add":
            if admin_id in admins:
                await event.reply("⚠️ Bu admin allaqachon mavjud.")
            else:
                admins.append(admin_id)
                save_admins(admins)
                await event.reply("✅ Admin muvaffaqiyatli qo‘shildi.")
        elif state == "remove":
            if admin_id in admins:
                admins.remove(admin_id)
                save_admins(admins)
                await event.reply("✅ Admin o‘chirildi.")
            else:
                await event.reply("❌ Bunday admin topilmadi.")

        os.remove(ADMIN_STATE_FILE)