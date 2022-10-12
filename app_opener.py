from AppOpener import run
import requests

OWM_API_KEY = "5a6566f939417827536ffec58230f2a4"
LAT = 29.760427
LON = -95.369804
OWM_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={OWM_API_KEY}"


def execute(s: str) -> str:
    """
    :param s: s - string containing the name of the app to open
    :return: feedback: string - depending on the command
    """
    command: list[str] = s.lower().split(" ")
    feedback = ""

    if "weather" in command:
        response = requests.get(url=OWM_URL)
        content = response.json()
        feedback = f"The sky right now is mostly {content['weather'][0]['description']} with " \
                   f"temperature of {content['main']['temp']} degree Fahrenheit; " \
                   f"and current wind speed is {content['wind']['speed']} miles per hour! " \
                   f"This is the end of today's weather forecast!"

        if "and" in command:
            command.pop(command.index('and'))
            feedback += " And "

    if "open" in command:
        feedback += "I am also opening: "
        # ----Extracting the name of the programs to open---- #
        sub_lst = command[command.index("open") + 1:]  # get a sub-list containing only the name of the apps to open
        app_name = " ".join(sub_lst)  # create a full sentence out of it
        app_name = app_name.replace(' and ', ', ')  # replace " and " with ', ' for the AppOpener to work
        # --------------------------------------------------- #
        feedback += app_name
        run(app_name)

    return "No command recognized! Please Try Again!" if feedback == '' else feedback
