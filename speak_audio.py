import pyttsx3


class Speak:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.set_default()

    def set_default(self):
        self.set_volume(1.0)
        self.set_speaker(1)
        self.set_speech_rate(170.0)

    def set_volume(self, volume: float) -> None:
        """
        :param volume: floating point number: 0 -> 1 | set volume to the speaker
        :return: None
        """
        self.engine.setProperty('volume', volume)

    def set_speaker(self, speaker: int) -> None:
        """
        :param speaker: 0 - male | 1 - female
        :return: None
        """
        self.engine.setProperty('voice', self.engine.getProperty('voices')[speaker].id)

    def set_speech_rate(self, rate: float) -> None:
        """
        :param rate: floating point number - the speed of speaking the text
        :return: None
        """
        self.engine.setProperty('rate', rate)  # setting up new voice rate

    def speak(self, s: str) -> None:
        """
        :param s: the text string the system will speak
        :return: None
        """
        self.engine.say(s)
        self.engine.runAndWait()
