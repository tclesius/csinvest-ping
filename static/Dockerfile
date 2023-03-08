FROM ubuntu 
RUN apt update 
RUN apt install -y apache2
RUN apt install -y apache2-utils 
RUN apt-get install -y git
RUN git clone https://github.com/tclesius/csinvest-ping.git
RUN cp -r csinvest-ping/static/* /var/www/html
RUN rm -rf ~/csinvest-ping
RUN apt clean 
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]