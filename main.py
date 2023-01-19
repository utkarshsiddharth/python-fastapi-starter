# Entrypoint for our API Server 

import uvicorn

if __name__ == '__main__':
    uvicorn.run("api.app:app", port=8000, reload=True)
