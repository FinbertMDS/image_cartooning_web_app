FROM yoanlin/opencv-python3

RUN apt-get update -q -y \
      && pip install --upgrade pip \
      && pip install streamlit

RUN mkdir /appdir
WORKDIR /appdir

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY setup.sh setup.sh
RUN "./setup.sh"
COPY run_app.sh run_app.sh

ENTRYPOINT [ "/bin/bash", "./run_app.sh"]