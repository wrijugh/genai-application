FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip3 install python-dotenv streamlit langchain langchain-openai openai==1.46.0

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "customer.py", "--server.port=8501", "--server.address=0.0.0.0"]