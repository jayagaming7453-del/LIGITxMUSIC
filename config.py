from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("22625485"))
API_HASH = getenv("d9a1e60445bdbf6626d03fe5aa45f577")

BOT_TOKEN = getenv("8314453591:AAFF6M3vZwuN_tGUacHMFc-d-K-5KHOGtiQ", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("7730034853"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/b3d0e737737d67a5bf5a5.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sastatony")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/team_ligit")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
