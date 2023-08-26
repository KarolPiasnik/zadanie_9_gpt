How to run server

install python modules:
pip install fastapi
pip install pydantic-settings


install uvicorn server:
pip install uvicorn[standard]

run server app with uvicorn(runs on port 8000 by default):
python -m uvicorn app:app --reload

How to run client:

install httpx with pip

python -m uvicorn app:app --reload --port 5555
access in browse on localhost:5555

