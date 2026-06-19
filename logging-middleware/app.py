from fastapi import FastAPI
app = FastAPI()

@app.post('/evaluation-service/logs')
def log_insert(string:"stack" , string:"level", string:"package", string:"message"):

    store = {}
    store.stack=stack
    store.level=level
    store.package=package
    store.message=message
    log_id=generate(id)
    if log_id:
        print("log_id":log_id)
        print("message:log created sucessfully")
    if type(stack)!=string:

        raise HTTPException(errorcode=403,message=datatype mismatch)

