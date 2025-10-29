# -------------------------------
# 🌐 Morse Code Converter Web App
# Built using Flask
# Features:
#   ✅ Text → Morse conversion
#   ✅ Morse → Text conversion
#   ✅ Reuses your existing logic
#   ✅ Graceful error handling
# -------------------------------

from flask import Flask, render_template, request

app = Flask(__name__)

# ----------------------------------------
# 🔸 Morse Code Dictionary
# ----------------------------------------
MORSE_CODE_DICT = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "!": "-.-.--",
    ":": "---...",
    "'": ".----.",
    ";": "-.-.-."
}

# Reverse dictionary for Morse → Text conversion
REVERSE_MORSE = {value: key for key, value in MORSE_CODE_DICT.items()}


# ----------------------------------------
# 🔹 Function: Convert Text → Morse Code
# ----------------------------------------
def text_to_morse(text):
    output = []
    for char in text.lower():
        if char in MORSE_CODE_DICT:
            output.append(MORSE_CODE_DICT[char])
        else:
            continue  # Skip unsupported chars
    return " ".join(output)


# ----------------------------------------
# 🔹 Function: Convert Morse → Text
# ----------------------------------------
def morse_to_text(code):
    words = code.split(" / ")  # Split by slash for words
    decoded_message = []

    for word in words:
        letters = word.split()
        decoded_word = ""
        for symbol in letters:
            decoded_word += REVERSE_MORSE.get(symbol, "?")
        decoded_message.append(decoded_word)

    return " ".join(decoded_message)


# ----------------------------------------
# 🔹 Flask Routes
# ----------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    error = ""
    mode = "text_to_morse"  # Default mode

    if request.method == "POST":
        mode = request.form.get("mode")
        user_input = request.form.get("user_input", "").strip()

        if not user_input:
            error = "⚠️ Please enter something to convert!"
        else:
            if mode == "text_to_morse":
                result = text_to_morse(user_input)

            elif mode == "morse_to_text":
                # Validation: ensure only valid Morse characters are present
                valid_chars = {".", "-", "/", " ", "\n"}
                if not all(ch in valid_chars for ch in user_input):
                    error = "⚠️ That doesn’t look like Morse code! Please use only dots (.), dashes (-), slashes (/), and spaces."
                else:
                    result = morse_to_text(user_input)

    return render_template("index.html", result=result, error=error, mode=mode)



# ----------------------------------------
# 🔹 Run Flask App
# ----------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
