FROM miguelpduarte/nsjail-ctf

ENV TIME_LIMIT=300

RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*

COPY ./private/flag.txt /home/ctf/chal/
COPY ./private/chall.py /home/ctf/chal/

EXPOSE 1337/tcp
CMD ["/chal/chall.py"]
