import os
from cert_issuer_identity import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(port=port)