FROM aammiirr/userbot:slim-buster

#clonning repo 
RUN git clone https://github.com/aaddr2iq/aaddr2.git /root/aaddr2
#working directory 
WORKDIR /root/aammiirr

# Install requirements
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["jepthon3","-m","aaddr2"]
