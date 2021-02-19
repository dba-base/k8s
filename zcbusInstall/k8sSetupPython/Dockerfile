FROM reg.zbomc.com/zcbus/zcbus-prepare-base:v2.1.1 

ENV LANG en_US.UTF-8

WORKDIR /usr/src/app
RUN mkdir templates
#COPY k8sZcbusSetup's all file to /usr/src/app
COPY g.py main.py zcbus.py /usr/src/app/
COPY templates/ /usr/src/app/templates
RUN pip3 install pyyaml \
    && pip3 install jinja2 \
    && pip3 install click
ENTRYPOINT [ "python3", "main.py" ]
