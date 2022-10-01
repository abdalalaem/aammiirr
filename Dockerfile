FROM aammiirr/userbot:slim-buster

#clonning repo 
RUN git clone https://github.com/aammiirriq/aammiirr.git /root/aammiirr 
#working directory 
WORKDIR /root/aammiirr

# Install requirements
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["aammiirr3","-m","aammiirr"]
