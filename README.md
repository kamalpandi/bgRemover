A simple flask app to remove the background of an image with [Rembg](https://github.com/kamalpandi/bgRemover)

## Run it for local install

```
pip install -r requirements.txt
```
Before running the app, [Downlad model file here](https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx)
```
python app.py
```

## Working

- `Dockerfile`: Contains the instructions to build the Docker image.
- `app.py`: The main Flask application code.
- `requirements.txt`: Lists the Python dependencies.
- `templates/`: Directory containing HTML templates.
- `u2net.onnx`: The ONNX model used by the `rembg` library.

## Docker install
### Prerequisites
> Docker installed on your machine.

``` 
docker build . -t flask-app 
```
```
docker run -p 5100:5100 flask-app
```