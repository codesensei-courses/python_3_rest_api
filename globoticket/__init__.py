# Note: this code differs from the code
# shown during the course.
# This has been added to fix problems loading dotenv
try:
    from dotenv import load_dotenv
except ImportError:
    from dotenv.main import load_dotenv


load_dotenv()
