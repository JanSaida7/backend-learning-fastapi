print("Test script starting...")
try:
    from fastapi import FastAPI
    print("FastAPI imported successfully")
    
    app = FastAPI()
    print(f"App created: {app}")
    print(f"App type: {type(app)}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
