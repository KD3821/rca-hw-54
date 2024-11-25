# rca-hw-54
Rioran Code Academy - class 54 - homework on Server Sent Events &amp; fastapi.

### Homework:

Your college tryed to build a fastapi SSE application with AI. But only got some unconnected files, all is a mess. Now it is up to you to save the day!

0) Fork this repository.
1) Set up templating and enable work with static. When done correctly - you'll see messages appear on index page every second.
2) We don't need THAT much messages! Limit amount of visible messages to 20. Might need some JS touch.
3) Add a personal touch. Seeing seconds is lame. Make it any updates stream of your choice. Forum logins? Fake price changes? Your call.
4) Drop your fork link to the HomeWork Form (check our channel).

**Feel like a web superhero?** Wanna shine brighter than average? Apply SSE to our [cat vote system](https://github.com/Rioran/rca-fastapi-hw) so that results page updates on the go. And don't forget to deploy! Koyeb or any other service.

### useful commands:

```bash
python -m venv venv
```

```bash
venv/Scripts/activate
```

```bash
pip install -r requirements.txt
```

```bash
uvicorn app.main:app --reload
```