FROM yud022/HOE-userbot:buster

RUN git clone -b HOE-Userbot https://github.com/yud022/HOE-Userbot /home/HOEuserbot/ \
    && chmod 777 /home/HOEuserbot \
    && mkdir /home/HOEuserbot/bin/

COPY ./sample_config.env ./config.env* /home/HOEuserbot/

WORKDIR /home/HOEuserbot/

CMD ["bash","start"]
