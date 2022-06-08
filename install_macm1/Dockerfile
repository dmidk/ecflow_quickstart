FROM ubuntu:18.04

RUN apt-get update && apt-get install -y build-essential
RUN apt-get install -y libxkbcommon-x11-0
RUN DEBIAN_FRONTEND=noninteractive && apt-get install -y xserver-xorg-core xserver-xorg xorg openbox wget
RUN apt-get install -y cmake python3-dev
RUN apt-get install -y qt5-default mesa-common-dev libqt5svg5-dev libqt5charts5-dev

# https://confluence.ecmwf.int/display/ECFLOW/ecflow+v4
ENV WK=/ecflow_source/ecFlow-4.17.2-Source
ENV ECF_NO_PYTHON=1
ENV BOOST_ROOT=/boost_source/boost_1_53_0

RUN mkdir ecflow_source && mkdir boost_source

RUN cd boost_source && \
   wget https://confluence.ecmwf.int/download/attachments/8650755/boost_1_53_0.tar.gz && \
   tar -xvzf boost_1_53_0.tar.gz

RUN cd $BOOST_ROOT && ./bootstrap.sh

RUN cd ecflow_source && \
   wget https://confluence.ecmwf.int/download/attachments/8650755/ecFlow-4.17.2-Source.tar.gz && \
   tar -xvzf ecFlow-4.17.2-Source.tar.gz

RUN cd $BOOST_ROOT && \
    $WK/build_scripts/boost_1_53_fix.sh && \
    $WK/build_scripts/boost_build.sh

RUN cd $WK && \
    mkdir build && \
    cd build && \
    cmake -DENABLE_PYTHON=OFF .. && \
    make && \
    make install

RUN mkdir -p /root/.ecflow_ui/default.session/
COPY servers.txt /root/.ecflow_ui/servers.txt
COPY settings.json /root/.ecflow_ui/default.session/settings.json
COPY session.json /root/.ecflow_ui/default.session/session.json

CMD ["/usr/local/bin/ecflow_ui"]
