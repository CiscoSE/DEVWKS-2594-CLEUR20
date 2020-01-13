FROM  fedora:31
LABEL maintainer "Tim Miller <timmil@cisco.com>"

WORKDIR /opt

# Install python and pip (add 'yum update -y' if publishing build)
RUN yum install -y python-pip \
        && yum clean all

# Install required Python modules
RUN     yes | pip install --upgrade requests prometheus_client 

COPY    payloads.py connection.py collect.py /opt/
EXPOSE  8888
USER    nobody

CMD [ "/usr/bin/python3", "/opt/collect.py" ]
