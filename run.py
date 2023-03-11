from app import app
from flask_cors import CORS
from dbcreds import production_mode


if (production_mode == True):
    print("Running in Production Mode")
    import bjoern #type: ignore
    bjoern.run(app, "0.0.0.0", 5500)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode!")
    
app.run(debug=True)