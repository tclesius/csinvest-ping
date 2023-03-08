FROM ubuntu 
RUN apt update 
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt-get install -y git
RUN git clone https://github.com/tclesius/csinvest-ping.git
RUN mkdir api
RUN cp -r csinvest-ping/api/* api/
RUN pip3 install -r api/requirements.txt
RUN rm -rf ~/csinvest-ping
RUN apt clean 
EXPOSE 5000

CMD [ "python3", "flask --app api/main run" ]