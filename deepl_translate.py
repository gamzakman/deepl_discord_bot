import deepl
import configparser


# creating the object of configparser
config_data = configparser.ConfigParser()
# reading data
config_data.read("config.ini")
# auth key
auth = config_data["auth"]

auth_key = auth.get("key")  # Replace with your key
print(auth_key)
translator = deepl.Translator(auth_key)

result = translator.translate_text("Hello, world!", target_lang="EN-US")
print(result.text)  # "Bonjour, le monde !"