---

# InstagramBot

An automated bot for logging into Instagram and posting comments on specific posts, developed using Python and Selenium WebDriver.

## Features

- Log into Instagram automatically using provided credentials.
- Simulate human-like typing for comments.
- Post comments on Instagram posts.
  
## Prerequisites

- [Selenium](https://pypi.org/project/selenium/) installed (`pip install selenium`)
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for Firefox installed and added to your system's PATH.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-repo/instagram-bot.git
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Download GeckoDriver [here](https://github.com/mozilla/geckodriver/releases).

## Usage

1. Modify the script to include your Instagram username and password in the following line:

```python
user = InstagramBot("your_username", "your_password")
```

2. Add the Instagram post link where you want to post comments in the `driver.get()` method inside the `comente_na_foto` function.

3. Run the script:

```bash
python instagram_bot.py
```

The bot will log in to Instagram, navigate to the specified post, and leave comments.

## Code Walkthrough

### `__init__(self, username, password)`
Initializes the bot, setting up a Firefox browser session with custom preferences (Portuguese language and disabled notifications).

### `login(self)`
Automates the login process by navigating to the Instagram login page, entering the username and password, and logging in.

### `type_like_a_person(sentence, single_input_field)`
Simulates human-like typing by typing each letter of the comment with a small random delay between each keypress.

### `comente_na_foto(self)`
Automates the process of navigating to a specific Instagram post and posting comments from a predefined list.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

--- 

This format follows the common structure found in GitHub README files for easy understanding and use by developers.
