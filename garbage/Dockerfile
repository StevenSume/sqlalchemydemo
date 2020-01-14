FROM selidocker.lmera.ericsson.se/proj-iotanalytics-dockerlocal/iae-python3/iae-python3:latest
ADD . /
WORKDIR /
RUN pip3 install -r requirements.txt
RUN chomd +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]