from urls import app
import  uvicorn

if __name__ == '__main__':
    # uvicorn run:app --reload
    uvicorn.run(app=app)

