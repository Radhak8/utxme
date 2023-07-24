from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 23616438
    API_HASH = "5e18eb26670d22c6e10cdfa6f3d47853"
    # the name to display in your alive message
    ALIVE_NAME = "RadhaUserbot"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = ""
    # After cloning the repo and installing requirements do python3 telesetup.py an fill th this
    LEGEND_STRING = "1BJWap1wBu69MbjrIkpxf7C0Giv8SIOfQJZ2bO1lWqnwP8s6hqzieTKSiPDReTVwqYfSmKBG-IcqKpKyaT6yZ4DWQ2AZViYte3IBKVuNlUz61IoMc3VmD6eRe8_w044pwXPKfwg4dyeOIbyV11RMgdMV4Rf0nLTb8KAQwtXhM9q9Z0xc5wnt94tJNcUGZ2-wzJb3ErcSlL8YdKyM0cXI-aSMDZBummn1r4APoPYezkyKv-5wTU5SOAS2KQcr-WmP1pA9SWAZRb3HSkaIPUqOhh1Y9uUMFrjacaIOgmswIe03vQDJWo23SSQiyUoF1BUQesVPCKydDNSzVe0dXL6wUuHLsxZMwgjQ="
    # create a new bot in @botfather and fill the following vales with bottoken
    BOT_TOKEN = "6081538712:AAHkJZitDGWKq-cBUTuYk1LF5vJQEUedJfs"
    # command handler
    HANDLER = "."
    # command hanler for sudo
    SUDO_HANDLER = "."
    # External plugins repo
    EXTERNAL_REPO = True
    EXTERNAL_REPOBRANCH = "main"
    UPSTREAM_REPO = "pro"
    VCMODE = False
    # Your City's TimeZone
    TZ = "Asia/Kolkata"
