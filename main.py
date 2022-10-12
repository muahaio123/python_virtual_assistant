import speech_recognition as sr
from speak_audio import Speak
from app_opener import execute


def main():
    # set up speech speaker, speech recognizer and microphone to listen to commands
    speaker = Speak()
    r = sr.Recognizer()
    mic = sr.Microphone()
    timeout_sec = 5

    # get the user's speech command
    speaker.speak(f"Microphone will now listen for 10 seconds! It will stop if no speech detected after "
                  f"{timeout_sec} seconds. Please either ask the weather and/or open apps by exact name, "
                  f"separated by 'and' ... it starts now")

    # listen to command
    with mic as source:
        # expect noisy background sound
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout_sec, 10)
        except sr.WaitTimeoutError:  # if user did not provide command in straight 5 seconds
            speaker.speak(f"No audio was picked up by microphone. Please try again!")
        else:
            # transcribing it to text
            speaker.speak("Analyzing Audio")
            try:
                user_command = r.recognize_google(audio)
            except sr.UnknownValueError:
                speaker.speak("Audio was not successfully transcribed. Please try again!")
            else:
                # execute command
                response = execute(user_command)
                print(response)
                speaker.speak(response)


if __name__ == "__main__":
    main()
