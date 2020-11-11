# See https://github.com/DownUnderCTF/Challenges_2020_public/blob/master/pwn/return-to-whats-revenge/Dockerfile
FROM miguelpduarte/nsjail-ctf

# ensure that libc is consistent, the ubuntu images update sometimes
# COPY ./private/libc.so.6 /lib/x86_64-linux-gnu/libc.so.6
COPY ./private/shellcoat /home/ctf/chal/
COPY ./private/flag.txt /home/ctf/chal/
EXPOSE 1337/tcp
CMD ["/chal/shellcoat"]
