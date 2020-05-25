# gen
This is a mini-project to connect a [discord](https://discord.com/) bot to a [language model](https://en.wikipedia.org/wiki/Language_model) so that it might generate interesting responses from a prompt.

## Dependencies
I'm using the following:
* [discord.py v1.3.3](https://pypi.org/project/discord.py/)
* [transformers v2.6.0](https://github.com/huggingface/transformers)
* [Python v3.8.2](https://www.python.org/)

Of course these have their own dependencies, I'm not your package manager.

## How to use
With any luck you only need to do the following:
1. Install the dependencies
2. Clone the repo
3. Create a `config.json` that has at least a single key `token` with your bot's token.
4. `python main.py`

Optionally you can pass the path to a JSON file as the first command-line argument to `main.py`.

The bot is currently configured to listen for messages that start with "$transform" and passes everything that follows in that message to the language model to generate follow-up text. The generated text is sent as a new message. 

## Optional
* Add a link to your GitHub repo as the `github` key in `config.json` to hook up the `$github` command (else it'll point back to my repo :stuck_out_tongue_closed_eyes: )

## Disclaimer
This is for fun, it's not intended to be anything. There are probably many bots like this, but this one is mine.