FROM  fedora:31
LABEL maintainer "Tim Miller <timmil@cisco.com>"

WORKDIR /opt

# Install python and pip (add 'yum update -y' if publishing build)
RUN yum install -y python-pip \
        && yum clean all

# Install required Python modules
RUN     yes | pip install --upgrade requests prometheus_client isodate

COPY    payloads.py connection.py visualize.py /opt/

EXPOSE  8888
USER    nobody

ENV  NXAPI_HOST "host.docker.internal"
ENV  NXAPI_PORT "23456"
ENV  NXAPI_USER "admin"
ENV  NXAPI_PASS "admin"

CMD [ "/usr/bin/python3", "/opt/visualize.py", "--container" ]

