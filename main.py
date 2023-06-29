from fastapi import FastAPI,Depends,HTTPException,status
from pydantic import BaseModel
from starlette.responses import JSONResponse
import joblib
import uvicorn

app = FastAPI(title="API Startup", description="Predict", version="1.0")

class StartupData(BaseModel):
    RdSpend: float = 73721
    Administration: float = 121344
    Marketing: float = 211025

@app.on_event("startup")
def startup_event():
    global model 
    model = joblib.load("company.pkl")
    print(" MODEL LOADED!!")
    return model

@app.get("/")
def home():
    return {"http://localhost:8000/docs"}

@app.get("/predict")
async def predictget(data:StartupData=Depends()):
    try:
        X = [[data.RdSpend, data.Administration, data.Marketing]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'result':res}
    except:
        raise HTTPException(status_code=404, detail="error")
    
@app.post("/predict")
async def predictpost(data:StartupData):
    try:
        X = [[data.RdSpend, data.Administration, data.Marketing]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'result':res}
    except:
        raise HTTPException(status_code=404, detail="error")



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
