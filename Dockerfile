FROM registry.4paradigm.com/prophet-saas-base:0.2

HEALTHCHECK --interval=1m CMD ls

MAINTAINER wangyiping@4paradigm.com

COPY image-hub /app

RUN bash /app/install.sh

RUN pip install -r /app/requirements.txt

WORKDIR /app

RUN python2.7 setup.py install

RUN mv /app/start.sh /usr/local/bin/start_cmd && chmod 755 /usr/local/bin/start_cmd

EXPOSE 51005

WORKDIR /root

ENTRYPOINT ["start_cmd"]
