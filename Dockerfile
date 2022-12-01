FROM python:latest

RUN apt-get -y update

COPY . .

ADD specific_scraper_election.py .

ADD specific_scraper_imdb_250.py .

ADD specific_scraper_az_animals.py .


RUN pip install -r requirements.txt



ENTRYPOINT ["python3", "./libraries_and_configuration_files/entrypoint.py" ]
