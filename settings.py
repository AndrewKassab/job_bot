import logging

from dotenv import load_dotenv
import os

from pathlib import Path

from selenium import webdriver

from jobbot.app.enum.dice.dice_posted_date import DicePostedDate
from jobbot.app.enum.dice.dice_work_settings import DiceWorkSetting
from jobbot.app.util.parse_pdf import parse_pdf_to_text

load_dotenv()

resources_path = (Path(__file__).parent / 'app' / 'resources')
RESUME_PATH = str((resources_path / 'resume.pdf').resolve())
COVER_LETTER_PATH = str((resources_path / 'cover_letter.pdf').resolve())

try:
    RESUME_TEXT = parse_pdf_to_text(RESUME_PATH)
except:
    logging.error('Error parsing resume, are you sure there is a resume.pdf in app/resources?')

driver = webdriver.Chrome()
driver.implicitly_wait(2)
DRIVER_EXPLICIT_WAIT = 2

# Activates Job description matching and cover letter writing but requires the
# OPENAI_APY_KEY environment variable to be set.
USE_AI = True
if os.environ.get('OPENAI_API_KEY') is None:
    USE_AI = False

# Env Variables
DICE_EMAIL = os.environ.get('DICE_EMAIL')
DICE_PASSWORD = os.environ.get('DICE_PASSWORD')
LINKEDIN_EMAIL = os.environ.get('LINKED_EMAIL')
LINKEDIN_PASSWORD = os.environ.get('LINKEDIN_PASSWORD')

# DICE job search configuration
POSTED_DATE = DicePostedDate.LAST_7_DAYS
WORK_SETTINGS_OPTIONS = [
    DiceWorkSetting.REMOTE,
    #WorkSetting.HYBRID,
    #WorkSetting.ON_SITE,
]
DICE_SEARCH_QUERY = "Java Python Software Engineer Quality Developer Backend"
DICE_LOCATION_QUERY = "San Diego"
