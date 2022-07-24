# mp3 from youtube

A script to download videos from youtube as mp3 file. Uses pytube.

## How to use

Create and activate virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Add youtube urls of songs to download in `urls.txt`. For example:

```
https://www.youtube.com/watch?v=iLLydSZOR8k
https://www.youtube.com/watch?v=63brW1YoLvY
https://www.youtube.com/watch?v=eQOkCQ6CQxA
```

Run the script `download.py`.

```
python download.py
```

Open `/music` folder.