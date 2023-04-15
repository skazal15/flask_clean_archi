FROM quay.io/qiime2/core:2023.2

WORKDIR /app
ADD . /app

RUN apt-get -y update
RUN apt-get install -y libmariadb-dev gcc

RUN pip install -r requirements.txt

RUN pip install git+https://github.com/kaanb93/q2-krona.git

RUN qiime krona

RUN conda install -c bioconda krona

ENTRYPOINT ["python", "app.py"]
