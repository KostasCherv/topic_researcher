import os
from src.main import create_interface
from dotenv import load_dotenv

load_dotenv()


# Create and launch the interface
interface = create_interface()
interface.launch(share=True)
