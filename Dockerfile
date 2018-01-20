FROM python:3.5-alpine
MAINTAINER Avash Mulmi <avasz@protonmail.com>
MAINTAINER Nootan Ghimire <nootan.ghimire@gmail.com>

WORKDIR /opt/dafuqis/backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
	&& rm requirements.txt

COPY . .

ENTRYPOINT [ "python", "/opt/dafuqis/backend/src/index.py" ]

