import fastapi as _fastapi
import json
from typing import Optional
from fastapi import Query


app = _fastapi.FastAPI()


with open('gubrefiyatlari.json','r') as f:
    gubreler = json.load(f)

@app.get("/")
def root():
    return gubreler


#tüm ürünler ve arama için
@app.get('/search',status_code=200)
def search_urun(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        return gubreler
    else:
        gubre = [p for p in gubreler if name.lower() in p ['urunismi'].lower()]
        return gubre

#toros ürünleri için
@app.get('/toros',status_code=200)
def search_urun(name: Optional[str] = Query(None, title="Name",description="Aranacak Ürün Giriniz.")):
    if name is None:
        return [p for p in gubreler if 'toros'.lower() in p ['urunismi'].lower()]
    else:
        gubre = [p for p in gubreler if name.lower() in p ['urunismi'].lower()]
        return gubre