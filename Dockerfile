FROM centos:7
RUN yum install -y python3-3.6.8-10.el7.x86_64 \
    && yum clean all
ADD . /
WORKDIR /
RUN pip3 install -r requirements.txt
RUN chomd +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
