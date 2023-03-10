from termcolor import colored


def input_error(func) -> str:
    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except KeyError as exception:
            return exception.args[0]

        except ValueError:
            return colored("You forgot to enter the author name or tags.", "red")

        except IndexError:
            return colored("Can't find quote of this author or the tag.", "red")

        except TypeError:
            return colored("Unknown command or parameters, please try again.", "red")

        except AttributeError as exception:
            return exception.args[0]

    return inner
