# dockerfile, Image, Container 
FROM python:3.9

ADD main.py .
ADD card.py .
ADD deck.py .
ADD player.py .
ADD gofishgame.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]