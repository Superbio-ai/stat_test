FROM 221497708189.dkr.ecr.us-west-2.amazonaws.com/ml_resources:python_310

# Install helper packages
RUN apt-get update && \
    apt-get install -y build-essential procps curl file git wget vim && \
    apt-get install -y --no-install-recommends gcc

# Install miniconda3
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh
	
# Make conda activate command available from /bin/bash --interative shells
RUN conda init bash
RUN conda update -n base -c defaults conda
RUN conda install -n base pip
RUN pip install --upgrade pip

RUN mkdir -p /app/
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY app/ /app/
RUN mkdir -p /data/

COPY application.py .

EXPOSE 8000

ENTRYPOINT ["python","application.py"]