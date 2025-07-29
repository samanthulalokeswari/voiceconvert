import pyttsx3
import speech_recognition as sr



def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()



def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... (Start speaking, and pause to finish)")

        try:
            # Listens until you stop speaking
            audio = recognizer.listen(source)

            print("Processing your speech...")
            text = recognizer.recognize_google(audio)
            return text

        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Network or API error."


def main():
    while True:
        print("\nChoose an option:")
        print("1. Text-to-Speech")
        print("2. Speech-to-Text ")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3: ")

        if choice == '1':
            text = input("Enter text to speak: ")
            text_to_speech(text)

        elif choice == '2':
            result = speech_to_text()
            print(f"Recognized text: {result}")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid input. Try 1, 2, or 3.")


if __name__ == "__main__":
    main()
