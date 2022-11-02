FROM python:3.11.0

ENV ARCH amd64
ENV GOVERSION 1.19.2

RUN set -x \
    && cd /tmp \
    && wget https://dl.google.com/go/go$GOVERSION.linux-$ARCH.tar.gz \
    && tar -C /usr/local -xzf go$GOVERSION.linux-$ARCH.tar.gz \
    && rm /tmp/go$GOVERSION.linux-$ARCH.tar.gz

ENV PATH $PATH:/usr/local/go/bin
ENV GOPATH $HOME/work

RUN apt-get update && \
    apt-get install -y util-linux strace cron sysstat less man manpages-dev

# activate sar
RUN sed -i 's/ENABLED="false"/ENABLED="true"/' /etc/default/sysstat && \
    service cron start && \
    /etc/init.d/sysstat start && \
    service cron status && \
    service sysstat status

WORKDIR /linux_practice

COPY .  ./
