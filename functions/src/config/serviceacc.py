import os
import json
import base64
from dotenv import load_dotenv
from pathlib import Path

if not os.getenv("FUNCTIONS_CONFIG_SERVICE_KEY"):
    env_path = Path(__file__).resolve().parents[2] / ".env"
    load_dotenv(env_path)

class Serviceacc:
    @staticmethod
    def fix_base64_padding(encoded_str):
        """Ensure the Base64 string has correct padding."""
        missing_padding = len(encoded_str) % 4
        if missing_padding:
            encoded_str += "=" * (4 - missing_padding)
        return encoded_str

    @staticmethod
    def get_service_acc():
        encode_key = os.getenv("FUNCTIONS_CONFIG_SERVICE_KEY")
        if not encode_key:
            raise ValueError("Service account key not found")

        serviceacc = Serviceacc()
        encode_key = serviceacc.fix_base64_padding(encode_key)
        decode_key = base64.b64decode(encode_key)
        return json.loads(decode_key)