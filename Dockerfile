FROM python:3.9-buster

ENV POETRY_VERSION=1.1.13

RUN apt-get update && apt install -y gcc vim gettext gawk unixodbc-dev flex bison odbc-mdbtools

# Install MDBtools

RUN git clone https://github.com/mdbtools/mdbtools.git

WORKDIR mdbtools/

RUN autoreconf -i -f

RUN ./configure --with-unixodbc=/usr/local

RUN make && make install

RUN ldconfig

WORKDIR /boterham

EXPOSE 8080 5000

COPY poetry.lock pyproject.toml /boterham/

RUN pip install "poetry==${POETRY_VERSION}"

RUN poetry install --no-interaction --no-ansi --no-root

# Need this for Linux builds
RUN poetry add UWSGI

COPY . /boterham

# FOR TESTING ONLY
ENV FLASK_APP=app.py
ENV FP_SK="TEST"
